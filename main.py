""" #how to save dictionary to file
def write_dictionary(dict):
    file = open("dict.txt", "w")
    for x in dict:
        file.write("{} {}\n".format(x, dict[x]))
    file.close()
"""
""" #how to read dictionary from file
def  read_dictionary():
    dict = {}
    if (os.stat('dict.txt').st_size == 0):
        print("empty")
        return dict
    with open("dict.txt") as file:
        for line in file:
            (key, value) = line.split()
            dict[str(key)] = value
    file.close()
    return dict
"""
""" #how to save list to file
def write_list(lst):
    file = open("lst.txt", "w")
    for x in lst:
        file.write(x)
        file.write("\n")
    file.close()
"""
""" how to read list from file
def read_list():  
    lst = []
    with open("lst.txt") as file:
        for line in file:
            line.strip()
            lst.append(line.replace("\n", ""))
    file.close()
    return lst
"""

import os

def main():
    loaded_list = {  # dict of actual shopping list
        'Bread': 2,
        'Ice Cream': 8,
        'Pepsi': 1
    }
    types_list = {
        'Bread': "Pastries",
        'White Cheese': "Dairy",
        'Yellow Cheese': "Dairy",
        'Milk': "Dairy",
        'Butter': "Dairy",
        'Water': "Drinks",
        'Pepsi': "Drinks"
    }
    product_list = {  # dict of avaible predefined products
        'Bread': 4.1,
        'Water': 2.5,
        'White Cheese': 7.6,
        'Yellow Cheese': 4.2,
        'Milk': 5.3,
        'Butter': 3,
        'Pepsi': 7.8,
        'Chocolate': 4.5,
        'Orange Juice': 5.5,
        'Ice Cream': 3.2
    }
    while 1:
        loaded_list, product_list = selection_shopping_list(loaded_list, product_list)


def modify_selected(loaded_list, selected_product):
    quantity = (int(input("insert product quantity\n")))
    if abs(quantity) >= loaded_list[selected_product] and quantity <= 0:
        rem_selected(loaded_list, selected_product)
    else:
        loaded_list[selected_product] += quantity
    return loaded_list


def rem_selected(loaded_list, selected_product):
    loaded_list.pop(selected_product)
    return loaded_list


def add_new(loaded_list, product_list, new_product):
    price = (int(input("Enter new product price\n")))
    product_list[new_product] = price
    quantity = (int(input("insert product quantity\n")))
    loaded_list[new_product] = quantity
    return loaded_list, product_list


def add_existing(loaded_list, selected_product):
    quantity = (input("insert product quantity\n"))
    loaded_list[selected_product] = quantity
    return loaded_list


def select_product():
    return input("Which product do you want select?\n")


def prt_pos(loaded_list):
    print("Products: ")
    if len(loaded_list) == 0:
        print("List is empty")
    else:
        for product in loaded_list:
            print("-{} :{}".format(product, loaded_list[product]))


def sum_price_list(list_to_sum, product_list):
    sum_price = 0
    for product in list_to_sum:
        sum_price += (list_to_sum[product] * product_list[product])
    return sum_price


def remove_list(file_name):
    try:
        os.remove("{}.txt".format(file_name))
    except IOError:
        print("File doesn't exist")
    loaded_list = {}
    return loaded_list


def add_list(file_name):
    try:
        open("{}.txt".format(file_name), "x")
    except IOError:
        print("A file with that name already exist")
    loaded_list = {}
    return loaded_list, file_name


def selection_add_or_remove():
    add_or_remove_menu = ["1. Add", "2. Remove\n"]

    for elem in add_or_remove_menu:
        print(elem)
    user_choice = input("select option ")
    if user_choice == "1":
        clear()
        list_to_add = input("Type name of list to add: \n")
        add_list(list_to_add)

    elif user_choice == "2":
        clear()
        list_to_remove = input("Type name of list to remove: \n")
        remove_list(list_to_remove)


def selection_shopping_list(loaded_list, product_list):
    shopping_list_menu = ["1: Change current list", "2: Add/remove list", "3: Edit list", "4: Print list",
                          "5: Go back\n"]
    for item in shopping_list_menu:
        print(item)
    user_choice = (input("select option "))
    if "1" == user_choice:
        clear()
        print("bruh\n")
    elif "2" == user_choice:
        clear()
        selection_add_or_remove()
    elif "3" == user_choice:
        clear()
        selection_shopping_list_edit(loaded_list, product_list)
    elif "4" == user_choice:
        clear()
        prt_pos(loaded_list)
        print("Summed products cost:", sum_price_list(loaded_list, product_list))
        input()
    elif "5" == user_choice:
        clear()
        print("Bye")
        exit()
    else:
        clear()
        print("bruhx2\n")
    return loaded_list, product_list


def selection_shopping_list_edit(loaded_list, product_list):
    shopping_list_edit_menu = ["enter position: Modify selected", "R: Remove", "B: Go back", "S: Sum up product prices",
                               "SB: Sum up product prices by category\n"]
    while 1:
        clear()
        prt_pos(loaded_list)
        for item in shopping_list_edit_menu:
            print(item)
        user_choice = (input("select option "))
        if type(user_choice) == str:
            if user_choice in loaded_list:
                loaded_list = modify_selected(loaded_list, user_choice)
            elif user_choice in product_list:
                loaded_list = add_existing(loaded_list, user_choice)
            elif user_choice == "R":
                if len(loaded_list) == 1:
                    clear()
                    loaded_list = rem_selected(loaded_list, (list(loaded_list.keys())[0]))
                else:
                    loaded_list = rem_selected(loaded_list, select_product())
            elif user_choice == "S":
                print(sum_price_list(loaded_list, product_list))
            elif user_choice == "SB":
                print(sum_price_list(loaded_list, product_list))
            elif user_choice == "B":
                return loaded_list
            else:
                loaded_list, product_list = add_new(loaded_list, product_list, user_choice)
        else:
            print("Invalid input\n")
        return loaded_list, product_list




clear = lambda: os.system('cls')  # on Windows System

if __name__ == "__main__":
    main()