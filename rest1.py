import requests
import json
url='https://api.speedcurve.com/v1/urls?days=1'
key='cn685aw5tj0i475zdzOsbmtpslry82'
password ='Any_password'
res=requests.get(url,auth=(key,password))
d=(res.json())
print(d)
