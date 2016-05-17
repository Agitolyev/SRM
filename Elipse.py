def euclidExt(a, b):

  assert a != 0 or b != 0
  a0, a1, b0, b1 = 1, 0, 0, 1
  while b != 0:
    q, r = divmod(a, b)
    a, b = b, r
    a0, a1, b0, b1 = b0, b1, a0 - q*b0, a1 - q*b1
  return (a, a0, a1)

def sum(x1,y1,x2,y2,m):

    a=(y1-y2)*euclidExt((x1-x2),m)[1] % m
    print a
    x3=(pow(a,2,m)-x1-x2) % m
    y3=-y1+a*(x1-x3) % m
    return x3,y3

def double(x,y,a,m):
    q= (3*pow(x,2,m)+a)*euclidExt(2*y,m)[1] % m
    print q
    x3= pow(q,2,m)-2*x % m
    y3= -y+q*(x-x3) % m
    return x3,y3

def sepNum(x):
    raw=[]
    while(x!=0):
        if(x%2 == 1):
          raw.append(1)
          x-=1
        else:
          raw.append(2)
          x=x/2
    raw.pop(-1)
    return raw



print double(4,1,5,11)