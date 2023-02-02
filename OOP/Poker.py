"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards = []
        self.hand_type = None

    def str_to_int(self):
        """Convert string values to integers."""
        for i in range(len(self.cards)):
            if self.cards[i].value == "J":
                self.cards[i].value = 11
            if self.cards[i].value == "Q":
                self.cards[i].value = 12
            if self.cards[i].value == "K":
                self.cards[i].value = 13
            if self.cards[i].value == "A":
                self.cards[i].value = 14
            if type(self.cards[i].value) is str:
                self.cards[i].value = int(self.cards[i].value)

    def int_to_str(self):
        """Convert integer values to strings."""
        for i in range(len(self.cards)):
            if self.cards[i].value == 11:
                self.cards[i].value = "J"
            if self.cards[i].value == 12:
                self.cards[i].value = "Q"
            if self.cards[i].value == 13:
                self.cards[i].value = "K"
            if self.cards[i].value == 14:
                self.cards[i].value = "A"
            if type(self.cards[i].value) is int:
                self.cards[i].value = str(self.cards[i].value)

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        can_add = True
        if len(self.cards) >= 5:
            can_add = False
        for i in range(len(self.cards)):
            if (card.value == self.cards[i].value) and (card.suit == self.cards[i].suit):
                can_add = False
        if card.value not in Hand.values or card.suit not in Hand.suits:
            can_add = False
        return can_add

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card) is True:
            self.cards.append(card)

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        if card in self.cards:
            return True
        else:
            return False

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card) is True:
            self.cards.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.cards

    def is_straight(self):
        """
        Determine if the hand is a straight.

        Astraight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.
        Examples:
        4 5 6 7 8
        K J 10 Q A
        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        straight_bool = False
        self.str_to_int()
        self.cards.sort(key=lambda x: x.value)
        if len(self.cards) == 5:
            if self.cards[0].value == self.cards[1].value - 1 == self.cards[2].value - 2 == self.cards[3].value - 3 == self.cards[4].value - 4:
                straight_bool = True
        self.int_to_str()
        return straight_bool

    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        flush_bool = False
        if len(self.cards) == 5:
            if self.cards[0].suit == self.cards[1].suit == self.cards[2].suit == self.cards[3].suit == self.cards[4].suit:
                flush_bool = True
        return flush_bool

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        if self.is_straight() and self.is_flush():
            return True
        else:
            return False

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        full_house_bool = False
        self.str_to_int()
        self.cards.sort(key=lambda x: x.value)
        if self.cards[0].value == self.cards[1].value == self.cards[2].value and self.cards[3].value == self.cards[4].value or self.cards[0].value == self.cards[1].value and self.cards[2].value == self.cards[3].value == self.cards[4].value:
            full_house_bool = True
        self.int_to_str()
        return full_house_bool

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        four_of_a_kind_bool = False
        self.str_to_int()
        self.cards.sort(key=lambda x: x.value)
        if self.cards[0].value == self.cards[1].value == self.cards[2].value == self.cards[3].value or self.cards[1].value == self.cards[2].value == self.cards[3].value == self.cards[4].value:
            four_of_a_kind_bool = True
        self.int_to_str()
        return four_of_a_kind_bool

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        three_of_a_kind_bool = False
        self.str_to_int()
        self.cards.sort(key=lambda x: x.value)
        if self.cards[0].value == self.cards[1].value == self.cards[2].value or self.cards[1].value == self.cards[2].value == self.cards[3].value or self.cards[2].value == self.cards[3].value == self.cards[4].value:
            three_of_a_kind_bool = True
        self.int_to_str()
        return three_of_a_kind_bool

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        pair_bool = False
        self.str_to_int()
        self.cards.sort(key=lambda x: x.value)
        if self.cards[0].value == self.cards[1].value or self.cards[1].value == self.cards[2].value or self.cards[2].value == self.cards[3].value or self.cards[3].value == self.cards[4].value:
            pair_bool = True
        self.int_to_str()
        return pair_bool

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        if len(self.cards) == 5:
            if self.is_straight_flush():
                return "straight flush"
            elif self.is_flush():
                return "flush"
            elif self.is_straight():
                return "straight"
            elif self.is_full_house():
                return "full house"
            elif self.is_four_of_a_kind():
                return "four of a kind"
            elif self.is_three_of_a_kind():
                return "three of a kind"
            elif self.is_pair():
                return "pair"
            else:
                return "high card"
        else:
            return None

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        if len(self.cards) < 5:
            return f"I'm holding {self.cards}"
        else:
            return f"I got a {self.get_hand_type()} with cards: {self.cards}"


if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "straight"

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"), Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"), Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "four of a kind"