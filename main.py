class InvalidName(Exception):  #Error code
    def __init__(self,message):
        self.message=message
def vlistChar(x): #making a list of all characters in the name.
    l=[]
    for i in x:
        if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90 ):
            l.append(i.lower())
        elif(i==' '):
            pass
        else:
            raise InvalidName("Please enter a valid name.")
    return l
def removeCount(n,y): #the count value which we want to remove from dict.
    r = y % n
    if r == 0:
        return n
    else:
        return r


try:
    # main code
    print()
    print("Flames Calculator".center(50))
    first_name = vlistChar(list(input("\nEnter First Person name: ")))
    second_name = vlistChar(list(input("Enter Second Person name: ")))
    if not first_name or not second_name:
        raise InvalidName("Please enter a valid name.")
    
except InvalidName as e:
    print(f"InvalidName Error: {e}")

else:
    # print(first_name,second_name)
    # find the number of character count : flames_count 
    count = [0]*256
    for i in first_name:
        count[ord(i)] += 1
    # print(sum(count))
    for i in second_name:
        count[ord(i)] -= 1
    flames_count = 0
    for i in count:
        flames_count += abs(i)
    # print(flames_count)
    inital_Flames_list={1:'f',2:'l',3:'a',4:'m',5:'e',6:'s'}

    while(len(inital_Flames_list)!=1):
       
        remCnt = removeCount(len(inital_Flames_list),flames_count)
        # print(remCnt)
        new_list=dict()
        # inital_Flames_list.pop(remCnt)
        k=1
        for i in range(remCnt+1,len(inital_Flames_list)+1):
            new_list[k]=inital_Flames_list[i]
            k+=1
        for j in range(1,remCnt):
            new_list[k]=inital_Flames_list[j]
            k+=1
        inital_Flames_list=new_list
        # print(inital_Flames_list)

    full_form_dict={'f':'Friends','l':'Lovers','a':'Affection','m':'Marriage','e':'Enemies','s':'Sister'}  
    x=list(inital_Flames_list.values())
                
    print("\nResult : {}\n".format(full_form_dict[x[0]]))

