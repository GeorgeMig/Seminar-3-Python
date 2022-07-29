my_list = [1, 2, 3, 4, 5, 6, 7]
def summ_oddindex(list):
    res = 0
    for i in range(1, len(list), 2):
        res += list[i]
    print(res)

summ_oddindex(my_list)
