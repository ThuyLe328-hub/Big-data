def is_prime(n):
    if n<=1:
        return False
    else: 
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False
    return True
def demtanso(input):
    message= input.replace("\n"," ").replace("'ll"," will").replace("It's","It is").replace("I'm","I am")
    preq = {}
    for word in input.split():
        if word in preq:
            preq[word] += 1
        else:
            preq[word]= 1

    return preq 
print("welcome to my module")