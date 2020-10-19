import json, requests

def serachWeather():
    res = requests.get('https://us-central1-poised-aleph-290508.cloudfunctions.net/testfun')
    data = json.loads(res.text)

    city = data['city']['name']
    weatherTitle = data['list'][0]['weather'][0]['description']
    temperature = str(data['list'][0]['main']['temp'])

    return " weather is "+weatherTitle+" Temperature is "+temperature+"°C"

serachWeather()
