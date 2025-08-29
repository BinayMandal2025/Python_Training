#Create an empty list to store scores.
myList = []

#Append the scores: 85, 90, 78, 92, 88
myList.extend([85, 90, 78, 92, 88])
print("Appended list is:", myList)

#Insert the score 80 at index 5
myList.insert(5, 80)
print("After insert the score 80 at index 5 list is:", myList)

#Remove the score 92 from the list
myList.remove(92)
print("After remove 92 list is:", myList)

#Sort the scores in ascending order
myList.sort()
print("After sort list is:", myList)

#Reverse the list
myList.reverse()
print("After reverse list is:", myList)

#Find and print the maximum and minimum score
print("max score in the list:", max(myList)) 
print("min score in the list:", min(myList)) 

#Check if 90 is in the list
print("Number 90 appears in the list:", myList.count(90)) 

#Print the total number of scores
print("Total number in the list:", len(myList)) 

#Slice and print the first three scores
print("First 3 scores in the list", myList[:3])

#find the last element from the list
print("Last element in the list", myList[-1])

#replace the score with new score on the index 2
myList[2] = 100
print("list", myList)

#create a new copied list also
myList_copy = myList.copy()
print("Copy list is:", myList)
