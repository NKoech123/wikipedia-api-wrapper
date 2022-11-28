import sys
sys.path.append("..")

import unittest, datetime

from fetchurl import fetch_api
from config import MostViewedArticles_uri, ViewCountPerArticle_uri, AllDaysOfTheWeek
from views import MostViewedArticles, ViewCounts, DayofMonthWhenArticleHasMostPageViews
from testData import expected_first_article, expected_second_article, expected_last_article, expected_viewcounts_first_article_monthly, expected_viewcounts_first_article_weekly

""" Ensure urls config work as it should """
class Test_MostViewedArticles_uri(unittest.TestCase):
    def test_config_urls_weekly(self):
        actual_url = MostViewedArticles_uri().get_url_for_mostview_weekly(2020,10,2)
        expected_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/2020/10/2"
        self.assertTrue(actual_url, expected_url)
        
    def test_config_urls_monthly(self):
        actual_url = MostViewedArticles_uri().get_url_for_mostview_monthly(10,2)
        expected_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/10/2/all-days"
        self.assertTrue(actual_url, expected_url)

class Test_ViewCountPerArticle_uri(unittest.TestCase):
    def test_config_urls_weekly_or_monthly(self):
        actual_url = ViewCountPerArticle_uri().get_url_for_viewcount_monthly_or_weekly("Alert Einstein","2020100100","2020103000")
        expected_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Alert Einstein/daily/2020100100/2020103000"
        self.assertTrue(actual_url, expected_url)

""" Ensure fetch_api works as it should """
class Test_FetchAPI(unittest.TestCase):
    def test_fetch_api(self):
        response = fetch_api("https://opentdb.com/api.php?amount=1&category=18")
        actual_result = response["results"][0]["category"]
        expected_result = "Science: Computers"
        self.assertTrue(actual_result, expected_result)

class Test_RetrieveAllWeekDaysInTheDaysWeek(unittest.TestCase):
    def test_get_all_dates_of_the_week(self):
        actual_end_week_result = AllDaysOfTheWeek().get_all_dates_of_the_week(2022, 11, 27)
        actual_mid_week_result = AllDaysOfTheWeek().get_all_dates_of_the_week(2022, 11, 23)
        actual_start_week_result= AllDaysOfTheWeek().get_all_dates_of_the_week(2022, 11, 21)

        expected_result = [datetime.date(2022, 11, 21), datetime.date(2022, 11, 22), 
            datetime.date(2022, 11, 23), datetime.date(2022, 11, 24), datetime.date(2022, 11, 25), 
            datetime.date(2022, 11, 26), datetime.date(2022, 11, 27)
        ]
     
        self.assertListEqual(actual_end_week_result,  expected_result)
        self.assertListEqual(actual_mid_week_result,  expected_result)
        self.assertListEqual(actual_start_week_result,  expected_result)

class Test_MostViewedArticles_View(unittest.TestCase):
    def test_most_viewed_month(self):
        all_month_articles = MostViewedArticles().most_viewed_month(2015,10)

        first_article = all_month_articles[0]
        second_article = all_month_articles[1]
        last_article = all_month_articles[-1]
        
        self.assertTrue(first_article, expected_first_article)
        self.assertTrue(second_article, expected_second_article)
        self.assertTrue(last_article, expected_last_article)

    def test_most_viewed_weekly(self):
        all_week_articles = MostViewedArticles().most_viewed_week(2015, 10, 10)
        num_of_articles = len(all_week_articles)
        expected_num_of_articles = 6664
        self.assertTrue(num_of_articles, expected_num_of_articles)

class Test_ViewCounts_View(unittest.TestCase):
    def test_monthly_viewcount_of_specific_article(self):
        view_counts = ViewCounts().monthly_viewcount_of_specific_article('Albert Einstein', 2015, 10)
        num_of_counts = len(view_counts)
        expected_counts = 31
        self.assertTrue(num_of_counts, expected_counts) 
        self.assertTrue(view_counts[0], expected_viewcounts_first_article_monthly) 

    def test_weekly_viewcount_of_specific_article(self):
        view_counts = ViewCounts().weekly_viewcount_of_specific_article('Johann_Wolfgang_von_Goethe', 2022, 11, 9)
        num_of_counts = len(view_counts)
        expected_counts = 7
        self.assertTrue(num_of_counts, expected_counts) 
        self.assertTrue(view_counts[0], expected_viewcounts_first_article_weekly)

class Test_DayofMonthWhenArticleHasMostPageViews(unittest.TestCase):
    def test_day_with_most_view_article(self):
        resp  = DayofMonthWhenArticleHasMostPageViews().day_with_most_viewed_article(2015, 10)
        date_with_max_views = resp["item"][0]["date"]
        expected_date = '2015-10-06'
        self.assertTrue(date_with_max_views, expected_date)


if __name__ == '__main__':
    unittest.main()