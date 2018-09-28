import base64
text = b"admin"
print(text,"\n")

for i in range(20):
	encoded_text = base64.encodebytes(text)
	text=encoded_text
print("encoded = ",encoded_text,"\n")

for i in range(20): 
	decoded_text = base64.decodebytes(encoded_text)
	encoded_text = decoded_text
print("decoded = ",decoded_text,"\n")

print(text == decoded_text)