'''
1. Average
Outline:
There are five trees in Jack's front yard. 
He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper.
Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
'''
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 96
tree5 = 11
average = (tree1 + tree2 + tree3 + tree4 + tree5)/5
print("The average of all the 5 trees is:",average)

'''
Count the notes
Outline:
Write a program to calculate the number of notes in the given amount?
'''
amount = int(input("Enter the amount for withdraw: "))
#note1 = 100
notes_amount1 = ((amount%100)//50)//10
print("Notes of 10 rupees are:",notes_amount1)

notes_amount2 = (amount%100)//50
print("Notes of 50 rupees are:",notes_amount2)

notes_amount3 = amount//100
print("Notes of 100 rupees are:",notes_amount3)

'''
3. Percentage calculation
Outline:
Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?
'''
m = 40
s = 70
h = 50
e = 60
total = (40 + 70 + 50 + 60)/4
print("The average marks is:",total)