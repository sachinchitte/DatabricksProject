number = 15
if number > 0:
  print("The number is positive")
#elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true,
# it executes that block and skips all remaining conditions.
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")

a = 200
b = 33
c=10
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
if b > a:
  pass

#The match statement selects one of many code blocks to be executed.
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")

#while loop
i = 1
while i < 6:
  #print(i)
  i += 1
#With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  #print(i) #o/p 1,2,3
  if i == 3:
    break
  i += 1

#With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  #print(i) #o/p 1,2,4,5,6

i = 1
while i < 6:
  #print(i) #o/p 1,2,3,4,5
  i += 1
else:
  print("i is no longer less than 6")

#range(start, stop, step)
x = range(6)
for n in x:
  print(n) #o/p 0,1,2,3,4,5

for x in range(2, 6):
  print(x) #o/p 2,3,4,5

