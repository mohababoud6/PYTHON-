#REPORT:    
#OVERALL APPRECIATION APP
#####GRADE SYSTEM ########

#grade= float(input("Enter student grade: \n "))

#if grade >= 85:
   # print("excellent")
#elif 85>grade>=75:
 #   print("very good") 
#elif 75>grade>= 65:
  #      print("good")
#elif 65>grade>=50:
 #           print("pass")
#elif grade<50:
 #     print("fail")

#####check number is even or odd########
#num = int (input("Enter any number to test whether it  odd  even: "))

# (num % 2) == 0:
 #   print ("The number is even" )

#else:
 #  print ("The number is odd")
###################################################################

######fizzzBuzz######
# For all number from 1 to n,
 #       if a number is divisible by 3 and 5 both, print “FizzBuzz”
  #      otherwise when the number is divisible by 3, print “Fizz”
   #     otherwise when the number is divisible by 5, print “Buzz”
    #    otherwise, write the number as a string



#for fizzbuzz in range(51):
    #if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
      #  print("fizzbuzz")
     #   continue
    #elif fizzbuzz % 3 == 0:
     #   print("fizz")
    #    continue
   # elif fizzbuzz % 5 == 0:
  #      print("buzz")
 #       continue
#    print(fizzbuzz)


##########################################################

#check string is pandolic or not
#Given a string, write a python function to check
# if it is palindrome or not. A string is said to be palindrome 
# if the reverse of the string is the same as string.
#def isPalindrome(str):
 
    # Run loop from 0 to len/2
    #for i in range(0, int(len(str)/2)):
   #     if str[i] != str[len(str)-i-1]:
  #          return False
 #   return True
 
# main function
#s = "maam"
#ans = isPalindrome(s)
 
 
#if (ans):
#    print("Yes")
#else:
#    print("No")

###############################################################

##########calculate rectangle area and perimeter####

#steps
#ask user for l and h and store them in 2 variables
#calculate perimeter and area

lenght =float(input("Enter lenght: \n"))
width =float(input("Enter width : \n"))

area= lenght * width
perimeter= 2*lenght + 2 *width

print("Rectangle area =  ")
print(area)

print("Rectangle perimeter= ")
print(perimeter)
