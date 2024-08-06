'''
My Module for Reed-Muller encoding and error correction programme containing all the definitions of the used function
'''

import random

# Fast Walsh Fourier Transformation function (using divide-conquor)
def fwht(list ):
    if(len(list)==2):
        list3 = []
        list3.append(list[0] + list[1])
        list3.append(list[0] - list[1])
        return list3
    list1 = fwht(list[:len(list)//2])
    list2 = fwht(list[len(list)//2 :])
    for i in range(len(list1)):
        list[i] = list1[i] + list2[i]
        list[i+len(list1)] = list1[i] - list2[i]
    return list

#Encoding function which takes a msg input and output the enconded string by calculating TT
def Reed_Muller_Encoder(msg):
    k = len(msg)
    Encoded_msg = []
    for i in range(2**(k-1)):
        x = "{0:b}".format(i)
        x = x.zfill(k-1)
        z = int(msg[0])
        for j in range(k-1):
            z = int(msg[j+1]) * int(x[j]) + z
        z = z % 2
        Encoded_msg.append(z)
    return Encoded_msg   

# This function flips the bits of the encoded msg wrt the probability
def Error_msg_generator(no_flip, Encoded_msg, n):
    list_rand = []
    count = 0
    while(count < no_flip):
        x = random.randrange((2**n)-1)
        if x not in list_rand:
            list_rand.append(x)
            count = count + 1
    print("flip position",list_rand)    ## bit flip positions(random)
    error_msg = []          ## list for storing erroneous msg after bit flips
    for i in range(len(Encoded_msg)):
        if i in list_rand:
            error_msg.append((int(Encoded_msg[i]) +1 ) % 2)
        else:
            error_msg.append(Encoded_msg[i])
    return error_msg

## Function for decoding the codeword, which takes input a list which was derived by the fwht function
## Takes the max modulous value position and check its negtivity and outputs the decoded msg
def Decoded_msg(list, n):
    list1 = list.copy()
    for i in range(len(list)):
        if(int(list[i]) < 0):
            list[i] = int(list[i]) * (-1)
    m = max(list)
    if(list1[list.index(m)] < 0):
        b = '1'
    else:
        b = '0'
    x = "{0:b}".format(list.index(m))
    x = x.zfill(n)
    x = b+x
    #print("msg : ",x)
    #print("max element is",m, "and index is", list.index(m))
    return x
    