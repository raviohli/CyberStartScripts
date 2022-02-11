#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send GET_KEY to download a string.
# The string is compressed with a common algorithm found in many
# websites. Uncompress the string and print it to get the flag.
#
import socket
import gzip
import zlib
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 10000))
s.send(bytes("GET_KEY", "UTF8"))
data = s.recv(1024)
decompressed_data = zlib.decompress(data, 16+zlib.MAX_WBITS)
print(decompressed_data)
