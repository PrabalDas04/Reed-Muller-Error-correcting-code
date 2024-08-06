###########################################################################
'''
Programme for Reed-Muller Encoding and Error Correction Scheme
Author : Prabal Das, CrS 2nd Sem, ISI
Date : 29.03.2024
'''
###########################################################################
import My_Module

## Driver code
if __name__ == "__main__":
    ############ Message encoding part ##############
    msg = input("Enter the message : ")
    n = len(msg) - 1
    Encoded_msg = []
    Encoded_msg = My_Module.Reed_Muller_Encoder(msg)
    print("msg : ",msg,"Encoded msg : ",Encoded_msg)

    ############# Message Error part ################
    p = float(input("Enter the probability of bit flip : "))
    no_flip = int((2**n) * p)
    print("no_flip",no_flip)

    if(no_flip <= (2**(n-2))-1):
        error_msg = []
        error_msg = My_Module.Error_msg_generator(no_flip, Encoded_msg, n)
        print("Error msg",error_msg)

    ############## Decoding part of emcoded message ############
        msg_mod = []
        for i in range(len(error_msg)):
            msg_mod.append((-1)**(error_msg[i]))
        
        list = My_Module.fwht(msg_mod)
        #print("transform list ",list)
        x = My_Module.Decoded_msg(list, n)
        print("Decoded msg :",x)
    else:
        print("Error : No of bit flip exceeds.")