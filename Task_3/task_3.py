

list = ['12', '123', '456', '123456', '43251645', '456123']
#strc = input('Введите искомое число в списке: ')
strc = '12'
count = 0
for i in list:
    if strc in i:
        count += 1

print(count)