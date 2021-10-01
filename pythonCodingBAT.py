a=5
b=6
sum = a + b
print(sum)



def diff21(n):
    if n<= 21:
        return 21 - n
    else: return(n - 21) * 2


def maskes10(a,b):
    return(a == 10)
    return(b == 10)
    return(a + b == 10)

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
