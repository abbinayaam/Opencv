x = int(input("enter x"))
y = int(input("enter y"))
z = int(input("enter z"))
n = int(input("enter n"))

print([a,b,c] for a in range(0,x+1)for b in range(0,y+1)for c in range(0,z+1)if a+b+c != n )