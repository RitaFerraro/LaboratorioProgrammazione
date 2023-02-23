#Creare un iteratore che genera i primi n numeri primi (n e' un prametro passato al costruttore)

class PrimeNumbers:

    def __init__(self, n):
        self.n =n
        self.a=2
    
    def primo(self, x ):
        self.x=x 
        self.p =1
        for i in range(2, x+1):
            if x%i==0 and x!=2 and i!=x:
                #print(x)
                #print(0)
                self.p=0
                return self.p
        return self.p    
    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.n:
            raise StopIteration
        else:
            while self.primo(self.a) ==0:
                self.a +=1
            if self.primo(self.a)==1:
                self.a +=1
                if self.a <=self.n +1:
                    return self.a -1
                else:
                    raise StopIteration

myS =PrimeNumbers(100)
for s in myS:
    print(s)
