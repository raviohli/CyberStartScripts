#
# Browse the contents of these alien directories found in /tmp/aliendir to find
# the flag
#
#
import os

for x in range(1, 200):
  try:
    print(os.listdir(f"/tmp/aliendir/folder-{x}"))
  except:
    continue