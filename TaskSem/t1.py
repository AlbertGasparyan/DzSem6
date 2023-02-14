
# lst1=[3,1,3,4,2,4,12]
# lst2=[4,15,43,1,15,1]

lst1=[int(input(f"Enter {i+1} num in list:")) for i in range(int(input("Enter len first list:")))]
print(lst1)

lst2=[int(input(f"Enter {i+1} num in list:")) for i in range(int(input("Enter len second list:")))]
print(lst2)

result= list(filter(lambda el:el not in lst2,lst1))


print(f'Ваш первый список:{lst1}\n'
      f'Ваш второй список:{lst2}\n'
      f'Ваш результат: {result}'
      )


