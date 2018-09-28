import requests

url = 'http://webhacking.kr/challenge/codeing/code5.html?hit=:)'
cookies = {'PHPSESSID':'215218d30030ff1ef648d452c42f3344'}

for i in range(101):
	respone = requests.get(url=url,cookies=cookies)
	print(i)