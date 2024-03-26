inventory = {"Food": 0, "Pants": 0, "Shirts": 0, "Toys": 0}

running = True
while running:
    menu = int(
        input(
            f"Please input a number for the desired item to update:\n# 1. Food\n# 2. Pants\n# 3. Shirts\n# 4. Toys\n"
        )
    )
    
    match(menu):
        case 1:category="Food"
        case 2:category="Pants"
        case 3:category="Shirts"
        case 4:category="Toys"
        case default:
            print("Wrong input")
            continue
        
    action = int(input(f"Please input the number for action:\n# 1. Add\n# 2. Remove\n"))
    if action not in[1,2]:
         print("Wrong input")
         continue
    quantity = int(input(f"Please input the number of items to {"add" if action==1 else "remove"}: \n"))
    if action == 1:
        inventory[category] += quantity
    else:
        if inventory[category]>=quantity:
            inventory[category] -= quantity
        else:
            print("Not enough inventory")
    print(f"Updated inventory:{inventory}")
    running = input("Do you want to modify another item? (yes/no):\n") == "yes"
