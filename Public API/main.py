from flask import *
import json, time

#create flask app
app = Flask(__name__)


#call to endpoint
@app.route('/', methods=['GET'])

def home_page():
    data_set = {'Page': 'Home', 'Messages': 'Successfully loaded the homepage', 'Timestamp': time.time()} #<< gets the current time
    
    #turn data set into json
    json_dump = json.dumps(data_set)
    return json_dump


#call to endpoint 2
@app.route('/user/', methods=['GET'])

def request_page():
    user_query = str(request.args.get('user')) # /user/?user=cfdare2eav

    data_set = {'Page': 'Request', 'Messages': f'Successfully got the request for {user_query}', 'Timestamp': time.time()} #<< gets the current time
    
    #turn data set into json
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run(port=2222)