#
# Connect to the  server at 'localhost', 10000 send any data,
# the server will respond with the required word codes
# You will find a passage of text in the file backdoor.txt write a script
# which will use that text to build a message using the received word codes.
# Each word code is sent on a new line and contains
# paragraph_number, line_number, word_number
# Send the expected words back to the server to retrieve the flag.
# The server expects all the words in a single transmission.
# The words should have punctuation stripped from them.
# And the words should be separated by newline characters (\\n)
#

import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10000))
s.send(bytes("hi", "utf8"))
data = s.recv(1024)
#print(data)
a, b, c, d, e, f, g = str(data).split("\\n")

#Throw away g, is empty
a = a.replace("b'", "")
a = a.split(",")
b = b.split(",")
c = c.split(",")
d = d.split(",")
e = e.split(",")
f = f.split(",")

firstpg = int(a[0])
secondpg = int(b[0])
thirdpg = int(c[0])
fourthpg = int(d[0])
fifthpg = int(e[0])
sixthpg = int(f[0])

firstline = int(a[1]) # This will print the second line in the array
secondline = int(b[1])
thirdline = int(c[1]) # 
fourthline = int(d[1])
fifthline = int(e[1])
sixthline = int(f[1])

firstword = int(a[2])
firstword = firstword-1
secondword = int(b[2])
secondword = secondword-1
thirdword = int(c[2])
thirdword = thirdword-1
fourthword = int(d[2])
fourthword = fourthword-1
fifthword = int(e[2])
fifthword = fifthword-1
sixthword = int(f[2])
sixthword = sixthword-1


print(a)
print(firstpg)
print(firstline)
print(firstword)
BOOK="./backdoor.txt"

with open(BOOK, "r") as book:
  book2 = book.read().split("\n\n")
  firstpg = (book2[firstpg-1])
  secondpg = (book2[secondpg-1])
  thirdpg = (book2[thirdpg-1])
  fourthpg = (book2[fourthpg-1])
  fifthpg = (book2[fifthpg-1])
  sixthpg = (book2[sixthpg-1])
  #print(firstpg + "\n")
  #print(secondpg + "\n")
  firstlinesplit = firstpg.split("\n")
  print(firstlinesplit)
  secondlinesplit = secondpg.split("\n")
  thirdlinesplit = thirdpg.split("\n")
  fourthlinesplit = fourthpg.split("\n")
  fifthlinesplit = fifthpg.split("\n")
  sixthlinesplit = sixthpg.split("\n")
  print(firstline)
  firstline = firstlinesplit[firstline-1] # this should print the original value (3) - 1 to get the third value of the array
  secondline = secondlinesplit[secondline-1]
  thirdline = thirdlinesplit[thirdline-1]
  fourthline = fourthlinesplit[fourthline-1]
  fifthline = fifthlinesplit[fifthline-1]
  sixthline = sixthlinesplit[sixthline-1]
  print(firstline)
  print(secondline)
  print(thirdline)
  print(fourthline)
  print(fifthline)
  print(sixthline)
  firstfinalword = firstline.split()
  secondfinalword = secondline.split()
  thirdfinalword = thirdline.split()
  forthfinalword = fourthline.split()
  fifthfinalword = fifthline.split()
  sixthfinalword = sixthline.split()
  print(firstfinalword)
  finalword1 = firstfinalword[firstword]
  finalword2 = secondfinalword[secondword]
  finalword3 = thirdfinalword[thirdword]
  finalword4 = forthfinalword[fourthword]
  finalword5 = fifthfinalword[fifthword]
  finalword6 = sixthfinalword[sixthword]
  
  FINALLY = finalword1 + " " + finalword2 + " " + finalword3 + " " +finalword4 + " " + finalword5 + " " + finalword6
  print(FINALLY)
  FINALLY = FINALLY.replace('"', "")
  FINALLY = FINALLY.replace(".", "")
  FINALLY = FINALLY.replace(",", "")
  FINALLY = FINALLY.replace("?", "")
  FINALLY = FINALLY.replace(" ", "\n ")
  print(FINALLY)
  s.send(bytes(FINALLY, "utf8"))
  print(s.recv(1024))