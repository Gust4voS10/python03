import random
from typing import Generator

PLAYERS = ["bob", "alice", "dylan", "charlie"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(data_list: list) -> Generator[tuple[str, str], None, None]:
    while len(data_list) > 0:
        index = random.randrange(len(data_list))
        yield data_list.pop(index)


def main() -> None:
    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    seed_events = [next(event_stream) for i in range(10)]
    print(f"Built list of 10 events: {seed_events}")

    for event in consume_event(seed_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {seed_events}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
