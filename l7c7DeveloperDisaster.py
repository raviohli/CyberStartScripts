import os
for x in range(0, 100):
    os.system(f"curl -d 'UserID={x}' https://slowlaneshipping.com/latest")

