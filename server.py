# REST API server
# Written By Nate Arkin

from flask import Flask, send_file, abort, request
from flask_restful import Resource, Api
import pandas as pd

# This is a thing that we do. I don't really know why
app = Flask(__name__)
api = Api(app)

# Here we are going to initialize the first endpoint for the api server
class FirstEndpoint(Resource): # FirstEndpoint is the name of the endpoint. It is a resource.
    def get(self): # Here we tell the class that we are defining a get request at the specified endpoint.
        print("Getting Endpoint") # Showing that we are inside the get request, but in development, Flask will also show a line in the output.
        return("Hello, World!") # This will be returned to the browser

# After the return, we attach the endpoint to a url location:
api.add_resource(FirstEndpoint, '/api/v1/endpoints/FirstEndpoint')

# Now, when a browser goes to http://localhost:5002/api/v1/endpoints/FirstEndpoint, they will see a line in the output saying "Hello, World!"

# This starts the server. Needs to stay at the bottom of the document:
if __name__ == '__main__':
    app.run(port=5002)