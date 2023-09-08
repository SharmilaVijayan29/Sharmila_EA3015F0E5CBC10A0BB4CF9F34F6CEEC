def face_rec(n):
  if n==0 or n==1:
    return 1 
  else:
    return n*face_rec(n-1)
number=int(input("Enter a value:"))
res=face_rec(number)
print("the number of factorial of{}is{}.".format(number,res))