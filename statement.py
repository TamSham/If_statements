#PART 1)  SIMPLE IF STATEMENTS
print("Whats your name? ")
name=input()
print("How old are you?")
age=int(input())
if (0<=age<=16):
  print("Please stay at home")
elif (16<=age<=17):
  print("You can drive and that is all")
elif (18<=age<=20):
  print("You can drive and vote")
elif (age>=21):
  print("You can drive,vote and gamble")
else:
  print("this is not an age")
print()
print()

#PART 2) MORE WITH IF STATEMENTS
print("Please enter four numbers? ")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a>=b and a>=c and a>=d):
  largest=a
elif (b>=a and b>=c and b>=d):
  largest=b
elif (c>=a and c>=b and c>=d):
  largest=c
else:
  largest=d
print("The largest number is: ", largest)
print()
print()

#PART 3) PYTHON
print("How many packages you want? ")
qty=int(input())
price=99
total=qty*price
if (1<=qty<=9):
  total=total
elif (10<=qty<=19):
  total=total*0.2
elif (20<=qty<=49):
  total=total*0.3
elif (50<=qty<=99):
  total=total*0.4
elif (qty<=0):
  total=0
else:
  total=total*0.5
print("These packages cost you: $"+str(round(total,2)))
print()
print()
