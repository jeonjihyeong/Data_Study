import os
import sys
import urllib.request
client_id="lWN4yY3PgIXg0Jw3JpZT"
client_secret="gTaZAzEl9w"
encText = urllib.parse.quote("한마음페스티벌")
url ="https://openapi.naver.com/v1/search/news.json?query="+encText
request=urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode=response.getcode()
if(rescode==200):
    response_body=response.read()
    encoded_text=response_body.decode('utf-8')
    print(encoded_text)
else:
    print("Error Code"+rescode)


