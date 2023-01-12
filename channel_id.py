import requests
import base64

# Replace these with your own client ID and client secret
client_id = "YOUR CLIENT ID HERE"
client_secret = "YOUR CLIENT SECRET HERE"

# Set the API endpoint URL for generating an access token
token_endpoint = 'https://id.twitch.tv/oauth2/token'

auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")


# Set the request headers for generating an access token
token_headers = {
    "Authorization": f"Basic {auth_header}"
}

# Set the request body for generating an access token
token_data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Make the request to the token endpoint to get an access token
token_response = requests.post(token_endpoint, headers=token_headers, data=token_data)

# Check if the request was successful
if token_response.status_code == 200:
    # Get the access token from the response
    access_token = token_response.json()['access_token']
else:
    # There was an error generating the access token, handle the error
    print(f'Error generating access token: {token_response.json()}')
    exit()

# Set the API endpoint URL for getting user information
user_endpoint = 'https://api.twitch.tv/helix/users'

# Set the request headers for getting user information
user_headers = {
    'Authorization': f'Bearer {access_token}',
    'Client-ID': client_id
}

# Set the request parameters for getting user information
user_params = {
    'login': 'WashedGamerBro'
}

# Make the request to the user endpoint to get user information
user_response = requests.get(user_endpoint, headers=user_headers, params=user_params)

# Check if the request was successful
if user_response.status_code == 200:
    # User was found, process the response
    user_info = user_response.json()['data'][0]
    print(user_info['id'])
else:
    # User was not found, handle the error
    print(f'Error getting user information: {user_response.json()}')
