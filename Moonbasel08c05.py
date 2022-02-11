#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

import urllib.parse
import urllib.error
import urllib.request

url = "http://127.0.0.1:8082/selfdestruct"
for x in range(0, 100):
  response = urllib.request.urlopen(url)
  data = str(response.read())
  if 'Win:' in data:
    print(data)
    print("FOUND IT")
    break
  else:
    print("none")
    