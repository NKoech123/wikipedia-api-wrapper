from views import MostViewedArticles, ViewCounts, DayofMonthWhenArticleHasMostPageViews
from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/mostviewedpermonth/<year>/<month>')
def most_viewed_articles_per_month(year, month):
    instance = MostViewedArticles()
    most_viewed_per_month = instance.most_viewed_month(year, month)
    return most_viewed_per_month

@app.route('/api/v1/mostviewedperweek/<year>/<month>/<day>')
def most_viewed_articles_for_week(year, month, day):
    instance = MostViewedArticles()
    most_viewed_per_week = instance.most_viewed_week(year, month, day)
    if len(most_viewed_per_week) == 0:
        statement = "No result during this week"
        most_viewed_per_week.append(statement)
    return most_viewed_per_week

@app.route('/api/v1/viewcountperarticle/monthly/<article>/<year>/<month>')
def viewcount_of_specific_article_monthly(article, year, month):
    instance = ViewCounts()
    viewcount = instance.monthly_viewcount_of_specific_article(article, year, month)
    print(viewcount)
    if len(viewcount) == 0:
        statement = "No result during this month"
        viewcount.append(statement)
    return viewcount

@app.route('/api/v1/viewcountperarticle/weekly/<article>/<year>/<month>/<day>')
def viewcount_of_specific_article_weekly(article, year, month, day):
    instance = ViewCounts()
    viewcount = instance.weekly_viewcount_of_specific_article(article, year, month, day)
    if len(viewcount) == 0:
        statement = "No result during this week"
        viewcount.append(statement)
    print(viewcount)
    return viewcount

@app.route('/api/v1/daywithmostviews/monthly/<year>/<month>')
def day_with_most_article_pageviews(year, month):
    instance = DayofMonthWhenArticleHasMostPageViews()
    day_with_most_pageviews = instance.day_with_most_viewed_article(int(year), int(month))
    return  day_with_most_pageviews
      

if __name__ == '__main__':
    app.run(debug=True)