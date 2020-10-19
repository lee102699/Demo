import json, requests


r = requests.post('https://us-central1-poised-aleph-290508.cloudfunctions.net/testfun', json = {'name':'taipei'})
print(r.text)

