#统计str中substr出现的次数
def couter_substr_in_str(str,substr):
    counter_num=0
    """
   intuitive method
    """
    for i in range(len(str)-1):
        if str[i:i+len(substr)]==substr:
            counter_num+=1
    return counter_num

ciphertext="lmqetxyeagtxctuiewnctxlzewuaispzyvapewlmgqwyaxftcjmsqcadagtxlmdxnxsnpjqsyvapriqsmhnocvaxfv"
counter=dict()
for i in range(len(ciphertext)-1):
    #couter=[]
    counter[ciphertext[i:i+2]]=couter_substr_in_str(ciphertext,ciphertext[i:i+2])
counter_dict=sorted(counter.items(),key=lambda d:d[1],reverse=True)
print(counter_dict)


