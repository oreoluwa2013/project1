n = int(input("Enter a number: "))
temp = n
sum = 0

l = len(str(n))
while(l):
 x = int(temp%10)
 sum += x**3
 if sum == n:
  print("Armstrong Number")
 else:
  print("Not an Armstrong Number")