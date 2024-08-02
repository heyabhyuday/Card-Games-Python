import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

random.shuffle(deck) 

def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card) 

def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10

    return value 

player_hand = []
dealer_hand = []

deal_card(deck, player_hand)
deal_card(deck, player_hand)
deal_card(deck, dealer_hand)
deal_card(deck, dealer_hand)

has_player_busted = False 

while True:
    print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
    print(f'Dealer hand: {dealer_hand[0]}, face down')

    if calculate_hand_value(player_hand) > 21:
        print('Player busts! Dealer wins!')
        has_player_busted = True
        break

    action = input('Do you want to hit or stand? ')

    if action.lower() == 'hit':
        deal_card(deck, player_hand)
    elif action.lower() == 'stand':
        break
    else:
        print('Invalid input. Please try again')
        continue

if not has_player_busted:
    print(f'Player hand: {player_hand} ({calculate_hand_value(player_hand)})')
    print(f'Dealer hand: {dealer_hand} ({calculate_hand_value(dealer_hand)})')

    dealer_value = calculate_hand_value(dealer_hand)
    while dealer_value < 15:
        print('Dealer total is less than 15. Dealer draws again.')
        deal_card(deck, dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)
        print(f'Dealer hand now: {dealer_hand} ({calculate_hand_value(dealer_hand)})')

    if calculate_hand_value(player_hand) > 21:
        print('Player busts! Dealer wins!')
    elif calculate_hand_value(dealer_hand) > 21:
        print('Dealer busts! Player wins!')
    elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        print('Player wins!')
    elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
        print('Dealer wins!')
    else:
        print('Push!') 




