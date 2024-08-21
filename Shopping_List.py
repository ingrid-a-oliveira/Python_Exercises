shopping_list = []

while True:
    print("Menu")
    print("1-Insert Item\n2-See Item\n3-Remove Item\n4-Exit")
    
    option = int(input("What do you want to do? "))
    
    if option == 1:
        item = input("Insert the item: ")
        shopping_list.append(item)
        
    elif option == 2:
        for i in range (0, len(shopping_list)):
            print(f"{i+1} - {shopping_list[i]}")
        
    elif option == 3:
        delete_item = input("What item do you want to remove? ")
        if delete_item in shopping_list:
            shopping_list.remove(delete_item)
        else:
            print("This item isn't in list.")
        
    elif option == 4:
        break
    
    else:
        print("This option is invalid. Choice 1, 2 or 3")