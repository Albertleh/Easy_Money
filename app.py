import random as rn

def roulette(balance, bet, color):
    """
    This funcion simulates a spin of Classic American Roulette
    Input : Current balance in $, the amount you would like to bet,
            and your lucky color 
    Output : The updated balance after one game
    """
    balance -=bet
    chosen_color = ""
    number = rn.randint(0,32)

    if number == 0:
        chosen_color = 'Green'
    elif number % 2 == 0:
        chosen_color = 'Black'
    else:
        chosen_color = 'Red'

    if chosen_color == color:
        #print(number, ": It's {}, you win!".format(chosen_color))
        if chosen_color == 'Green':
            bet *= 35
        else:
            bet *= 2
    else:
        #print(number, ": It's {}, you loose!".format(chosen_color))
        bet = 0
    balance += bet
    return balance


starting_money = 100

for i in range(0,15): # Loops for every price point

    tries = 5000

    profit_chance = 0
    profit = 0


    for n in range(0,tries): # Loops for confident results

        beforebet, balance = starting_money, starting_money
        bet = 5
        color = "Red"

        for i in range(0, 150): # Simulates 150 Bets
            if balance < bet:
                #print("\nBROKE !")
                break
            else:
                balance = roulette(balance, bet, color)
                if balance < beforebet:
                    bet *= 2
                else:
                    bet = 5
                beforebet = balance

        if starting_money < balance:
            #print("Profit! ")
            profit += 1
        else:
            pass
            #print("Loss!")

    profit_chance = profit/tries*100
    print("\nUsing the method with",str(starting_money)+"$ Balance the chance of winning equals {}%".format(round(profit_chance,2)))
    starting_money *= 2

