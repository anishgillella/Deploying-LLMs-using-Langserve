# Import the requests module to enable HTTP requests from Python
import requests

# Make a POST request to a FastAPI endpoint configured to handle requests for essays
response = requests.post(
    "http://localhost:8000/essay/invoke",  # URL targeting the specific API route for essays
    json={'input': {"topic": "Hitler"}}  # Payload containing the topic for the essay
)

# Print the complete JSON response from the server
print(response.json())  # This prints the entire JSON response object received from the server

# Assuming the server response structure includes 'output' and 'content', extract and print the actual essay content
print(response.json()['output']['content'])  # Extract and print just the content part of the essay from the response
