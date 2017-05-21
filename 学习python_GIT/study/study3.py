 #-*- coding: UTF-8 -*-

#
# num= random.randint(1,100)
# while True:
#     ans=input('请输入一个值： \n')
#     if ans>num:
#         print('值太大了')
#     elif ans<num:
#         print('值太小了')
#     else:
#         print '你太厉害了'
#         print num
#         type(num)
#         break

# import random
# import math
#
# print random.choice(['hello', 'world'])
#
# import  time
# starttime =time.time()
# print 'start %f '%(starttime)
# for i in range(10):
#     print i
#     endtime = time.time()
#     print 'endtime %f'%endtime
#     print  'total time %f'%(endtime-starttime)


#作业


import random
num= random.randint(1,100)
i=0
count=0
while True:
    i=0
    count+=1
    chos = input('是否开始游戏：1.yes or 2.no \n')
    if chos ==1:
        print'游戏开始，你只有5次机会'
        while i != 5 :
            ans=input('请输入一个值： \n')
            if ans>num:
                print('值太大了')
            elif ans<num:
                print('值太小了')
            else:
                print num,'你太厉害了'
            i+=1
            print '你尝试了',i,'次'
    else:
        print('游戏结束')
        break
avg=i/count
print'平均',avg,'次，才能猜到哦'
