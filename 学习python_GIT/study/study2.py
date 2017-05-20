height = input('please input your Height: \n')
weight = input('please input your weight \n ')

BMI =weight/(height*height)

if BMI <  18.5:
    print 'BMI:%2f'%(BMI)
    print('Too light')
elif   18.5 < BMI < 23.9:
    print 'BMI:%2f'%(BMI)
    print('normal')
elif  24< BMI < 27:
    print 'BMI:%2f'%(BMI)
    print 'overweight'
elif 28< BMI <32 :
    print 'BMI:%2f'%(BMI)
    print'Obesity'
elif BMI>32:
    print 'BMI:%2f'%(BMI)
    print  'Very fat'