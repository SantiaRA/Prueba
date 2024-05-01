from addition import add
from sustraction import rest
from multiplication import multi
from divition import divit
from power import potent
from module import modul
def game():
  score = 0
  while True:
     print('======== Menu ========'
     '\n1. Add'
     '\n2. Rest'
     '\n3. Multiplication'
     '\n4. Divition'
     '\n5. Power'
     '\n6. Module'
     '\n0. Exit')
 option = int(input('\nChoice an option: '))
 if option == 0:
   break
 num_1 = int(input('Enter first number: '))
 num_2 = int(input('Enter second number: '))
 answer = int(input('Enter you answer: '))
 if option == 1:
   result = add(num_1, num_2)
   if result == answer:
     score += 1
     print('Correct!!')
   else:
     print('Incorrect')
 if option == 2:
    result = rest(num_1, num_2)
    if result == answer:
      score += 1
      print('Correct!!')
    else:
      print('Incorrect')
 if option == 3:
    result = multi(num_1, num_2)
    if result == answer:
      score += 2
      print('Correct!!')
    else:
      print('Incorrect')
 if option == 4:
    result = divit(num_1, num_2)
    if result == answer:
      score += 2
      print('Correct!!')
    else:
      print('Incorrect')
 if option == 5:
    result = potent(num_1, num_2)
    if result == answer:
      score += 4
      print('Correct!!')
    else:
      print('Incorrect')
 if option == 6:
    result = modul(num_1, num_2)
    if result == answer:
      score += 4
      print('Correct!!')
    else:
      print('Incorrect')
      
 print(f'======== Game Over ========'
 f'\nYou score is {score}'
 '\nKeep going!')
game()
