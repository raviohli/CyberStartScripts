#
# Connect over TCP to the following server 'localhost', 10000
# Initiate communication with GET to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

import socket

symbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 10000))
s.send(bytes("GET", "utf8"))
data = s.recv(1024)
data = str(data)
data = data.replace("b'Return the below codes decrypted. Each sentence should be split with a newline", "")
data = data.replace("'", "")
a, b, c, d, e = data.split("\\n")
#print(b)
#print("")
#print(c)
#print("")
#print(d)
def crack(x):
  for shiftnum in range(1, 26):
    #CHANGING AMOUNT OF SHIFT
    test = ""
    for symbol in x:
      unicodenum = ord(symbol)
      if unicodenum == 32:
        #SHIFTING THE WORDS
        test = test + " "
      else:
        pass
      unicodenumshifted = unicodenum + shiftnum
      if unicodenumshifted > 90:
        unicodenumshifted = unicodenumshifted - 26
        charactershifted = chr(unicodenumshifted)
        test = test + charactershifted
      elif unicodenumshifted in range(65, 90):
        charactershifted = chr(unicodenumshifted)
        test = test + charactershifted
    if "AND" in test:
      return test
    if "THE" in test:
      return test
    if "SAID" in test:
      return test
    if "GENIE" in test:
      return test
    if "WHAT" in test:
      return test
    if "MASTER" in test:
      return test
    if "ALADDIN" in test:
      return test
    if "LEAVES" in test:
      return test
    if "SILVER" in test:
      return test
    if "INSTANT" in test:
      return test
    if "EARTH" in test:
      return test

      
print(b)
print(c)
print(d)
      
        
        
bcracked = crack(b)
ccracked = crack(c)
dcracked = crack(d)
bcracked = bcracked+"\n"
ccracked = ccracked+"\n"
dcracked = dcracked+"\n"
s.send(bytes(bcracked, "utf8"))
s.send(bytes(ccracked, "utf8"))
s.send(bytes(dcracked, "utf8"))
print(s.recv(1024))
