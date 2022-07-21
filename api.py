import json
from flask import Flask, jsonify, request

color = {"012245":"red"}

# creating the instance of our flask application
app = Flask(__name__)


@app.route('/color',methods = ['GET', 'POST'])
#@cross_origin(maxAge = 3600) #web auth
def downloadRoute0(): #change number for every new route!
    global color
    if(request.method == 'GET'):
        color_key = request.args.get('key')
        if(color.has_key(color_key)):
         return jsonify({"color" : color[color_key]}) #returns color from app with code
        else:
            return jsonify({"color":"null"})

    elif(request.method == 'POST'):
        color_key = request.args.get('key')
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        color[color_key] = request_data['color']
        return ' '


if __name__ == "__main__":
    app.run(debug=True)