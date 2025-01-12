import main

def test_stack():
    deck = main.Deck()
    deck.push(1)
    deck.pop()
    assert deck.cards == []