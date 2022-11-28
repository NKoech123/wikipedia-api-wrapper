# Grow
Create a wrapper API around the Wikipedia API that allows users to do the
following:
- Retrieve a list of the most viewed articles for a week or a month (You can get the
most viewed articles for a day and their view count. To calculate the most articles
for a week or month, you can assume that an article that is listed for one day but
not listed for another day has 0 views when it’s not listed)
- For any given article, be able to get the view count of that specific article for a
week or a month
- Retrieve the day of the month where an article got the most page views

There are three endpoints:

* `/api/v1/mostviewedpermonth/<year>/<month>` 
* `/api/v1/mostviewedperweek/<year>/<month>/<day>` 
* `/api/v1/viewcountperarticle/monthly/<article>/<year>/<month>`
* `/api/v1/viewcountperarticle/weekly/<article>/<year>/<month>/<day>`
* `/api/v1/daywithmostviews/monthly/<year>/<month>` 


## Set up
* Clone the repo `git clone https://github.com/NKoech123/grow.git`
* Activate virtual env `source env/bin/activate`
* Start by running `pip3 install -r requirements.txt`
* To run flask app, `python3 main.py`
	* feel free to hit the endpoints
	
	
* To run tests, `cd tests` then `python3 tests.py`

<img width="1023" alt="Screenshot 2022-11-28 at 1 19 50 AM" src="https://user-images.githubusercontent.com/84946242/204240203-25855187-d7ec-493a-930e-5372b7fbacc6.png">

<img width="1013" alt="Screenshot 2022-11-28 at 2 25 49 AM" src="https://user-images.githubusercontent.com/84946242/204254726-87282728-76b1-444e-9bb5-a6b27222804e.png">

