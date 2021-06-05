
import os
import pickle


def main():
    loaded_list_name = check_latest_name()
    loaded_list = load_shopping_list(loaded_list_name)

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
        'WhiteCheese': 7.6,
        'YellowCheese': 4.2,
        'Milk': 5.3,
        'Butter': 3,
        'Pepsi': 7.8,
        'Chocolate': 4.5,
        'Orange Juice': 5.5,
        'IceCream': 3.2
    }
    while 1:
        loaded_list, product_list, loaded_list_name, types_list = selection_shopping_list(loaded_list, product_list,
                                                                              loaded_list_name, types_list)


def save_lst_name(loaded_list_name):
    file = open("last_lst.txt", "w")
    file.write("{} \n".format(loaded_list_name))
    file.close()


def save_shopping_list(loaded_list, loaded_list_name):
    file = open(loaded_list_name, "w")
    for x in loaded_list:
        file.write("{} {}\n".format(x, loaded_list[x]))
    file.close()


def check_latest_name():
    file = open("last_lst.txt", "r")
    lastest_name = file.read()
    file.close()
    return lastest_name


def load_shopping_list(list_to_load):
    loaded_list = {}
    if os.stat(list_to_load).st_size == 0:
        print("empty")
        list_to_load.close()
        return loaded_list
    print(list_to_load)
    with open(list_to_load, "r") as file:
        for line in file:
            key, value = line.split()
            loaded_list[key] = int(value)
    file.close()
    return loaded_list

def sort_list_by_category(loaded_list, types_list):
    sorted_list = {}
    category = input("Input category you want to sort by: ")
    for key in loaded_list.keys():
        if key in types_list.keys():
            if types_list[key] == category:
                sorted_list[key] = loaded_list[key]
    print(sorted_list)
    return sorted_list

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


def add_new(loaded_list, product_list, new_product, types_list):
    price = (float(input("Enter new product price\n")))
    product_list[new_product] = price
    quantity = (int(input("insert product quantity\n")))
    loaded_list[new_product] = quantity
    type = input("insert product type\n")
    types_list[new_product] = type
    return loaded_list, product_list, types_list


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
        os.chdir("./Lists")
        os.remove("{}.txt".format(file_name))
        os.chdir("..")
        loaded_list = {}
        return loaded_list
    except IOError:
        print("File doesn't exist\n")
        os.chdir("..")


def add_list(file_name):
    try:
        os.chdir("./Lists")
        open("{}.txt".format(file_name), "x")
        loaded_list = {}
        os.chdir("..")
    except IOError:
        print("A file with that name already exist")
        os.chdir("..")




def selection_add_or_remove(loaded_list, product_list, types_list):
    add_or_remove_menu = ["1. Add", "2. Remove", "3. Go back\n"]

    for elem in add_or_remove_menu:
        print(elem)
    user_choice = input("select option ")
    if user_choice == "1":
        clear()
        print("Existing files: ", os.listdir("Lists"))
        list_to_add = input("Type name of list to add: \n")
        add_list(list_to_add)

    elif user_choice == "2":
        clear()
        print("Existing files: ", os.listdir("Lists"))
        list_to_remove = input("Type name of list to remove: \n")
        remove_list(list_to_remove)

    elif user_choice == "3":
        clear()
        selection_shopping_list(loaded_list, product_list, loaded_list, types_list)


def selection_shopping_list(loaded_list, product_list, loaded_list_name, types_list):
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
        selection_add_or_remove(loaded_list, product_list, types_list)
    elif "3" == user_choice:
        clear()
        selection_shopping_list_edit(loaded_list, product_list, types_list)
    elif "4" == user_choice:
        clear()
        prt_pos(loaded_list)
        print("Summed products cost: {:.2f}".format(sum_price_list(loaded_list, product_list)))
        input()
    elif "5" == user_choice:
        clear()
        save_lst_name(loaded_list_name)
        print("Bye")
        exit()
    else:
        clear()
        print("bruhx2\n")
    return loaded_list, product_list, loaded_list_name, types_list


def selection_shopping_list_edit(loaded_list, product_list, types_list):
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
                sorted_loaded_list = sort_list_by_category(loaded_list, types_list)
                print(sum_price_list(sorted_loaded_list, product_list))
            elif user_choice == "B":
                return loaded_list
            else:
                loaded_list, product_list, tyepes_list= add_new(loaded_list, product_list, user_choice, types_list)
        else:
            print("Invalid input\n")
        return loaded_list, product_list, types_list


clear = lambda: os.system('cls')  # on Windows System

if __name__ == "__main__":
    main()
