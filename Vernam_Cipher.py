############################## VERNAM CIPHER #######################################
# Author: Debjeet Banerjee      | encodes and decodes the message given to the     #
# Topic: Vernam Cipher          | computer. It automatically generates a key       #
# Version: 1.0.0                | whose length is equal to the length of the       #
#                               | message provided, but will ask a key from the    # 
#                               | user while decoding.                             #
####################################################################################


#Imports
import string
import random
import pyfiglet

#Banner 
#print('__     _______ ____  _   _    _    __  __     ____ ___ ____  _   _ _____ ____')
#print('\ \   / / ____|  _ \| \ | |  / \  |  \/  |   / ___|_ _|  _ \| | | | ____|  _ \\')
#print(' \ \ / /|  _| | |_) |  \| | / _ \ | |\/| |  | |    | || |_) | |_| |  _| | |_) |')
#print('  \ V / | |___|  _ <| |\  |/ ___ \| |  | |  | |___ | ||  __/|  _  | |___|  _ <')
#print('   \_/  |_____|_| \_\_| \_/_/   \_\_|  |_|   \____|___|_|   |_| |_|_____|_| \_\\')
#print('                                                                               ')
#print('                                                                                 ')

banner = pyfiglet.figlet_format('VERNAM  CIPHER')
print(banner)

print('***Enter everything in small***')
choice = str(input('Choose your cryptography format (encode/decode): '))
print('')

dict = {'A':0,0:'A','B':1,1:'B','C':2,2:'C','D':3,3:'D','E':4,4:'E','F':5,5:'F','G':6,6:'G','H':7,7:'H','I':8,8:'I','J':9,9:'J','K':10,10:'K','L':11,11:'L','M':12,12:'M','N':13,13:'N','O':14,14:'O','P':15,15:'P','Q':16,16:'Q','R':17,17:'R','S':18,18:'S','T':19,19:'T','U':20,20:'U','V':21,21:'V','W':22,22:'W','X':23,23:'X','Y':24,24:'Y','Z':25,25:'Z','a':0,0:'a','b':1,1:'b','c':2,2:'c','d':3,3:'d','e':4,4:'e','f':5,5:'f','g':6,6:'g','h':7,7:'h','i':8,8:'i','j':9,9:'j','k':10,10:'k','l':11,11:'l','m':12,12:'m','n':13,13:'n','o':14,14:'o','p':15,15:'p','q':16,16:'q','r':17,17:'r','s':18,18:'s','t':19,19:'t','u':20,20:'u','v':21,21:'v','w':22,22:'w','x':23,23:'x','y':24,24:'y','z':25,25:'z',' ':26,26:' '}

if 'encode' in choice:
    msg = str(input('[+]Message: '))
    msg_lst = []
    msg_num_lst = []
    for i in range(len(msg)):
        msg_lst.append(msg[i])
    for x in range(len(msg_lst)):
        msg_num_lst.append(dict.get(msg_lst[x]))
    key_lst = []
    def generate_key(length):
        letters = string.ascii_letters
        for j in range(length):
            key_lst.append(random.choice(letters))
    generate_key(len(msg))
    res_key = ''.join(key for key in key_lst)
    print('[+]Key: ',res_key)
    key_num_lst = []
    for key in range(len(key_lst)):
        key_num_lst.append(dict.get(key_lst[key]))
    cipher_num_lst = []
    for num in range(len(msg_num_lst)):
        sum_of_lst = msg_num_lst[num] + key_num_lst[num]
        if sum_of_lst>26:
            sum_of_lst = sum_of_lst-27
            cipher_num_lst.append(sum_of_lst)
        else:
            cipher_num_lst.append(sum_of_lst)
    cipher_lst = []
    for cipher_num in range(len(cipher_num_lst)):
        cipher_lst.append(dict.get(cipher_num_lst[cipher_num]))
    res_cipher = ''.join(cipher for cipher in cipher_lst)
    print('[+]Cipher text: ',res_cipher)
    input('press enter to exit....')

elif 'decode' in choice:
    cipher_txt = str(input('[+]Cipher Text: '))
    key_txt = str(input('[+]Key: '))

    cipher_txt_lst = []
    key_txt_lst = []
    for a in range(len(cipher_txt)):
        cipher_txt_lst.append(cipher_txt[a])
    for b in range(len(key_txt)):
        key_txt_lst.append(key_txt[b])
    cipher_txt_num_lst = []
    key_txt_num_lst = []
    for c in range(len(cipher_txt_lst)):
        cipher_txt_num_lst.append(dict.get(cipher_txt_lst[c]))
    for d in range(len(key_txt_lst)):
        key_txt_num_lst.append(dict.get(key_txt_lst[d]))
    plain_txt_num_lst = []
    plain_txt_lst = []
    for e in range(len(cipher_txt_num_lst)):
        sub_of_lst = cipher_txt_num_lst[e] - key_txt_num_lst[e]
        if sub_of_lst<0:
            sub_of_lst = sub_of_lst + 27
            plain_txt_num_lst.append(sub_of_lst)
        else:
            plain_txt_num_lst.append(sub_of_lst)
    for f in range(len(plain_txt_num_lst)):
        plain_txt_lst.append(dict.get(plain_txt_num_lst[f]))
    res_plain = ''.join(plain_txt for plain_txt in plain_txt_lst)
    print('[+]Message: ',res_plain)
    input('press enter to exit....')
else:
    print('[-]Exception raised due to choice of invalid format')
