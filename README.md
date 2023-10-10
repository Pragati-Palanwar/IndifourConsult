# IndifourConsult
An assignment given by Indifour Consult

Project title : api_development
App name : api




Given data : API url - https://api.worldbank.org/v2/countries?format=json




Description :

Under api_development i have created an "api" application.
Within "api" our 3 API call codebase written under views.py and path given in urls.py file.

In api/views.py, 

1. listofcountries --> This API display the list of country names fetched from source url and returns only name of country and iso2Code of 
                       that country.

2. populationyear --> This API returns the population of country within different years, only by providing its countryCode, it fetches all data.

3. tempconver --> This API converts the given temperature in Celcius to Farenheit within JSON format.

In api/urls.py, import all views and set url with its run path.

eg. From api/views.py, 
for listofcountries API, we give path="api1/" with it API connectivity.
    urlpatterns = [path("api1", views.listofcountries, name="listofcountries"),]

for populationyear API, give countrycode as a input parameter from user which we have to add during running the server
    urlpatterns = [path("api2/<countryCode>", views.populationyear, name="populationyear"),]

for tempconvert API, set temperature as a input from User side.
whatever the temperature we entered in celcius, it will be converted into farenheit.
    urlpatterns =[path("api3/<temperature>", views.tempconvert, name="tempconvert"),]

The next step is to point the root URLconf at the api_development.urls module. 
In api_development/urls.py, we include the URLs in the urlpatterns list.




Run project :



we’ll run our "api" app in the same directory as your manage.py(under api_development), so open command propmt/terminal from that.
Run the command:

...\> python manage.py runserver

It runs the server and system check if any issue,we get following lines of server response:

"""
System check identified no issues (0 silenced).

You have unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 11, 2023 - 00:30:54
Django version 4.2.6, using settings 'api_development.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK. 
"""

Now, our application runs properly.



1. listofcountries

for API1 means listofcountries, we have to open the browser and paste following url:

"https://api.worldbank.org/v2/country/<iso2Code>/indicator/SP.POP.TOTL?format=json"

Within <iso2code> we have to enter iso2code of any countries. 
[All countries iso2code given in url : API url - https://api.worldbank.org/v2/countries?format=json
 open it, copy one iso2code and paste it under above link]



 2. populationyear

Copy url from starting development server add path next to it.
    
    Enter url : http://127.0.0.1:8000/api/api2/<countrycode>
    Example : http://127.0.0.1:8000/api/api2/AW

    where api -> root URL path
          api2 -> current api URL
          AW -> countrycode (given under the same source link)



3. tempconvert

Copy url from starting development server add path next to it.

    Enter url : http://127.0.0.1:8000/api/api3/<temperature>
    Example : http://127.0.0.1:8000/api/api3/30

    where 30 -> input temperature from user

    Output:  {'farenheit': 86}





