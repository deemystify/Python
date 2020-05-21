# This code will show you how to call the computer vision API from Python.
# The documentation for computer vision analyze Image method can be located via the following website
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa
# Use the requestss library to simplify making a REST API call from Python

#import requests
from pip._vendor import requests

# We will need the json library to read the data passed back by the web service
import json
# We need the key to access our Computer Vision Service
SUBSCRIPTION_KEY = "e3cb0a9f6f104c34bd4828db434af3f4"

# We need the address of our Computer vision service 
vision_service_address = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/"
# Add the name of the function we wnat to call to the address
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function
# There are three optional parameters: language, details and visualFeatures
parameters = {'visualFeatures': 'Description,Color', 'language':'en'}

# Open the image file to get a file object containing the image to analyze
image_path = "C:/LloydImages/noName.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# We need to specify the subscription key and the content type
# in the HTTP headers. Content-Type is application/octet-stream when you pass in an image directly

headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function
# We use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))

 
