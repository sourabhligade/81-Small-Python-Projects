"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
 More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""
  

import datetime,random
def getBirthdays(numberofBirthdays):
    birthdays=[]
    for i in range(numberofBirthdays):
        startOfYear=datetime.date(2001,1,1)
    
        randomNumberOfDays=datetime.timedelta(random.randint(0,364))
        birthday=startOfYear+randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    
    for a,birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA==birthdayB:
                return birthdayA
            
# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
 40.
 41. The Birthday Paradox shows us that in a group of N people, the odds
 42. that two of them have matching birthdays is surprisingly large.
 43. This program does a Monte Carlo simulation (that is, repeated random
 44. simulations) to explore this concept.
 45.
 46. (It's not actually a paradox, it's just a surprising result.)
 47. ''')
 # Set up a tuple of month names in order:


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
 

while True:
    print('how many birthdays shall i generate')
    response=input()
    if response.isdecimal() and (0<int(response)<=100):
        numBDays=int(response)
        break
print()


# Generate and display the birthdays:
# 
print('Here are', numBDays, 'birthdays:')
birthdays =getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
# Display a comma for each birthday after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match=getMatch(birthdays)

print('')


# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()
 
  # Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')
 
print('Let\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
      # Report on the progress every 10,000 simulations:
      if i % 10_000 == 0:
          print(i, 'simulations run...')
      birthdays = getBirthdays(numBDays)
      if getMatch(birthdays) != None:
          simMatch = simMatch + 1
print('100,000 simulations run.')

 # Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.') 
print('That\'s probably more than you would think!')
