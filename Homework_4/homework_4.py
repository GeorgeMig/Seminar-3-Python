number = 45

def second_system(num):
    res = []
    count = num
    while count >= 1:
        if int(round(count, 0)) > count:
            res.append((int(round(count, 0)) - 1) % 2)
        else:
            res.append(int(round(count, 0)) % 2)
        count = count / 2
    for i in range (len(res)):
        print(res[(len(res) - 1) - i], end=' ')
second_system(number)