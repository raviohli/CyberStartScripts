#
# Tweet bot API listening at http://127.0.0.1:8082.
# GET / returns basic info about api. POST / with x-api-key:tweetbotkeyv1
# and data with user tweetbotuser and status-update of alientest
#


import urllib
import urllib.request
import urllib.parse
request = urllib.request.Request("http://127.0.0.1:8082")
response = urllib.request.urlopen(request)
html = response.read()



data = urllib.parse.urlencode({'user':'tweetbotuser','status-update':'alientest'})
data = data.encode("ascii")
request = urllib.request.Request("http://127.0.0.1:8082", headers={'x-api-key':'tweetbotkeyv1'}, data=data)
response = urllib.request.urlopen(request)
print(response.read())