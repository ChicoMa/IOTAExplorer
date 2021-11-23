from IOTAExplorer import IOTAExplorer
import urllib3
import time
import pandas as pd
from flask import Flask, abort, render_template, redirect, Markup, request, jsonify, make_response, json, abort

@IOTAExplorer.route("/")
# Open HTML file on local computer
def home():
    return render_template("public/home.html")

@IOTAExplorer.route("/search/<category>/<searchable>", methods=["GET"])
def search(category, searchable):
    if category == "transaction":
        command = {
                "command": "getTrytes",
                "hashes": [
                    searchable
                ],
                "page_size": 50
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

        trytes = jsonData["trytes"]
        milestone = jsonData["milestones"]
        x = zip(trytes, milestone)

        return render_template("public/search_transaction.html", category=category, searchable=searchable,x=x)

    if category == "address":
        command = {
            "command": "findTransactions",
            "page_size": 50,
            "addresses": [
                searchable
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

        transaction = jsonData["hashes"]
        value = jsonData["values"]
        milestone = jsonData["milestones"]
        timestamps = jsonData["timestamps"]
        n = 0
        for t in timestamps:
            t= int(t/1000)
            timestamps[n] = time.ctime(t)
            n += 1

        x = zip(timestamps, transaction, value, milestone)
        y = zip(timestamps, transaction, value, milestone)
    
        df = pd.DataFrame(list(y), columns=['Time','Transaction','Value','Milestone'])
        data = df.groupby('Time').Transaction.count().reset_index(name="Count")

        labels = data.loc[:,"Time"]
        values = data.loc[:,"Count"]

        maxA = values.max()

        return render_template("public/search_hints.html", category=category, searchable=searchable, x=x, maxA=maxA,title="Transaction amounts", labels=labels, values=values)

    if category == "bundle":
        command = {
            "command": "findTransactions",
            "bundles": [
                searchable
            ],
            "page_size": 50
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
       

        transaction = jsonData["hashes"]
        value = jsonData["values"]
        milestone = jsonData["milestones"]
        timestamps = jsonData["timestamps"]
        n = 0
        for t in timestamps:
            t= int(t/1000)
            timestamps[n] = time.ctime(t)
            n += 1
             
        x = zip(timestamps, transaction, value, milestone)
        y = zip(timestamps, transaction, value, milestone)
    
        df = pd.DataFrame(list(y), columns=['Time','Transaction','Value','Milestone'])
        data = df.groupby('Time').Transaction.count().reset_index(name="Count")

        labels = data.loc[:,"Time"]
        values = data.loc[:,"Count"]

        maxA = values.max()
        return render_template("public/search_hints.html", category=category, searchable=searchable, x=x, maxA=maxA,title="Transaction amounts", labels=labels, values=values)

    if category == "tag":
        command = {
                "command": "findTransactions",
                "tags": [
                    searchable
                ],
                "page_size": 50
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

        transaction = jsonData["hashes"]
        values = jsonData["values"]
        milestone = jsonData["milestones"]
        timestamps = jsonData["timestamps"]
        n = 0
        for t in timestamps:
            t = int(t/1000)
            timestamps[n] = time.ctime(t)
            n += 1

        x = zip(timestamps, transaction, values, milestone)
        y = zip(timestamps, transaction, values, milestone)
    
        df = pd.DataFrame(list(y), columns=['Time','Transaction','Value','Milestone'])
        data = df.groupby('Time').Transaction.count().reset_index(name="Count")

        labels = data.loc[:,"Time"]
        values = data.loc[:,"Count"]

        maxA = values.max()

        return render_template("public/search_hints.html", category=category, searchable=searchable, x=x, maxA=maxA,title="Transaction amounts", labels=labels, values=values)

    return "Request was not correct", 400

@IOTAExplorer.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@IOTAExplorer.route("/practice")
def prac():
    jsonData = {'hashes': ['IWGZKDYFIVDNVNFMFM9EDZMUO9YSEHMMWQIRCROIDNMJHFPKTJLOB9NWMHFLEI9CATKVFRLEVEJN99999', 'IHGEYHNNNDIYGNRYTYANBPYKLFHGNVSXZVYA9FWGDAOMSXXIOOAWDQPBGSZSYGPMATGEUEJZEJJ9A9999', 'TZBVBTD9EYMFOJAZNCMUHFUTUHLUMADLVIXCTMQKHJORCDEIVQJY9JFWBDLLNYPOCEEZHSHIZLQBZ9999', 'LPX9ZVPQPHJJSTCANNUEZJSLWTPAYHLTT9WSFPXKRGPJVBZXCBRAPLJMXJPYQFLXOLJHJCYUATBGZ9999', 'YQP9CUQXLV9UNCIXRPIDYDJVJVCPPVKGWW9FBUYPCXBUWAOYNAPUJODSLKTHUQSTZFKKKPIOYEXMA9999', 'XQWPRLCPCXEZOVWXZZUQBQCJBRDLDBMTOVUEZ9D9RBBP9EKEZTGO9HLWKWOSDQYUXIYBGIIGCDBBZ9999', 'LTFCYNXGWBZQTHZBS9IQZVAQG9OQRVPHVHZDPXOJ9LGG9PZACBYXGBBKPQQANEDCSXOOOQVSTHSA99999'], 'milestones': [3663575, 3663574, 3663574, 3663574, 3663572, 3663573, 3663575], 'values': [0, 0, 0, 0, 0, 0, 0], 'timestamps': [1619178588111, 1619178588044, 1619178587862, 1619178587852, 1619178587520, 1619178587447, 1619178587308], 'hints': []}
    transaction = jsonData["hashes"]
    values = jsonData["values"]
    milestone = jsonData["milestones"]
    timestamps = jsonData["timestamps"]

    n = 0
    for t in timestamps:
        t = int(t/1000)
        timestamps[n] = time.ctime(t)
        n += 1

    x = zip(timestamps, transaction, values, milestone)
    y = zip(timestamps, transaction, values, milestone)
    
    df = pd.DataFrame(list(y), columns=['Time','Transaction','Value','Milestone'])
    data = df.groupby('Time').Transaction.count().reset_index(name="Count")

    labels = data.loc[:,"Time"]
    values = data.loc[:,"Count"]

    maxA = values.max()
    
    return render_template("public/search_hints.html",max=maxA,title="Transaction amounts", labels=labels, values=values, x=x)


