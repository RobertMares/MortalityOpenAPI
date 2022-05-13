#importing libraries
from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask
from flask_cors import CORS
from mortality.routes import mortalidad

#Initiating the Application
app = Flask(__name__)
CORS(app)

#adding the swagger route to return the json
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

#defining the URL for  Open API Documentation
SWAGGER_URL = '/mortality/v.1/'
API_URL = '/static/swagger.json'

#creating the blueprint to create the Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name" : "Open API Mortality"
    }
)

#registering the Swagger UI Blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
#registering the mortality Blueprint
app.register_blueprint(mortalidad)



#auto debug on save
if __name__ == '__main__':
    app.run(debug=True)
