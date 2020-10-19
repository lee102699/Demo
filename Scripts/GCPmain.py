from flask import Flask , request
import requests, json
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
def weatherAPI(CITY):
   # base URL
   BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
   URL = BASE_URL + "q=" + CITY + "&appid=" + "5c23d8f44b6a520211b8539b8512bdaa" + "&units=metric"
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      return print(data)
   else:
      # showing the error message
      print("Error in the HTTP request")
weatherAPI("taipei")


# if __name__ == '__main__':
#    app.run(port=5000, host='0.0.0.0')