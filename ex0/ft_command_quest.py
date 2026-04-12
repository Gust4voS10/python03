import sys


def main():
    print("=== Command Quest ===")
    count = len(sys.argv)
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print(f"program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments received {count - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"total arguments: {count}\n")


if __name__ == "__main__":
    main()
