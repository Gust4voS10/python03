import random


def main():
    achievements = {"Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme",
                    "Untouchable", "Sharp Mind", "Boss Slayer"}
    Alice: set = set()
    Bob: set = set()
    Charlie: set = set()
    Dylan: set = set()
    for _ in range(7):
        Alice.add(random.choice(list(achievements)))
        Bob.add(random.choice(list(achievements)))
        Charlie.add(random.choice(list(achievements)))
        Dylan.add(random.choice(list(achievements)))
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}")
    All_distinct = Alice.union(Bob).union(Charlie).union(Dylan)
    print(f"\nAll distinct achievements: {All_distinct}")
    common_achievements = (
        Alice.intersection(Bob)
        .intersection(Charlie)
        .intersection(Dylan)
    )
    print(f"\nCommon achievements: {common_achievements}\n")
    print(f"Only Alice: "
          f"{Alice.difference(Bob).difference(Charlie).difference(Dylan)}")
    print(f"Only Bob: "
          f"{Bob.difference(Alice).difference(Charlie).difference(Dylan)}")
    print(f"Only Charlie: "
          f"{Charlie.difference(Alice).difference(Bob).difference(Dylan)}")
    print(f"Only Dylan: "
          f"{Dylan.difference(Alice).difference(Bob).difference(Charlie)}")
    print(f"\nAlice is missing: "
          f"{achievements.difference(Alice)}")
    print(f"Bob is missing: "
          f"{achievements.difference(Bob)}")
    print(f"Charlie is missing: "
          f"{achievements.difference(Charlie)}")
    print(f"Dylan is missing: "
          f"{achievements.difference(Dylan)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    main()
