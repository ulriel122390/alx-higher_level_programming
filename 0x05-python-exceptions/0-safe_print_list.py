#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    size_list = 0
    new_list = my_list
    try:
        for i in range(0, x):
            new_list[i] = my_list[i]
        for j in new_list[:x]:
            if(j == new_list[x-1]):
                print("{}".format(j))
            else:
                print("{}".format(j), end = "")
        return (x)
    except IndexError:
        for k in my_list:
            if(k == my_list[-1]):
                print("{}".format(k))
            else:
                print("{}".format(k), end = "")
            size_list += 1
        return (size_list)

