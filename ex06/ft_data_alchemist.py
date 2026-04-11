import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    Player = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
              "john", "kevin", "Liam"]
    print(f"\nInitial list of players: {Player}")

    all_cap = [name for name in Player if name.istitle()]
    all_upca = [name.capitalize() for name in Player]
    print(f"New list with all names capitalized: {all_upca}")
    print(f"New list of capitalized names only: {all_cap}\n")
    dict_cap = {name: random.randint(1, 100) for name in all_upca}
    print(f"Score dict: {dict_cap}")
    average = sum(dict_cap.values()) / len(dict_cap)
    print(f"Score average is {average:.2f}\n")
    above_average = {
        name: score for name,
        score in dict_cap.items() if score > average
        }
    print(f"High scores: {above_average}")


if __name__ == "__main__":
    main()
