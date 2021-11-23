import webbrowser
import urllib3
from flask import flask, request, jsonify, make_response

site = flask.Flask(__name__)
site.config["DEBUG"] = True
new = 2 # Open in a new tab, if possible

@site.route('/', methods=['GET'])
def home():
    # Open HTML file on local computer
    url = "file:///Users/leonorampofu/IOTA%20Explorer/home.html"
    webbrowser.open(url, new=new)

@site.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@site.route('public/search', methods=['GET'])
def api_filter():
    query_parameters = request.args
    
    # Read query parameters provided by user
    transaction = query_parameters.get('tx')
    address = query_parameters.get('address')
    bundle = query_parameters.get('bundle')
    timestamp = query_parameters.get('timestamp')

    #query = "SELECT hash, address, value, timestamp, bundle, milestone FROM mainnet.transaction WHERE"
    to_filter = []
     
    # Filter matching data 
    # Populate table 

    # Build SQL query based on parameters
    if transaction:
        command = {
            "command": "getTrytes",
            "hashes": [
                transaction
            ]
        }
        stringified = json.dumps(command).encode('utf-8')
        http = urllib3.PoolManager()
        headers = {
            'content-type': 'application/json',
            'X-IOTA-API-Version': '1'
        }
        request = http.request('POST', url="157.90.244.179:4000/api", body=stringified, headers=headers)
        returnData = request.data.decode('utf-8')
        jsonData = json.loads(returnData)
        print(jsonData)
        #query += ' transaction=?'
        #to_filter.append(transaction)
    elif address:
        command = {
            "command": "findTransactions",
            "hints.address": [
                address
            ]
        }
        stringified = json.dumps(command).encode('utf-8')
        http = urllib3.PoolManager()
        headers = {
            'content-type': 'application/json',
            'X-IOTA-API-Version': '1'
        }
        request = http.request('POST', url="157.90.244.179:4000/api", body=stringified, headers=headers)
        returnData = request.data.decode('utf-8')
        jsonData = json.loads(returnData)
        print(jsonData)
        #query += ' address=?'
        #to_filter.append(address)
    elif bundle:
        command = {
            "command": "findTransactions",
            "hints.bundle": [
                bundle
            ]
        }
        stringified = json.dumps(command).encode('utf-8')
        http = urllib3.PoolManager()
        headers = {
            'content-type': 'application/json',
            'X-IOTA-API-Version': '1'
        }
        request = http.request('POST', url="157.90.244.179:4000/api", body=stringified, headers=headers)
        returnData = request.data.decode('utf-8')
        jsonData = json.loads(returnData)
        print(jsonData)
        #query += ' bundle=?'
        #to_filter.append(bundle)
    elif timestamp:
        command = {
            "command": "findTransactions",
            "hints.timeline": [
                timestamp
            ]
        }
        stringified = json.dumps(command).encode('utf-8')
        http = urllib3.PoolManager()
        headers = {
            'content-type': 'application/json',
            'X-IOTA-API-Version': '1'
        }
        request = http.request('POST', url="157.90.244.179:4000/api", body=stringified, headers=headers)
        returnData = request.data.decode('utf-8')
        jsonData = json.loads(returnData)
        print(jsonData)
        #query += ' timestamp=?'
        #to_filter.append(timestamp)
    if not (transaction or address or bundle or timestamp):
        return page_not_found(404)
    

    #query = query[:-4] + ';'

#     @app.route("/json", methods=["POST"])
# def json_example():

#     # Validate the request body contains JSON
#     if request.is_json:

#         # Parse the JSON into a Python dictionary
#         req = request.get_json()

#         # Print the dictionary
#         print(req)

#         # Return a string along with an HTTP status code
#         return "JSON received!", 200

#     else:

#         # The request body wasn't JSON so return a 400 HTTP status code
#         return "Request was not JSON", 400

    # # Instantiate Cassandra cluster
    # from cassandra.cluster import Cluster
    # cluster = Cluster(['188.34.184.215'], port=9042)
    #  # Start session and establish connection with keyspace argument
    # session = cluster.connect('mainnet')
    
    
    # # Execute query with prepared statement
    # lookup = session.prepare(query)
    # results = []
    # for x in to_filter:
    #     row = session.execute(lookup, [x])
    #     results.append(row)
    
    # # Returns matches as JSON to user
    # return jsonify(results)

    # # Produce corresponding graph 

site.run()