import math

def get_player_pos():

    spawn_coordinate = (0, 0, 0)
    while True:
        coordinate = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            coord = (coordinate.split(","))
            for i in range(3):
                coord[i] = float(coord[i])
            list_coord:tuple = [
                tuple(coord[0:3])
                ]
            print(f"Got a first tuple: {list_coord[0]}")
            x1, y1, z1 = spawn_coordinate
            x2, y2, z2 = list_coord[0]
            print(f"It includes: X={x2}, Y={y2}, Z={z2}")
            dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(f"Distance from spawn point: {dist:.4f}")
            

        except ValueError:
            print("Invalid syntax")

if __name__ == "__main__":
    get_player_pos()
