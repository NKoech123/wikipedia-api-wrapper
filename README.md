# wikipedia-api-wrapper
A wrapper API around the Wikipedia API that allows users to do the
following:
- Retrieve a list of the most viewed articles for a week or a month
  - endpoints:
	  * `/api/v1/mostviewedpermonth/<year>/<month>` *(for a specific month)*
	  * `/api/v1/mostviewedperweek/<year>/<month>/<day>` *(for a specific week)*
- For any given article, be able to get the view count of that specific article for a
week or a month
  - endpoints:
	  * `/api/v1/viewcountperarticle/monthly/<article>/<year>/<month>` *(for a specific month)*
	  * `/api/v1/viewcountperarticle/weekly/<article>/<year>/<month>/<day>` *(for a specific week)*
  
- Retrieve the day of the month where an article got the most page views
  - endpoint:
       * `/api/v1/daywithmostviews/monthly/<year>/<month>` 

## Set up
* Clone the repo `git clone https://github.com/NKoech123/grow.git`
* Activate virtual env `source env/bin/activate`
* Install dependencies `pip3 install -r requirements.txt`
* To run flask app, `python3 main.py`
	* feel free to hit the endpoints
	
	
* To run tests, `cd tests` then `python3 tests.py`
## Retrieve a list of the most viewed articles for a month
<img width="747" alt="Screenshot 2022-11-28 at 1 19 50 AM" src="https://user-images.githubusercontent.com/84946242/204240203-25855187-d7ec-493a-930e-5372b7fbacc6.png">

## Retrieve a list of the most viewed articles for a week
<img width="747" alt="Screenshot 2022-11-29 at 12 07 37 PM" src="https://user-images.githubusercontent.com/84946242/204637311-b627375c-d7e2-4966-82b5-b7f585104604.png">


## Get the view count of that specific article for a month
<img width="747" alt="Screenshot 2022-11-28 at 4 20 27 PM" src="https://user-images.githubusercontent.com/84946242/204408000-f4fbd3ef-6434-41a2-b7c8-86d77a141ece.png">

## Get the view count of that specific article for a week 
<img width="747" alt="Screenshot 2022-11-28 at 4 22 53 PM" src="https://user-images.githubusercontent.com/84946242/204408258-82103d12-3320-4b13-b13e-bd98382c7e2f.png">

## Retrieve the day of the month where an article got the most page views
<img width="747" alt="Screenshot 2022-11-28 at 2 25 49 AM" src="https://user-images.githubusercontent.com/84946242/204254726-87282728-76b1-444e-9bb5-a6b27222804e.png">




