import json
import os
from flask import Flask, jsonify, request
import redis

#color = {"012245":"red"}

# creating the instance of our flask application
app = Flask(__name__)
db=redis.from_url(os.environ['REDISCLOUD_URL'])

@app.route('/color',methods = ['GET', 'POST'])
#@cross_origin(maxAge = 3600) #web auth
def downloadRoute0(): #change number for every new route!
    #global color
    if(request.method == 'GET'):
        value_key = request.args.get('key')
        value = db.get(value_key)
        if (str(value) == "None"):
            db.set(value_key,'L')
            value = 'L'
        return jsonify({"value" : str(value)})
      #  if color_key in color:
       #  return jsonify({"color" : color[color_key]}) #returns color from app with code
        #else:
         #   return jsonify({"color":"null"})

    elif(request.method == 'POST'):
        value_key = request.args.get('key')
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        #color[color_key] = request_data['color']
        value = db.get(value_key)
        if(str(value) != "None"):
            db.set(value_key,request_data['value']) #original request_data["color"]
        return ' '
      


if __name__ == "__main__":
    app.run(debug=True)