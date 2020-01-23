import sys

# read input format 
def read_input(filename):
  f= open(filename, "r").readlines()
  m=int(f[0].split()[0])
  s=[int(k) for k in f[1].split()]
  return s,m

# the goal is to order as many pizza slices as possible,
# but not more than the maximum number M
def more_pizzas(s,m):
  S_pizzas=0
  i=len(s)-1
  pizzas=[]
  while(i >= 0 and S_pizzas < m ):
    if(S_pizzas + s[i] <= m):
      pizzas.append(i)
      S_pizzas += s[i]
    i= i-1
  pizzas.reverse()
  return len(pizzas), pizzas

# wite output format
def write_output(kpizzas,k):
    f = open("write_output.txt", "w")
    print()
    f.write(str(k)+'\n')
    f.write(kpizzas) 
    f.close()
#print(sys.argv[1])
if sys.argv.__len__() == 2:
    s,m = read_input(sys.argv[1])
else:
    s,m = read_input("c_medium.in")

k, kpizzas = more_pizzas(s,m)
ordred_pizzas =" ".join(str(x) for x in kpizzas)
write_output(ordred_pizzas,k)