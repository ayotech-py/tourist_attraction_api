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

## tourist_radius/
This endpoint accepts the radius, latitude and longitude parameters and they are of type ==int.
This endpoint returns details about tourist places within the specified radius to the users location(lat, and long)

## tourist_budget/
This endpoint accepts budget, latitude and longitude parameters and they are of type ==int.
This endpoint returns details about tourist places that their fares are within the users budget and are within a radius of 200km to the users location(lat, and long)

## tourist_type/
This endpoint accepts type(==string), latitude(==int) and longitude(==int) parameters.
This endpoint returns details about tourist places that their type matches the user type and are within a radius of 200km to the user's location(lat, and long)

## tourist_type_radius/
This endpoint accepts type(==string), radius(==int) latitude(==int) and longitude(==int) parameters.
This endpoint returns details about tourist places that their type matches the user type and are within the specified radius to the user's location(lat, and long)

## tourist_search/
This endpoint accepts keyword(==string) and country(==string) parameters
The endpoint returns details about tourist places that matches the keyword within the specified country
