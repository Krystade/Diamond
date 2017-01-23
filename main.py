print('How many lines wide in the center?')
try:
    width = int(input())
except ValueError:
    print('Not an Integer')
    quit()
for i in range(1,width,2):
    print (('*' * i).center(width))
center = i
for i in range(center - 2,0,-2):
    print (('*' * i).center(width))
