#Multiplications, arithmetique des corps fini

def CF_Mult2(operation):   #Arithmétique des corps fini, multiplication par 2
    if (operation & 0x80):
        return ((operation << 1) ^ 0x1B) & 0xFF
    else:
        return (operation << 1)&0xFF
    
def CF_Mult3(operation):   #Multiplication par 3 équivaut à x×2+x
    return (CF_Mult2(operation) ^ operation)&0xFF

def CF_Mult9(operation):
    return (CF_Mult2(CF_Mult2(CF_Mult2(operation))) ^ operation)&0xFF    #Multiplication par 9 équivaut à (((x×2)×2)×2)+x

def CF_Mult11(operation):
    return (CF_Mult2(CF_Mult2(CF_Mult2(operation)) ^ operation)^operation)&0xFF  #Multiplication par 11 équivaut à((((x×2)×2)+x)×2)+x

def CF_Mult13(operation):
    return (CF_Mult2(CF_Mult2(CF_Mult2(operation)^operation))^operation)&0xFF  #Multiplication par 13 équivaut à((((x×2)+x)×2)×2)+x

def CF_Mult14(operation):
    return (CF_Mult2(CF_Mult2(CF_Mult2(operation)^operation)^operation))&0xFF         #Multiplication par 14 équivaut à((((x×2)+x)×2)+x)×2  
