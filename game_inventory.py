from prettytable import PrettyTable
# import csv


inventory = {
    "magic scrolls": "3",
    "arrows": "6",
    "HP potions": "8",
    "mana potions": "3",
    "gloves": "2",
}


def display_inventory(inventory):
    for x, y in inventory.items():
        print(x + ": " + y + "\n") 
        

# w = display_inventory(inventory)


def add_to_inventory(inventory, added_items, items_no):
    for i in added_items:
        if i not in inventory:   
            inventory.update([(i, int(items_no))])
        else:
            inventory.update([(i, int(inventory.get(i)) + int(items_no))])
                
    return inventory


# w = add_to_inventory(inventory, ["gloves", "gloves", "armor", "gloves", "ring"])
# print(w)

def remove_from_inventory(inventory, removed_items, items_no):
    for i in removed_items:
        if i in inventory:
            inventory.update([(i, int(inventory.get(i)) - int(items_no))])
            if inventory.get(i) == 0: 
                del inventory[i]
    
    return inventory


# w = remove_from_inventory(inventory, ["arrows"])
# print(w)


def print_table(inventory, order):
    table = PrettyTable()
    table.field_names = ["item name", "count"]
    for i in inventory:
        table.add_row([i, inventory.get(i)])
   
    if order == "ascending":
        print(table.get_string(sortby="count"))
    elif order == "descending":
        print(table.get_string(sortby="count", reversesort=True))
    else:
        print(table)


# w = print_table(inventory, "count,asc")


# def import_inventory(inventory, filename):
#     with open("inv_list.csv", "r") as filename:
#         reader = csv.DictReader(filename, fieldnames="item name")
#         for i in reader:
#             inventory.update[i]
            
        
# print(import_inventory(inventory, "inv_list.csv"))


# def export_inventory(inventory, filename):
#     with open("csv_inventory.txt", "w") as filename:
#         csv.writer = csv.DictWriter(filename, delimiter=",")
#         for i in filename:
#             if i in inventory:
#                 inventory.update()


def main():

    print_table(inventory, "")

    question = input("Do you want to order your items?" + "\n")
    if question == "Yes" or question == "yes":
        user_order = input("How? ascending or descending?" + "\n").lower()
        if user_order == "ascending" or "Ascending":
            print_table(inventory, "ascending")
        elif user_order == "descending" or "Descending":
            print_table(inventory, "descending")
        else:
            print("The inventory will be sorted in a default order:" + "\n")
            user_order = ""
            print_table(inventory, "")
    elif question == "No" or question == "no":
        print("The inventory will be sorted in a default order:" + "\n")
        user_order = ""
        print_table(inventory, "")
    else:
        print("The inventory will be sorted in a default order:" + "\n")
        user_order = ""
        print_table(inventory, "")

    while True:
        answer = input("Do you want to add or remove an item?" + "\n")
        added_items = []
        removed_items = []
        items_no = 0
        if answer == "Yes" or answer == "yes":
            new_answer = input("Add or remove?" + "\n")
            if new_answer == "add" or new_answer == "Add":
                added_item = input("Enter the item you want to add: " + "\n")
                items_no = int(input("How many?" + "\n"))
                if added_item != "":
                    added_items.append(added_item)
                    add_to_inventory(inventory, added_items, items_no)
                    print_table(inventory, user_order)       
            elif new_answer == "remove" or new_answer == "Remove":
                removed_item = input("Enter the iteam you want to remove: " + "\n")
                items_no = int(input("How many?" + "\n"))
                if removed_item != "":
                    removed_items.append(removed_item)
                    remove_from_inventory(inventory, removed_items, items_no)
                    print_table(inventory, user_order)
        elif answer == "No" or answer == "no":
            print("Goodbye")
            break
       
#             # answer = input("Do you want to do anything else?" + "\n")
#             # if answer == "No" or answer == "no":
#             #     print("Goodbye")
#             #     break


main()