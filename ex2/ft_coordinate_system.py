import math

def get_player_pos():
    print("Get a first set of coordinates")
    while True:
        spawn_coordinate = (0, 0, 0)
        coordinate = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            coord = (coordinate.split(","))
            for i in range(3):
                coord[i] = float(coord[i])
            list_coord = tuple(coord)
            print(f"Got a first tuple: {list_coord[0]}")
            x1, y1, z1 = spawn_coordinate
            x2, y2, z2 = list_coord
            print(f"It includes: X={x2}, Y={y2}, Z={z2}")
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(f"Distance from spawn point: {dist:.4f}")
            break
        except ValueError:
            print("Invalid syntax")
    print("\nGet a second set of coordinates")
    while True:
        coordinate = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            coord = (coordinate.split(","))
            for i in range(3):
                coord[i] = float(coord[i])
            list_coord = tuple(coord)
            x3, y3, z3 = list_coord
            dist = math.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2)
            print(f"Distance between the 2 sets of coordinates: {dist:.4f}")
            break
        except ValueError:
            print("Invalid syntax")

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
