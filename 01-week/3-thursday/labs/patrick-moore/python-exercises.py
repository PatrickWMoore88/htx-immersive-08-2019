coins = 0
coin_phrase = f"You have {coins} coins."
print(coin_phrase)
coin_question = input("Do you want another? ")
while coin_question == "yes" or coin_question == "YES" or coin_question == "Yes" :
    if coin_question == "yes" or coin_question == "YES" or coin_question == "Yes" :
        coins = coins + 1
        coin_phrase = f"You have {coins} coins."
        print(coin_phrase)
        coin_question= input("Do you want another? ")
    else:
        break
print("Bye")


