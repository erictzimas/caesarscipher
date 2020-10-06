#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:15:39 2020

@author: Eric Tzimas
"""

# This method encrypts the input string based on given key value.
def encryptionmode():
    cipherind=[]
    encrypted=[]
    counter=0
    s=""
    cipher2 = input()
    cc=list(cipher2)
    d="".join(cipher2.split())
    
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher=list(d)
  
   
    for i in range(0,len(cipher)):
        cipherind.append(alpha.index(cipher[i]))
   
    print("Select key")
    key=int(input())
    
    for i in range(0,len(cipherind)):
        if cipherind[i]+key<=len(alpha)-1:
            cipherind[i]=cipherind[i]+key
        else:
            cipherind[i]=cipherind[i]-len(alpha)+key
    for i in range(0, len(cipherind)):
        encrypted.append(alpha[cipherind[i]])
    for i in range(0,len(cc)):
                   if " " not in cc[i]:
                       cc[i]=encrypted[counter]
                       counter+=1
                   
    print(s.join(cc))
# This method decrypts input string based on key value.
def decryptionmode():
    print("Give encrypted text")
    cipherind=[]
    decrypted=[]
    counter=0
    s=""
    cipher2 = input()
    cc=list(cipher2)
    d="".join(cipher2.split())
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipher=list(d)
    for i in range(0,len(cipher)):
        cipherind.append(alpha.index(cipher[i]))
    print("Select key")
    key=int(input())
    
    for i in range(0,len(cipherind)):
        if cipherind[i]-key>=0:
            cipherind[i]=cipherind[i]-key
        else:
            cipherind[i]=len(alpha) + cipherind[i]-key
    for i in range(0, len(cipherind)):
        decrypted.append(alpha[cipherind[i]])
    for i in range(0,len(cc)):
                   if " " not in cc[i]:
                       cc[i]=decrypted[counter]
                       counter+=1
                   
    print(s.join(cc))
    
print("Select Mode")
st=input()
if st=='e':
    encryptionmode()
elif st=='d':
    decryptionmode()

    
    
