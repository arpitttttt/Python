def factorial_recursive(n):
     if n==1 or n==0:
      return 1
     return n*factorial_recursive(n-1)
     f=factorial_recursive(0)
     print(f)
#N = input
#if N % 2 == 0:
 #   print( "Weird")
#else:
 #   if N >= 2 and N <= 5:
  #      print ("Not Weird")
   # elif N >= 6 and N <= 20:
    #    print ("Weird")
    #elif N > 20:
     #   print ("Not Weird")
