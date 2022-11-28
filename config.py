class MostViewedArticles_uri:
    def __init__(self):
        self.base_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/"

    def get_url_for_mostview_weekly(self, year: int, month: int, day: int) -> str:
        uri = self.base_url + "{}/{}/{}".format(year, month, day)
        return uri
    
    def get_url_for_mostview_monthly(self, year: int, month: int) -> str:
        uri = self.base_url + "{}/{}/all-days".format(year, month)
        return uri
   
class ViewCountPerArticle_uri:
    def __init__(self):
        self.base_url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/"
    
    def get_url_for_viewcount_monthly_or_weekly(self, article: str, start_month_date: str, end_month_date: str) -> str:
        uri = self.base_url + "{}/daily/{}/{}".format(article, start_month_date, end_month_date)
        return uri


    