def pattern(n):
   for i in range(n):
      for j in range(i+1):
         # printing stars
         print("*",end=" ")
      print("\r")
 
n = int(input('Enter the number of rows: '))
pattern(n)