from urllib.request import urlopen
import os.system
url = "https://bulldoghax.com/secret/spinner"
page = urlopen(url)
html_bytes=page.read()
html=html_bytes.decode("utf-8")
print(html)
number_index = html.find('<div class="number">')
print(number_index)
start_index=number_index + len('class="number"')
print(start_index)
end_index=html.find("</div>")
print(end_index)
htmlnumber=html[number_index:end_index]
print(htmlnumber)
number = htmlnumber.replace('div class="number">', " ").replace("<", " ").replace(" ", "")
print(htmlnumber)
print(number)

os.system(f"curl -b 'timelock={number}'")
