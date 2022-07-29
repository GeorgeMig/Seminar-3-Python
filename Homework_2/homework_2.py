my_list = [2, 3, 4, 5, 6, 8, 3]
def res_values(list):
    res_list = []
    for i in range(len(list) - int(len(list) / 2)):
        res_list.append(list[(len(list) - 1) - i] * list [i])
    print(res_list)

res_values(my_list)