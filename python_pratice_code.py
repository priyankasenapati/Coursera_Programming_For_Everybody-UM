# SEQUENTIAL STEP
#x = 2
#x = x + 1
#print(x)


# CONDITIONAL STEPS
#x = 5
#if x < 10:
#    print('Smaller')
#if x > 20:
#    print('Bigger')

#print('Finis')


# REPEATED STEPS have iteration variables that change each time through a loop.
#n = 5
#while n > 0:
#    print(n)
#    n = n - 1
#print('Blastoff')

#Input Function
#nam = input('Enter your name:')
#print('Welcome', nam)

#COMPARISON OPERATORS
#x = 10
#if x = 10 :
#    print('Equals to 10')
#if x > 9 :
#    print('Lesser than 9')
#if x >= 10 :
#    print('Greater or equal to 10')

# ONE WAY DECISION
#x = 10
#print('Before', x)
#if x == 10:
#    print('it is True')

#print('Afterwards 10')
#print('Before 20')
#if x == 20:
#    print('it is True')

#print('ALL DONE!')

# Nested DECISION
#x = 42
#if x > 1:
#    print('yes')
#    if x < 100 :
#        print('less than 100')
#print('DONE!')

# Two way DECISION

#x = 6
#if x > 2 :
#    print('Bigger')
#else:
#    print('Smaller')

#print('All Done')


# Multi Way Elif which means else if
#x = 7
#if x < 2 :
#    print('less than two')
#elif x > 10 :
#    print('Medium')
#else :
 #  print('Large')
#print('All Done')


# try and except
x = '345678'
try:
    num = int(x)
except:
    num = -1

print('the number', num)
