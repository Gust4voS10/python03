import sys
import random


def main():
    inventory = {}
    arguments = sys.argv[1:]
    for arg in arguments:
        try:
            if ':' in arg:
                arg_split = arg.split(':')
                name = arg_split[0]
                amount = int(arg_split[1])
                if name not in inventory.keys():
                    inventory.update({name: amount})
                else:
                    print(f"Redundant item '{name}' - discarding")
            else:
                print(f"Error - invalid parameter: {arg}")
        except ValueError:
            print(f"Quantity error for '{arg_split[0]}': invalid "
                  f"literal for int() with base 10: '{arg_split[1]}'")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the "
          f"{len(inventory)} items: {total}")
    for item, quantity in inventory.items():
        percentage = (quantity / total) * 100
        print(f"{item}: {quantity} ({percentage:.2f}%)")
    list_items_random: list[str] = ["magic_item", "boot", "breastplate", "bow"]
    item_max = max(inventory, key=inventory.get)
    print(f"Item most abundant: {item_max}"
          f" with quantity {inventory[item_max]}")
    item_min = min(inventory, key=inventory.get)
    print(f"Item least abundant: {item_min} "
          f"with quantity {inventory[item_min]}")
    quantity = random.randint(1, 5)
    inventory.update({random.choice(list(list_items_random)): quantity})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
