import random


state= input('1:自动模式\n2:手动模式\n')

while(True):    
    if state == '1':
        a = round(random.uniform(1,10))
        b = round(random.uniform(1,10))
        c = round(random.uniform(1,10))
        d = round(random.uniform(1,10))
        arr = [float(a),float(b),float(c),float(d)]
        print('\n题目:',arr)
        input('回车显示答案')
    #
    # print(a,b,c,d)
    elif state == '2':
        arr=[]
        nums=input("请输入4个整数（用空格隔开）:")
        num=nums.split(' ')
        print(num)
        print()
        for i in num:
            arr.append(float(i))
        print('题目:',arr)
    # print('arr2',arr2)

    def perm(items, n=None):
        if n is None:
            n = len(items)
        for i in range(len(items)):
            v = items[i:i+1]
            if n == 1:
                yield v
            else:
                rest = items[:i] + items[i+1:]
                for p in perm(rest, n-1):
                    yield v + p

    def F(a,b):
        arr={}
        for i in a:
            for j in b:
                va=a[i]
                vb=b[j]
                arr.update({"("+i+"+"+j+")":va+vb})
                arr.update({"("+i+"-"+j+")":va-vb})
                arr.update({"("+j+"-"+i+")":vb-va})
                arr.update({"("+i+"*"+j+")":va*vb})
                vb>0 and arr.update({"("+i+"/"+j+")":va/vb})
                va>0 and arr.update({"("+j+"/"+i+")":vb/va})
        return arr

    # input('显示答案')

    for i in perm(arr):
          dic=[{"a":i[0]},{"b":i[1]},{"c":i[2]},{"d":i[3]}]
          alist=F(F(F(dic[0],dic[1]),dic[2]),dic[3])
          blist=F(F(dic[0],dic[1]),F(dic[2],dic[3]))
          for i in alist:
              if alist[i]==24.0:
                 print(i.replace('a',str(dic[0]['a'])).replace('b',str(dic[1]['b'])).replace('c',str(dic[2]['c'])).replace('d',str(dic[3]['d'])))
          for i in blist:
              if blist[i]==24.0:
                 print(i.replace('a',str(dic[0]['a'])).replace('b',str(dic[1]['b'])).replace('c',str(dic[2]['c'])).replace('d',str(dic[3]['d'])))