##dump():Encryption
##Loads(): Decryption

'''
1.JSON
2. Pickle
'''
import json
import pickle
# file=open('temp.txt','a+')
# data={
#     'fullname':"sam sung",
#     'userid': 43425342,
#     'password':'******'
# }
# print(f'original Data:{data}')
# print(f'type of data:{type(data)}')

# enc_data=json.dumps(data)
# print(f"Encryted Data:{enc_data}")
# print(f"type of encryted data:{type(enc_data)}")

# dec_data=json.loads(enc_data)
# print(f"Decryted Data:{dec_data}")
# # print(f"type of decryted data:{type(dec_data)}")

file=open('temp.txt','ab+')
data={
    'fullname':"sam sung",
    'userid': 43425342,
    'password':'******'
}
print(f'original Data:{data}')
print(f'type of data:{type(data)}')

enc_data=pickle.dumps(data)
print(f"Encryted Data:{enc_data}")
print(f"type of encryted data:{type(enc_data)}")

dec_data=pickle.loads(enc_data)
print(f"Decryted Data:{dec_data}")
print(f"type of decryted data:{type(dec_data)}")