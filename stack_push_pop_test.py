import main

def test_Deck():
    deck = main.Deck()
    deck.push(1)
    deck.push(2)
    deck.push(3)
    deck.pop()
    assert deck.cards == [1,2]