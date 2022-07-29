my_list = [1.1, 1.2, 3.1, 5, 10.01]
def diff_maxmin(list):
    max = 0
    for i in list:
        res = round(i - round(i, 0), 2)
        if res> max:
            max = res
    min = max
    for i in list:
        if res != 0 and res < min:
            min = res
    print(max - min)
diff_maxmin(my_list)