from dataclasses import dataclass
import random

# Suits and ranks in the desired order
SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
RANKS = (
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"
)


@dataclass(frozen=True, order=True)
class Card:
    suit: str
    rank: str


class Deck:
    def __init__(self):
        self._cards = [
            Card(suit, rank)
            for suit in SUITS
            for rank in RANKS
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __setitem__(self, index, value):
        self._cards[index] = value

    def __iter__(self):
        return iter(self._cards)


if __name__ == "__main__":
    deck = Deck()

    print(f"Number of cards: {len(deck)}")

    print("\nFirst card:")
    print(deck[0])

    print("\nFirst five cards:")
    for card in deck[:5]:
        print(card)

    random.shuffle(deck)

    print("\nAfter shuffling (first five cards):")
    for card in deck[:5]:
        print(card)