### A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
### e mostre sua categoria de acordo com sua idade:
#Até 9 anos : Mirim / Até 14 anos : Infantil / Até 19 anos : Junior / Até 25 anos : Senior / Acima : Master

from datetime import date


current_year = date.today().year
year_of_birth = int(input('Enter year of birth:'))
age = current_year - year_of_birth


if age <= 9:
    print('The Athlete is {} years old'.format(age))
    print('CATEGORY : LITTLE.')
elif age <= 14:
    print('The Athlete is {} years old'.format(age))
    print('CATEGORY : CHILDREN.')
elif age <= 19:
    print('The Athlete is {} years old.'.format(age))
    print('CATEGORY : JUNIOR')
elif age <= 25:
    print('The Athlete is {} years old.'.format(age))
    print('CATEGORY : SENIOR .')
else:
    print('The Athlete is {} years old.'.format(age))
    print('CATEGORY : MASTER.')