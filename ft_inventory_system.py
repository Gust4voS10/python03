import sys
import random

def main():
    if len(sys.argv) > 2:
        items = {'sword': 0, 'potion': 0, 'shield': 0, 'armor': 0, 'helmet': 0, 'magic_item': 0}
        for i in range(1, len(sys.argv)):
            split_items = sys.argv[i].split(":")
            if i in items:
            else:
                print(f"Unknown item: {item}")
