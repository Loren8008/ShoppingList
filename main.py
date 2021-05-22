def main():
    while(1):
        loaded_list = {
            'test_product' : [2, 20]
                    }
        types_list = {
            'type_1' : "test_product",
            'type_1' : "test_product2",
            'type_1' : "test_product3",
            'type_2' : "test_product4"
                    }
        selection_shopping_list(loaded_list)
    # year_list = calc_leap_years(1900, 2000)
    # print(year_list)

# def calc_leap_years(first_y, last_y):
    # leap_year_list = [year for year in range(first_y, (last_y+1)) if ( ( (year % 4 == 0)and(year % 100 != 0) )or(year % 400 == 0) ) ]
    # return leap_year_list
    
def add_pos(loaded_list):
    new_product = ""
    quantity_value = []
    new_product = input ("insert product name\n")
    quantity_value.append(input ("insert product quantity\n"))
    quantity_value.append(input ("insert product price\n"))
    loaded_list[new_product] = quantity_value
    return loaded_list
    
def rem_pos(loaded_list):
    product_to_remove = ""
    quantity_value = [2]
    product_to_remove = input ("insert product name to delete\n")
    quantity_to_remove = int(input ("how many pieces you want to delete\n"))
    print(product_to_remove)
    if ((0 > quantity_to_remove) or (quantity_to_remove == int(loaded_list.get(product_to_remove)[0]))):
        loaded_list.pop(product_to_remove)
    else:
        loaded_list[product_to_remove][0] = (int(loaded_list.get(product_to_remove)[0]) - quantity_to_remove)
    return loaded_list
    
def prt_pos(loaded_list):
    clear()
    print ("Procuts: ")
    for product in loaded_list:
            print (product)
            
def selection_shopping_list(loaded_list):
    shopping_list_menu = ["1: Change current list", "2: Add/remove list", "3: Edit list", "4: Print list", "5: Go back\n"]
    for item in shopping_list_menu:
        print (item)
    user_choice = (input("select option "))
    if ("1" == user_choice):
        clear()
        print("bruh\n")
    elif ("2" == user_choice):
        clear()
        print("bruh\n")
    elif ("3" == user_choice):
        clear()
        selection_shopping_list_edit(loaded_list)
    elif ("4" == user_choice):
        clear()
        prt_pos(loaded_list)
        input()
    elif ("5" == user_choice):
        exit()
    else:
        clear()
        print("bruhx2\n")
def selection_shopping_list_edit(loaded_list):
    shopping_list_edit_menu = ["1: Add", "2: Remove", "3: Go back\n"]
    for item in shopping_list_edit_menu:
        print (item)
    user_choice = (input("select option "))
    while("3" != user_choice):
        for item in shopping_list_edit_menu:
            print (item)
        user_choice = (input("select option "))
        if ("1" == user_choice):
            clear()
            prt_pos(loaded_list)
            loaded_list = add_pos(loaded_list)
        elif ("2" == user_choice):
            clear()
            prt_pos(loaded_list)
            loaded_list = rem_pos(loaded_list)
        elif ("3" == user_choice):
            clear()
            prt_pos(loaded_list)
            loaded_list = rem_pos(loaded_list)
        else:
            print("bruhx3\n")
    clear()
import os
clear = lambda: os.system('cls') #on Windows System


if __name__ == "__main__":
    main()
    
        