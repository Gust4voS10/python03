import sys

def is_number(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

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

        except ValueError:
            for arg in sys.argv[1:]:
                if is_number(arg) == False:
                    print(f"Invalid parameter: {arg}")
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")

if __name__ == "__main__":
    main()
