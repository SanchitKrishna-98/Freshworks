import threading #import threading package
from threading import*
import time
dictionary={} #using a dictionary to store data

#Create function
def create_data(key,data,time_to_live=0): 
    if key in dictionary:
        print("an error occured, this key is already present")
    else:
        if(key.isalpha()): #if the key is a character
            if data<=(16*1024*1024) and len(dictionary)<(1024*1020*1024): #condition for JSON object size less than 16Kb and file size less than 1GB
                if time_to_live==0:
                    temp=[data,time_to_live]
                else:
                    temp=[data,time.time()+time_to_live]
                if len(key)<=32: #condition for key to be string capped at 32 chars
                    dictionary[key]=temp
            else:
                print("Memory limit exceded error occured")
        else:
            print("an error occured, key must contain only alphabets and should not be numbers or special chars")


#Read function          
def read_data(key):
    if key not in dictionary:
        print("key not present, enter a valid key") 
    else:
        read_temp=dictionary[key]
        if read_temp[1]!=0:
            if time.time()<read_temp[1]: #condition to check if time_to_live is less than present time 
                string=str(key)+":"+str(read_temp[0]) #string will return in the form of JSON object
                return string
            else:
                print("error,time-to-live of",key,"has expired") 
        else:
            string=str(key)+":"+str(read_temp[0])
            return string

#Delete function
def delete_data(key):
    if key not in dictionary:
        print("error,the key is not present in dictionary") 
    else:
        delete_temp=dictionary[key]
        if delete_temp[1]!=0:
            if time.time()<delete_temp[1]: 
                del dictionary[key]
                print("key is deleted successfully")
            else:
                print("error,time-to-live of",key,"has expired") 
        else:
            del dictionary[key]
            print("key is deleted successfully")
