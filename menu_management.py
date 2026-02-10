def add_item(menu, item):
    menu.append(item)


def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu")


def check_item(menu, item):
    return item in menu


# Example usage
menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item(menu, "Tacos")
remove_item(menu, "Salad")

print("Updated menu:", menu)

item_to_check = "Pizza"
if check_item(menu, item_to_check):
    print(f"{item_to_check} is available")
else:
    print(f"{item_to_check} is not available")
