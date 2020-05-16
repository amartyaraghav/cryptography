import numpy as np
public = input("Plain Text: ")
ciparr =[]
cipher =""
key = input("Key of length 9: ")
result =[[0],[0],[0]]
#Key Matrix
arr = np.zeros([3,3],dtype= int)
pubarr = np.zeros([3,1],dtype=int)
k= 0
for i in range(3):
    for j in range(3):
        arr[i][j] = (ord(key[k])-97)%26
        k+= 1
print(arr)
#Encryption
for i in range(0,len(public),3):
    if(i<len(public)-2):
        pubarr = np.array([[(ord(public[i])-97)%26],[(ord(public[i+1])-97)%26],[(ord(public[i+2])-97)%26]])
    elif(i<len(public)-1):
        pubarr = np.array([[(ord(public[i])-97)%26],[(ord(public[i+1])-97)%26],[(ord("x")-97)%26]])
    else:
        pubarr = np.array([[(ord(public[i])-97)%26],[(ord("x")-97)%26],[(ord("x")-97)%26]])
        
    ciparr = np.dot(arr,pubarr)
    #print(pubarr)
    for j in range(0,3,1):
        ciparr[j][0]=(ciparr[j][0]%26)+97
        cipher +=chr(ciparr[j]) 
print(cipher)

#Decryption
arrinv = np.zeros([3,3],dtype= int)
#arr1 =[[2,4,5],[9,2,1],[3,17,7]]
dinv=0
det = int(np.linalg.det(arr).round(2))
print(det)
for i in range(0,26):
    #print((i*det)%26)
    if (i*det)%26==1:
     #   print(i)
        dinv=i
arrinv = np.linalg.inv(arr)
arrinv = (det*arrinv)%26 #Adjoint
arrinv = (dinv*arrinv)%26
decipher=""

#print(det)
print(arrinv)
decarr =[]
#print(cipher)
#print((ord(cipher[0])-97)%26)
for k in range(0,len(public),3):
    decarr = np.array([[(ord(cipher[k])-97)%26],[(ord(cipher[k+1])-97)%26],[(ord(cipher[k+2])-97)%26]])    
 #   print(decarr)
    decarr = np.dot(arrinv,decarr)%26
    print(decarr)
    for i in decarr:
        z = chr(i+97)
        print(z)
        decipher+= z
    
print(decipher)
