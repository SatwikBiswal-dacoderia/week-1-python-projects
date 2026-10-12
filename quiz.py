print("Welcome to the quiz !!!")
print("The quiz contains of 5 questions. \n The user will be rewarded +1 for right answer and -0.25 for every wrong answer")
name=input("Enter your name : ")

marks=0
right=0
wrong=0

print("Q1. What is 5+7 ? \n a.4\nb.5\nc.12\nd.NOTA")
c1=input("Enter your choice : ")
if c1 in "cC":
    marks+=1
    right+=1
else:
    marks=marks-0.25
    wrong+=1

print("Q2. What is the color of the apple ?\na.red\nb.yellow\nc.black\nd.orange")
c2=input("Enter your choice : ")
if c2 in "aA":
    marks+=1
    right+=1
else:
    marks=marks-0.25
    wrong+=1

print("Q3. What is 14/7 ?\na.1\nb.2\nc.3\nd.4")
c3=input("Enter your choice : ")
if c3 in "bB":
    marks+=1
    right+=1
else:
    marks=marks-0.25
    wrong+=1

print("Q4. What 1024x2?\na.90876\nb.0\nc.2056\nd.2048")
c4=input("Enter your choice : ")
if c4 in "dD":
    marks+=1
    right=+1
else:
    marks=marks-0.25
    wrong+=1

print("Total marks stored : ",marks)
print("Total right answers : ",right)
print("Total wrong answers : ",wrong)
print((marks/4)*100,"% scored")