def sum_div(a):
    sum_a=0
    for i in range(1,a):
        if a%i==0:
            sum_a+=1
    return sum_a

def sum_num(n):
    for i in range(1,n):
        sum_1=sum_div(i)
        sum_2=sum_div(sum_1)
        if i==sum_2 and i<sum_1:
            print(i,sum_1)

sum_num(300)



