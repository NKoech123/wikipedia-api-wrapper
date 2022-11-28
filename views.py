from fetchurl import fetch_api
from config import MostViewedArticles_uri, ViewCountPerArticle_uri, AllDaysOfTheWeek

class MostViewedArticles:

    def most_viewed_month(self, year, month):
        month = '0' + str(month) if month<10 else month
        url = MostViewedArticles_uri(). get_url_for_mostview_monthly(year, month)
        #url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/{}/{}/all-days".format(year, month)
        resp = fetch_api(url)
        all_month_articles  = resp["items"][0]["articles"]
        return  all_month_articles

    def  most_viewed_week(self, year, month, day):
        dates_of_that_week = AllDaysOfTheWeek().get_all_dates_of_the_week(int(year), int(month), int(day))
        all_week_articles = []
        for date in dates_of_that_week:
            year = date.year
            month = '0' + str(date.month) if date.month < 10 else date.month
            day = '0' + str(date.day) if date.day < 10 else date.day
            url = MostViewedArticles_uri().get_url_for_mostview_weekly(year, month, day)
            #url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikipedia/all-access/{}/{}/{}".format(year, month, day)
            try:
                resp = fetch_api(url)
                articles = resp['items'][0]['articles']
                all_week_articles += articles
            except KeyError as e:
                print((year, month, day))
                print(e)
        # return a message if there's no data in the dates
        # return when dates are invalid
        return all_week_articles


class ViewCounts:

    def monthly_viewcount_of_specific_article(self, article, year, month):
        last_day = calendar.monthrange(int(year), int(month))[1]

        month = '0' + str(month) if int(month) < 10 else month
        start_month_date = str(year) + str(month) + '01' + '00'
        end_month_date =  str(year) + str(month) + str(last_day) + '00'
    
        try:
            url = ViewCountPerArticle_uri().get_url_for_viewcount_monthly_or_weekly(article, start_month_date, end_month_date)
            #url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(article, start_month_date, end_month_date)
            articles = fetch_api(url)
            articles = articles['items']
        except KeyError as e:
            print(e)

        return articles

    def weekly_viewcount_of_specific_article(self, article, year, month, day):
        dates_of_that_week = get_all_dates_of_the_week(int(year), int(month), int(day))
     
        start_week_date =  dates_of_that_week[0]
        year = start_week_date.year
        month = '0' + str(start_week_date.month) if start_week_date.month < 10 else start_week_date.month
        day = '0' + str(start_week_date.day) if start_week_date.day < 10 else start_week_date.day
        start_month_date = str(year) + str(month) + str(day) + '00'

        end_week =  dates_of_that_week[-1]
    
        year = end_week.year
        month = '0' + str(end_week.month) if end_week.month < 10 else end_week.month
        day = '0' + str(end_week .day) if end_week.day < 10 else end_week.day

        end_month_date =  str(year) + str(month) + str(day) + '00'
        
        try:
            url = ViewCountPerArticle_uri().get_url_for_viewcount_monthly_or_weekly(article, start_month_date, end_month_date)
            #url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(article, start_month_date, end_month_date)
            articles = fetch_api(url)
            articles = articles['items']
        except KeyError as e:
            print(e)

        return articles
      

class DayofMonthWhenArticleHasMostPageViews:

    def day_with_most_view_article(self, article, year, month, day):
        last_day = calendar.monthrange(int(year), int(month))[1]
        month = '0' + str(month) if int(month) < 10 else month
        start_month_date = str(year) + str(month) + '01' + '00'

        end_month_date =  str(year) + str(month) + str(last_day) + '00'
       
        try:
            url =  ViewCountPerArticle_uri().get_url_for_viewcount_monthly_or_weekly(article, start_month_date, end_month_date)
            #url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(article, start_month_date, end_month_date)
            articles = fetchAPI(url)
            articles = articles['items']
        except KeyError as e:
            print(e)
     
        max_views = 0
        idx = 0
   
        for index, article in enumerate(articles):
            if 'views' in article and max_views < article['views']:
                max_views, idx = article['views'], index
              
        return  articles[idx]
           
