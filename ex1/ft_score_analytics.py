import sys


def is_number(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    num = []
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        for a in sys.argv[1:]:
            try:
                # num.append(int(a))
                num += [int(a)]
                int_max = max(num)
                int_min = min(num)
            except ValueError:
                print(f"Invalid parameter: {a}")
        if len(num) == 0:
            print("No scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")
            return
        plus = 0
        i = int(len(sys.argv[1:]))
        print("=== Player Score Analytics ===")
        print(f"score processed: {num}")
        print(f"total players: {i}")
        for n in num:
            plus += n
        print(f"total score: {plus}")
        print(f"Average score: {plus / i:.1f}")
        print(f"High score: {int_max}")
        print(f"Low score: {int_min}")
        print(f"Score range: {int_max - int_min}\n")


if __name__ == "__main__":
    main()
