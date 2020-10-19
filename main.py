import json, requests
from flask import Flask, render_template, flash, request, redirect

app = Flask(__name__)
@app.route('/')
def getdata():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():

    SearchCity = request.form.get('city')
    my_params = {'name': SearchCity}
    res = requests.post('https://us-central1-poised-aleph-290508.cloudfunctions.net/testfun', json = my_params)
    data = json.loads(res.text)

    city = data['city']['name']
    weatherTitle = data['list'][0]['weather'][0]['description']
    temperature = str(data['list'][0]['main']['temp'])
    result = SearchCity+" weather: "+weatherTitle+" \n Temperature: "+temperature+"°C"
    # return result
    return render_template('index.html', message = result)


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')