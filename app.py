import math
import datetime as d
import jpholiday
import time
import re
import sys

# check holiday
def isHoliday(inputDate):
   array = re.split('/', inputDate)
   dateCheck = d.date(int(array[0]), int(array[1]), int(array[2]))
   if dateCheck.weekday() >= 5 or jpholiday.is_holiday(dateCheck):
      return 1
   else:
      return 0

# total Calculation
def totalCalculation(rtype, size, km, holidayPer = 1):
   total = (rtype + size + km) * holidayPer
   return int(total)

# type miss
def checkFinish(num):
   if num > 0:
      print('Input error.')
      sys.exit()


print('''
$$\      $$\           $$\                                                     $$\                    $$\      $$\                    $$\                            $$$$$$\                         $$\   $$$$$$$$\ $$$$$$$\      
$$ | $\  $$ |          $$ |                                                    $$ |                   $$$\    $$$ |                   \__|                          $$  __$$\                        $$ |  \__$$  __|$$  __$$\     
$$ |$$$\ $$ | $$$$$$\  $$ | $$$$$$$\  $$$$$$\  $$$$$$\$$$$\   $$$$$$\        $$$$$$\   $$$$$$\        $$$$\  $$$$ | $$$$$$\$$\    $$\ $$\ $$$$$$$\   $$$$$$\        $$ /  \__|$$$$$$\                $$ |     $$ |   $$ |  $$ |    
$$ $$ $$\$$ |$$  __$$\ $$ |$$  _____|$$  __$$\ $$  _$$  _$$\ $$  __$$\       \_$$  _| $$  __$$\       $$\$$\$$ $$ |$$  __$$\$$\  $$  |$$ |$$  __$$\ $$  __$$\       $$ |     $$  __$$\               $$ |     $$ |   $$ |  $$ |    
$$$$  _$$$$ |$$$$$$$$ |$$ |$$ /      $$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |        $$ |   $$ /  $$ |      $$ \$$$  $$ |$$ /  $$ \$$\$$  / $$ |$$ |  $$ |$$ /  $$ |      $$ |     $$ /  $$ |              $$ |     $$ |   $$ |  $$ |    
$$$  / \$$$ |$$   ____|$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|        $$ |$$\$$ |  $$ |      $$ |\$  /$$ |$$ |  $$ |\$$$  /  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$\$$ |  $$ |              $$ |     $$ |   $$ |  $$ |    
$$  /   \$$ |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$  |$$ | $$ | $$ |\$$$$$$$\         \$$$$  \$$$$$$  |      $$ | \_/ $$ |\$$$$$$  | \$  /   $$ |$$ |  $$ |\$$$$$$$ |      \$$$$$$  \$$$$$$  |$$\ $$\       $$$$$$$$\$$ |   $$$$$$$  |$$\ 
\__/     \__| \_______|\__| \_______| \______/ \__| \__| \__| \_______|         \____/ \______/       \__|     \__| \______/   \_/    \__|\__|  \__| \____$$ |       \______/ \______/ \__|$  |      \________\__|   \_______/ \__|
                                                                                                                                                    $$\   $$ |                             \_/                                     
                                                                                                                                                    \$$$$$$  |                                                                     
                                                                                                                                                     \______/                                                                      
''')

print('Welcome to Moving Co., LTD.')
print('Answer the following questions to calculate your moving costs.')

print('What is you building type, write the corresponding number from 1 to 3')
print('1. Domitory')
print('2. Apartment')
print('3. Detached House')
roomType = input('answer: ')

patternType = r'[1-3]$'
for i in range(2):
   if re.fullmatch(patternType, roomType):
      roomType = int(roomType)
      break
   else:
      print('Please enter correctly. (half-width digit)')
      roomType = input('answer: ')
      checkFinish(i)

if roomType == 1:
   rtype = 20000
elif roomType == 2:
   rtype = 30000
else:
   rtype = 50000

if roomType != 1:
   print('What is you room size, write the corresponding number from 1 to 4')
   print('1. 1K')
   print('2. 1LDK')
   print('3. 2LDK')
   print('4. 3LDK')
   roomSize = input('answer: ')

   patternSize = r'[1-4]$'
   for i in range(2):
      if re.fullmatch(patternSize, roomSize):
         roomSize = int(roomSize)
         break
      else:
         print('Please enter correctly. (half-width digit)')
         roomSize = input('answer: ')
         checkFinish(i)

   if roomSize == 1:
      rsize = 20000
      truck = '2t Truck'
   elif roomSize == 2:
      rsize = 40000
      truck = '3t Truck'
   elif roomSize == 3:
      rsize = 50000
      truck = '3t Truck'
   elif roomSize == 4:
      rsize = 60000
      truck = '4t Truck'

else:
   rsize = 0
   truck = 'Minitruck'

print('How long is the distance from the origin to destination in KM?')
print('you can use google maps https://www.google.com/maps')
distance = input('answer: ')

patternDistance = r'[0-9.]+$'
for i in range(2):
   if re.fullmatch(patternDistance, distance):
      distance = int(distance)
      break
   else:
      print('Please enter correctly. (half-width digit)')
      distance = input('answer: ')
      checkFinish(i)

if (distance <= 100):
   km = 20000
else:
   km = 20000 + (distance - 100) * 200

print('When do you plan to move out? ex) 2020/09/01')
dt = input('answer: ')

patternDate = r'^[12]\d{3}\/(0?[1-9]|1[0-2])\/(0?[1-9]|[12][0-9]|3[01])$'
   
for i in range(2):
   if re.fullmatch(patternDate, dt):
      break
   else:
      print('Please enter correctly. ex) 2020/09/01')
      dt = input('answer: ')
      checkFinish(i)

if isHoliday(dt) == 1:
   holidayPer = 1.1
else:
   holidayPer = 1

totalCost = totalCalculation(int(rtype), int(rsize), int(km), holidayPer)

print('Thank you for your input.')
print('Truck size: {} '.format(truck))
print('Total: {} yen'.format(totalCost))



