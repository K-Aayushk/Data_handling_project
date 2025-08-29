# Open a csv file and able to perform simple task like add, mean,median,mul

import pandas as pd
import numpy as np


def read():
    file_name=input("Enter the file name with extension: ")
    data=pd.read_csv(file_name,encoding="latin1",index_col=0)
    return data

file=read()
print(file.columns)
col=input("Enter the column name: ")
arr=np.array(file.get(col))

def check_data(arr):
    try:
        for i in arr:
            float(i)
            return "yes"
    except(ValueError):
        return "no"


def tasks(value):
    yes_dict={"Add":1,"Mean":2,"Median":3}
    no_dict={"Add to file":1,"Append the file":2}
    if(value.lower()=="yes"):
        print(yes_dict)
        return "yes"
    elif(value.lower()=="no"):
        print(no_dict)
        return "no"

def perform_digit(task,arr):
    inp=input("Enter the task you want to perform: ")
    if(task.lower()=="yes"):
        if(int(inp)==1):
            sum=np.sum(np.ceil(arr).astype(int))
            print(sum)
        elif(int(inp)==2):
            mn=np.mean(arr.astype(int))
            print(mn)
        elif(int(inp)==3):
            md=np.median(arr.astype(int))
            print(md)
    elif(task.lower()=="no"):
        f_name=input("Enter the file name: ")
        if(int(inp)==1):
            with open(f_name,"w") as f:
                for i  in arr:
                    f.write(str(i)+"\n")
        elif(int(inp)==2):
            with open(f_name,"a") as f:
                for i in arr:
                    f.write(str(arr)+"\n")
                
            
            
        
        
perform_digit(tasks(check_data(arr)),arr)



