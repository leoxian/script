def open_file(str_A,str_B,final):
    list_A=[]
    list_B=[]
    with open(str_A) as f:
        for i in f.readlines():
            list_A.append(i)
    with open(str_B) as w:
        for j in w.readlines():
            list_B.append(j)
    list_A=list_A+list_B[1:-1]
    with open(final+'/result.md','w+') as r:
        for i in list_A:
            r.write(i)

    f.close()
    w.close()
    r.close()

print("输入地址:A")
A ='/Users/leo/Desktop/script/invest_amount.md'
print("输入地址:B")
B ='/Users/leo/Desktop/script/invest_return.md'
print("名字")
C ='/Users/leo/Desktop/script'
open_file(A,B,C)