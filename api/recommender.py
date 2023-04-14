from geopy.distance import geodesic
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def budget_loc_recommendation(lat, long, budget):
    # Filter the data based on the user's budget
    data = pd.read_csv(
        '/home/ayotech/tourist_env/tourist_attraction_api/api/tourism_data.csv')
    data = data[data['price'] <= budget]

    # Compute the distance matrix between tourist places and user country

    # User's location in latitude and longitude
    user_location = (lat, long)
    distances = []
    for _, row in data.iterrows():
        tourist_location = (row['lat'], row['lng'])
        distance = geodesic(user_location, tourist_location).km
        distances.append(distance)

    data['distance'] = distances

    # Filter the data based on the user's location
    max_distance = 50  # Maximum distance from user's location in km
    data = data[data['distance'] <= max_distance]

    # Compute the similarity matrix between tourist places
    tfidf = TfidfVectorizer(stop_words='english')
    data['country'] = data['country'].fillna('')
    tfidf_matrix = tfidf.fit_transform(data['country'])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Get the top n similar tourist places
    n = 10
    indices = pd.Series(data.index)
    recommendations = []

    # Iterate over all tourist places in the similarity matrix
    for i in range(len(data)):
        # Sort the tourist places by similarity score
        similarity_scores = list(enumerate(similarity_matrix[i]))
        similarity_scores = sorted(
            similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the top n similar tourist places
        top_indices = [i[0] for i in similarity_scores[1:n+1]]

        # Get the names of the top n similar tourist places
        top_names = data['name'].iloc[top_indices]

        # Add the recommendations to the list
        recommendations.append(
            {
                'business_status': data['business_status'].iloc[i],
                'tourist_place': data['name'].iloc[i],
                'opening_now': data['opening_hours'].iloc[i],
                'about': data['photos'].iloc[i],
                'location': data["formatted_address"].iloc[i],
                'country': data['country'].iloc[i],
                'price': data['price'].iloc[i],
                'lat': data['lat'].iloc[i],
                'long': data['lng'].iloc[i],
                'ratings': data['ratings'].iloc[i],
                'user_ratings_total': data['user_ratings_total'].iloc[i],
                'types': data['types'].iloc[i],
            })

    return recommendations


def tourism_recommendation(lat, long, budget=1000):
    # Filter the data based on the user's budget
    data = pd.read_csv(
        '/home/ayotech/tourist_env/tourist_attraction_api/api/tourism_data.csv')
    data = data[data['price'] <= budget]

    # Compute the distance matrix between tourist places and user location

    # User's location in latitude and longitude
    user_location = (lat, long)
    distances = []
    for _, row in data.iterrows():
        tourist_location = (row['lat'], row['lng'])
        distance = geodesic(user_location, tourist_location).km
        distances.append(distance)

    data['distance'] = distances

    # Filter the data based on the user's location
    max_distance = 500  # Maximum distance from user's location in km
    data = data[data['distance'] <= max_distance]

    # Compute the similarity matrix between tourist places
    tfidf = TfidfVectorizer(stop_words='english')
    data['country'] = data['country'].fillna('')
    tfidf_matrix = tfidf.fit_transform(data['country'])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Get the top n similar tourist places
    n = 10
    indices = pd.Series(data.index)
    recommendations = []

    # Iterate over all tourist places in the similarity matrix
    for i in range(len(data)):
        # Sort the tourist places by similarity score
        similarity_scores = list(enumerate(similarity_matrix[i]))
        similarity_scores = sorted(
            similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the top n similar tourist places
        top_indices = [i[0] for i in similarity_scores[1:n+1]]

        # Get the names of the top n similar tourist places
        top_names = data['name'].iloc[top_indices]

        # Add the recommendations to the list
        recommendations.append(
            {
                'business_status': data['business_status'].iloc[i],
                'tourist_place': data['name'].iloc[i],
                'opening_now': data['opening_hours'].iloc[i],
                'about': data['photos'].iloc[i],
                'location': data["formatted_address"].iloc[i],
                'country': data['country'].iloc[i],
                'price': data['price'].iloc[i],
                'lat': data['lat'].iloc[i],
                'long': data['lng'].iloc[i],
                'ratings': data['ratings'].iloc[i],
                'user_ratings_total': data['user_ratings_total'].iloc[i],
                'types': data['types'].iloc[i],
            })

    return recommendations


def tourist_type_recommendation(lat, long, keyword, max_distance=50):
    # Load the data from CSV file
    data = pd.read_csv(
        '/home/ayotech/tourist_env/tourist_attraction_api/api/tourism_data.csv')

    # Filter the data based on keyword matching
    mask = (data['types'].str.contains(keyword, case=False)) | (
        data['name'].str.contains(keyword, case=False))
    data = data[mask]

    # Filter the data based on the user's budget
    budget = 1000
    data = data[data['price'] <= budget]

    # Compute the distance matrix between tourist places and user location
    from geopy.distance import geodesic

    # User's location in latitude and longitude
    user_location = (lat, long)
    distances = []
    for _, row in data.iterrows():
        tourist_location = (row['lat'], row['lng'])
        distance = geodesic(user_location, tourist_location).km
        distances.append(distance)

    data['distance'] = distances

    # Filter the data based on the user's location
    max_distance = 50  # Maximum distance from user's location in km
    data = data[data['distance'] <= max_distance]

    # Compute the similarity matrix between tourist places
    from sklearn.feature_extraction.text import TfidfVectorizer

    tfidf = TfidfVectorizer(stop_words='english')
    data['country'] = data['country'].fillna('')
    tfidf_matrix = tfidf.fit_transform(data['country'])
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Get the top n similar tourist places
    n = 10
    indices = pd.Series(data.index)
    recommendations = []

    # Iterate over all tourist places in the similarity matrix
    for i in range(len(data)):
        # Sort the tourist places by similarity score
        similarity_scores = list(enumerate(similarity_matrix[i]))
        similarity_scores = sorted(
            similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the top n similar tourist places
        top_indices = [i[0] for i in similarity_scores[1:n+1]]

        # Get the names of the top n similar tourist places
        top_names = data['name'].iloc[top_indices]

        # Add the recommendations to the lis
        recommendations.append(
            {
                'business_status': data['business_status'].iloc[i],
                'tourist_place': data['name'].iloc[i],
                'opening_now': data['opening_hours'].iloc[i],
                'about': data['photos'].iloc[i],
                'location': data["formatted_address"].iloc[i],
                'country': data['country'].iloc[i],
                'price': data['price'].iloc[i],
                'lat': data['lat'].iloc[i],
                'long': data['lng'].iloc[i],
                'ratings': data['ratings'].iloc[i],
                'user_ratings_total': data['user_ratings_total'].iloc[i],
                'types': data['types'].iloc[i],
            })

    return recommendations
