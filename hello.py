def fact(t):
    if t==0:
      return 1
    else:
      f=1
      for i in range(1,t+1):
          f *= i
      return f
         


print(fact(5))
