class Base:
    def solve(self,n):
        sign ='-' if n<0 else ''        
        n=abs(n)
        if n<3:
            return str(n)
        a = ''
        while n!=0:
            a = str(n%3)+a
            n = n//3
        return sign+a
b=Base()    
print(b.solve(10))