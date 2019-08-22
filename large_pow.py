# To find large power with short time complexicity.
 
MOD = 1000000007; 

def powerLL(x, n): 
  
    result = 1; 
    while (n):  
        if (n&1):

            result = result * x % MOD;
        
        n = int(n / 2)
        
        x = x * x % MOD;
        
    return result;
 
print(powerLL(2,10000000000000000))

#For dynamic variable
#x,y=map(int,input().split())
#print(powerLL(x,y))

 
      
