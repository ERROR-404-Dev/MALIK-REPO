# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question1 = 'Q1) Do you like Dawns or Duscl?'
question1 += '\n1) Dawn\n2) Dusk\n'
int(input(question1))

if question1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif question1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input')

  question2 = int(input('Q2) When Im dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n'))
if question2 == 1:
  Hufflepuff += 1
else:
  print('Wrong input')