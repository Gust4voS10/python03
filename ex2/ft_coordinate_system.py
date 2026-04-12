import math


class Input_erro(Exception):
    def __init__(self, msg="Invalid syntax"):
        super().__init__(msg)


def get_player_pos():
    print("Get a first set of coordinates")
    while True:
        spawn_coordinate = (0, 0, 0)
        coordinate = input(
            "Enter new coordinates as floats in format 'x,y,z': "
            )
        try:
            coord = (coordinate.split(","))
            if len(coord) != 3:
                raise Input_erro
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
            print(f"Error on parameter '{coord[i]}': "
                  f"could not convert string to float: '{coord[i]}'")
        except Input_erro as a:
            print(a)
    print("\nGet a second set of coordinates")
    while True:
        try:
            coordinate = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                )
            coord = (coordinate.split(","))
            if len(coord) != 3:
                raise Input_erro
            for i in range(3):
                coord[i] = float(coord[i])
            list_coord = tuple(coord)
            x3, y3, z3 = list_coord
            dist = math.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2)
            print(f"Distance between the 2 sets of coordinates: {dist:.4f}")
            break
        except ValueError:
            print(f"Error on parameter '{coord[i]}': "
                  f"could not convert string to float: '{coord[i]}'")
        except Input_erro as a:
            print(a)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
