from BST import Tree
from AVL_tree import AVL_tree
import matplotlib.pyplot as plt
import timeit
import numpy as  np
import sys
#function for creating the list of numbers
def get_numbers(amount= 100,low= 1 , high= 3000):
    array = []
    for i in range(amount):
        array.append(np.random.randint(low , high))
    return array

def draw_graph(times, amount, title):
    y = times
    x = amount
    plt.plot(x, y)
    plt.ylabel("Time")
    plt.xlabel("Amount of words")
    plt.title(title)
    plt.show
    plt.savefig(title + ".png")
    plt.close()

def get_sub_array(amount, array=[]):
    sub_array = []
    for i in array:
        sub_array.append(i)
        amount = amount -1
        if amount == 0:
            return sub_array



number_list = get_numbers(10000)
max = 10000
increment = 1000
amount = 0

time_creat_BST = []
time_delet_BST = []
time_creat_AVL = []
time_delet_AVL = []

numbers = []
if numbers == []:
    while amount < max:
        amount = amount + increment
        create = get_sub_array(amount, number_list)
        amount_inner = 0
        b = Tree()
        a = AVL_tree()
        def creation_bst():
            b.creator(create )
        def deletion_bst():
            b.destructor(delete)
        def creation_AVL():
            a.creator(create)
        def deletion_AVL():
            a.destructor(delete)
        numbers.append(amount)
        time_creation_bst = round(timeit.timeit('creation_bst()','from main import creation_bst', number = 1),7)
        time_creation_AVL = round(timeit.timeit('creation_AVL()','from main import creation_AVL', number = 1),7)
        time_creat_BST.append(time_creation_bst)
        time_creat_AVL.append(time_creation_AVL)
        print('---------------------------------------------------------------------------------------------')
        print (str(amount) + "|BST create:" + str(time_creation_bst)+ "|AVL create:" + str(time_creation_AVL))
        print('---------------------------------------------------------------------------------------------')
        while amount_inner < max/10:
            amount_inner = amount_inner + increment/10 
            delete = get_sub_array(int(amount_inner/10),number_list)
            b = Tree()
            a = AVL_tree()
            creation_AVL()
            creation_bst()
            time_deletion_bst = round(timeit.timeit('deletion_bst()','from main import deletion_bst', number = 1),7)
            time_deletion_AVL = round(timeit.timeit('deletion_AVL()','from main import deletion_AVL', number = 1),7)
            time_delet_BST.append(float(time_deletion_bst))
            time_delet_AVL.append(float(time_deletion_AVL))
            print (str(amount_inner) + "|BST delete:"+ str(time_deletion_bst) + "|AVL delete:" + str(time_deletion_AVL))



small_del_bst = get_sub_array(10, time_delet_BST)
small_del_avl = get_sub_array(10, time_delet_AVL)
draw_graph(time_creat_BST, numbers, "BST Creation")
draw_graph(time_creat_AVL, numbers, "AVL Creation")
draw_graph(small_del_bst, numbers, "BST Destruction - 1000")
draw_graph(small_del_avl, numbers, "AVL Destruction - 1000")
sys.exit()