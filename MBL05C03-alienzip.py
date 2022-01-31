#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

from zipfile import ZipFile
import os


path = "/tmp/"

def test(x):
  for y in range(0, 1001):
    try:
      z.extract("/tmp", pwd = bytes(x, "utf-8"))
      print(f"password found! : {x}")
    except:
      print(" ")
      

with ZipFile("/tmp/alien-zip-2092.zip", "r") as z:
  for x in range(0, 1000):
    try:
      z.extractall("/tmp/", pwd = bytes(str(x), "UTF-8"))
      print(f"pass found : {x}")
      break
      
    except:
      continue
      
file_read = open("/tmp")
file_read = file_read.read()
print(file_read)
            