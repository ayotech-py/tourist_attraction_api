# Tourism AI Recommendation Service API

An AI recommendation service that gives personalized tourist attraction recommendations based on the following

- Users input (budget, location, radius, search keywords)
- Keyword filter”.
- Feedback (ratings from user) to improve the recommendations.

# Libraries used in building this Service API

This API was built with django restframework alongside other dependencies

- Django
- djangorestframework
- geographiclib
- geopy
- numpy
- pandas
- scikit-learn

# API Endpoints

This API have 6 endpoints that accept POST requests only, here is the live API [https://tourist-api.onrender.com/places/] which was hosted on [https://render.com]

## tourist_attraction/

This endpoint accepts the latitude and longitude parameters and they are of type ==int.
This endpoint returns details about tourist places within a radius of 200km to the users location(lat, and long)

```Python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_attraction/'

response = requests.post(url=url, json={'lat': 55.323322, 'long': 23.287491})
print(response.text)
```

## tourist_radius/

This endpoint accepts the radius, latitude and longitude parameters and they are of type ==int.
This endpoint returns details about tourist places within the specified radius to the users location(lat, and long)

```Python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_radius/'

response = requests.post(url=url, json={'lat': 55.323322, 'long': 23.287491, 'radius': 500})
print(response.text)
```

## tourist_budget/

This endpoint accepts budget, latitude and longitude parameters and they are of type ==int.
This endpoint returns details about tourist places that their fares fall within the users budget and are within a radius of 200km to the users location(lat, and long)

```Python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_budget/'

response = requests.post(url=url, json={'lat': 55.323322, 'long': 23.287491, 'budget': 500})
print(response.text)
```

## tourist_type/

This endpoint accepts keyword(==string), latitude(==int) and longitude(==int) parameters.
This endpoint returns details about tourist places that their type matches the user type and are within a radius of 200km to the user's location(lat, and long)

```Python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_type/'

response = requests.post(url=url, json={'lat': 55.323322, 'long': 23.287491, 'keyword': 'tourist'})
print(response.text)
```

## tourist_type_radius/

This endpoint accepts keyword(==string), radius(==int) latitude(==int) and longitude(==int) parameters.
This endpoint returns details about tourist places that their type matches the user type and are within the specified radius to the user's location(lat, and long)

```Python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_type_radius/'

response = requests.post(url=url, json={'lat': 55.323322, 'long': 23.287491, 'keyword': 'tourist', 'radius': 500})
print(response.text)
```

## tourist_search/

This endpoint accepts keyword(==string) and location(==string) parameters
The endpoint returns details about tourist places that matches the keyword within the specified location,

```Python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_search/'

response = requests.post(url=url, json={'keyword': 'tourist', 'location': 'Georgia'})
print(response.text)
```

# API Response

The api returns a json response containing all tourist places when a post request is sent to the endpoint. The below response was received when a request was sent to the api endpoint

```python
import requests

url = 'https://tourist-api.onrender.com/places/tourist_search/'

response = requests.post(url=url, json={'keyword': 'tourist', 'location': 'Georgia'})
print(response.text)
```

```
{
    "data": [
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Tybee Island Light Station & Museum",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/107004577986193143793\">Tybee Island Light Station And Museum</a>",
            "location": "30 Meddin Dr, Tybee Island, GA 31328, United States",
            "country": "Georgia",
            "price": 470,
            "lat": 32.0221761,
            "long": -80.8457839,
            "ratings": 4.7,
            "user_ratings_total": 5873,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Andersonville National Historic Site",
            "opening_now": true,
            "about": "<a href=\"https://maps.google.com/maps/contrib/109429353588083113779\">Donald Blaylock</a>",
            "location": "760 POW Rd, Andersonville, GA 31711, United States",
            "country": "Georgia",
            "price": 390,
            "lat": 32.2002948,
            "long": -84.1303207,
            "ratings": 4.8,
            "user_ratings_total": 1910,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Savannah's Waterfront",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/100343347859864193239\">sk fry</a>",
            "location": "1 W River St, Savannah, GA 31401, United States",
            "country": "Georgia",
            "price": 410,
            "lat": 32.0818497,
            "long": -81.09184929999999,
            "ratings": 4.7,
            "user_ratings_total": 343,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "EXPEDITION:BIGFOOT! The Sasquatch Museum",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/113729808740085834054\">Frank Brocato</a>",
            "location": "1934 GA-515, Blue Ridge, GA 30513, United States",
            "country": "Georgia",
            "price": 740,
            "lat": 34.80225679999999,
            "long": -84.3761855,
            "ratings": 4.6,
            "user_ratings_total": 2319,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Ocmulgee Mounds National Historical Park",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/106840940755291651286\">Tre Robinson</a>",
            "location": "1207 Emery Hwy, Macon, GA 31217, United States",
            "country": "Georgia",
            "price": 640,
            "lat": 32.8381287,
            "long": -83.6020624,
            "ratings": 4.8,
            "user_ratings_total": 1850,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "George L Smith St Park",
            "opening_now": true,
            "about": "<a href=\"https://maps.google.com/maps/contrib/108811369966888639063\">John Gaines</a>",
            "location": "371 George L Smith State Park Rd, Twin City, GA 30471, United States",
            "country": "Georgia",
            "price": 200,
            "lat": 32.5510315,
            "long": -82.1252435,
            "ratings": 4.7,
            "user_ratings_total": 998,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "World of Coca-Cola",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/114391305206899275712\">A Google User</a>",
            "location": "121 Baker St NW, Atlanta, GA 30313, United States",
            "country": "Georgia",
            "price": 110,
            "lat": 33.7625564,
            "long": -84.39243599999999,
            "ratings": 4.4,
            "user_ratings_total": 27196,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Atlanta Botanical Garden",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/108292276191678605454\">108292276191678605454</a>",
            "location": "1345 Piedmont Ave NE, Atlanta, GA 30309, United States",
            "country": "Georgia",
            "price": 860,
            "lat": 33.7899568,
            "long": -84.37259879999999,
            "ratings": 4.7,
            "user_ratings_total": 16580,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Stone Mountain Park",
            "opening_now": true,
            "about": "<a href=\"https://maps.google.com/maps/contrib/112696527203685564405\">William Maney</a>",
            "location": "1000 Robert E Lee Blvd, Stone Mountain, GA 30083, United States",
            "country": "Georgia",
            "price": 290,
            "lat": 33.8053189,
            "long": -84.1455315,
            "ratings": 4.6,
            "user_ratings_total": 35631,
            "types": "tourist attraction"
        },
        {
            "business_status": "OPERATIONAL",
            "tourist_place": "Wormsloe Historic Site",
            "opening_now": false,
            "about": "<a href=\"https://maps.google.com/maps/contrib/107462942977657280642\">Brenda Peterson</a>",
            "location": "7601 Skidaway Rd, Savannah, GA 31406, United States",
            "country": "Georgia",
            "price": 820,
            "lat": 31.9801931,
            "long": -81.069243,
            "ratings": 4.5,
            "user_ratings_total": 3153,
            "types": "tourist attraction"
        }
    ]
}
```
