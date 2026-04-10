import sys


def main():
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        try:
            num: list[int] = [int(a) for a in sys.argv[1:]]
            int_max = max(num)
            int_min = min(num)
            plus = 0
            i = len(sys.argv[1:])
            print("=== Player Score Analytics ===")
            print(f"score processed: {num}")
            print(f"total players: {i}")
            for n in num:
                plus += n
            print(f"total score: {plus}")
            print(f"Average score: {plus / i}")
            print(f"High score: {int_max}")
            print(f"fow score: {int_min}")
            print(f"Score range: {int_max - int_min}")

        except ValueError:
            print("the points have to be numbers")


if __name__ == "__main__":
    main()
