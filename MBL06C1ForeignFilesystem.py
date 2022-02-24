#
# Browse the contents of these alien directories found in /tmp/aliendir to find
# the flag
#

import os
for x in range(0, 200):
  print(os.listdir(f"/tmp/aliendir/folder-{x}"))
