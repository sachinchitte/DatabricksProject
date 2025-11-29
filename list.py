#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

alpha = [1, 2, 3, 4, 5, 6]
#alpha[3] = 2 #update

#insert at particular index
alpha.insert(1,100)
#print(alpha) #print particular index value
#o/p [1, 100, 2, 3, 4, 5, 6]

#append (add item to the end of the list)
alpha.append(200)
#print(alpha)

#extend ( to append elements from other list)
alpha2 =[7,8,9,10]
alpha.extend(alpha2)
#print(alpha)
#[1, 100, 2, 3, 4, 5, 6, 200, 7, 8, 9, 10]

#Remove (remove specific value from list
alpha.remove(100)
#print(alpha)
#o/p [1, 2, 3, 4, 5, 6, 200, 7, 8, 9, 10]

#pop removes the last item if we don't specify the index
alpha2.pop()
#print(alpha2)
#[7, 8, 9]
alpha2.pop(0)
#print(alpha2)
#[8, 9]

#clear() empties the list
alpha2.clear()
#print(alpha2)
#o/p []


#LOOP List
beta2=[5,6,7,8,9,10]
#for i in range(len(beta2)):
    #print(beta2[i])
i=0
while i<len(beta2):
    print(beta2[i],i)
    i+=1  #i--
#op
#5 0
#6 1
#7 2
#8 3
#9 4
#10 5

#reverse the list
beta2.reverse()
print(beta2)

#sort