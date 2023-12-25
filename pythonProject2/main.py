import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    suits = ['Червы', 'Бубны', 'Крести', 'Пики']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def play_round(player1, player2):
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    print(f"{player1_name}: {card1['rank']} {card1['suit']}   {player2_name}: {card2['rank']} {card2['suit']}")

    if card1['rank'] > card2['rank']:
        print(f"{player1_name} забирает карты!")
        player1.extend([card1, card2])
        return player1_name
    elif card1['rank'] < card2['rank']:
        print(f"{player2_name} забирает карты!")
        player2.extend([card1, card2])
        return player2_name
    else:
        print("Война!")

        war_cards1 = [card1]
        war_cards2 = [card2]

        while True:
            for _ in range(3):
                if player1:
                    war_cards1.append(player1.pop(0))
                if player2:
                    war_cards2.append(player2.pop(0))

            war_card1 = war_cards1[-1]
            war_card2 = war_cards2[-1]

            print(f"{player1_name}: {war_card1['rank']} {war_card1['suit']}   {player2_name}: {war_card2['rank']} {war_card2['suit']}")

            if war_card1['rank'] > war_card2['rank']:
                print(f"{player1_name} забирает карты после войны!")
                player1.extend(war_cards1 + war_cards2)
                #используется для добавления всех элементов из списков war_cards1 и war_cards2 в конец списка player1.
                return player1_name
            elif war_card1['rank'] < war_card2['rank']:
                print(f"{player2_name} забирает карты после войны!")
                player2.extend(war_cards1 + war_cards2)
                return player2_name
            else:
                print("Еще война!")

def play_with_bot():
    global player1_name
    player1_name = input("Введите ваше имя: ")
    global player2_name
    player2_name = "Бот"

    while True:
        deck = create_deck()

        player1 = deck[:26]
        player2 = deck[26:]

        player1_score = 0
        player2_score = 0

        while player1 and player2:
            print(f"{player1_name}:")

            for i, card in enumerate(player1, start=1):
                print(f"{i}. {card['rank']} {card['suit']}")
#enumerate(player1, start=1): Функция enumerate перебирает элементы в player1 и возвращает их вместе с порядковыми номерами.
            choice1 = int(input("Выберите номер карты для выкладывания: "))

            if 1 <= choice1 <= len(player1):
                card1 = player1.pop(choice1 - 1)
            else:
                print(f"{player1_name} проигрывает раунд из-за неверного ввода.")
                player2_score += 26
                break

            print(f"{player2_name}:")

            choice2 = random.randint(1, len(player2))
            card2 = player2.pop(choice2 - 1)
            print(f"{player2_name} выбрал карту: {card2['rank']} {card2['suit']}")

            winner = play_round([card1], [card2])

            if winner == player1_name:
                player1_score += 1
            elif winner == player2_name:
                player2_score += 1

            print(f"Очки {player1_name}: {player1_score}   Очки {player2_name}: {player2_score}")

        if not player1:
            print(f"{player2_name} выиграл раунд!")
        else:
            print(f"{player1_name} выиграл раунд!")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print("До свидания!")
            break

def play_1vs1():
    global player1_name
    player1_name = input("Введите имя игрока 1: ")
    global player2_name
    player2_name = input("Введите имя игрока 2: ")

    while True:
        deck = create_deck()

        player1 = deck[:26]
        player2 = deck[26:]

        player1_score = 0
        player2_score = 0

        while player1 and player2:
            # Убрана строка с input
            print(f"{player1_name}:")

            for i, card in enumerate(player1, start=1):
                print(f"{i}. {card['rank']} {card['suit']}")
            # enumerate(player1, start=1): Функция enumerate перебирает элементы в player1 и возвращает их вместе с порядковыми номерами.

            choice1 = int(input("Выберите номер карты для выкладывания: "))

            if 1 <= choice1 <= len(player1):
                card1 = player1.pop(choice1 - 1)
            else:
                print(f"{player1_name} проигрывает раунд из-за неверного ввода.")
                player2_score += 26
                break

            print(f"{player2_name}:")

            for i, card in enumerate(player2, start=1):
                print(f"{i}. {card['rank']} {card['suit']}")

            choice2 = int(input("Выберите номер карты для выкладывания: "))

            if 1 <= choice2 <= len(player2):
                card2 = player2.pop(choice2 - 1)
            else:
                print(f"{player2_name} проигрывает раунд из-за неверного ввода.")
                player1_score += 26
                break

            winner = play_round([card1], [card2])

            if winner == player1_name:
                player1_score += 1
            elif winner == player2_name:
                player2_score += 1

            print(f"Очки {player1_name}: {player1_score}   Очки {player2_name}: {player2_score}")

        if not player1:
            print(f"{player2_name} выиграл раунд!")
        else:
            print(f"{player1_name} выиграл раунд!")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            print("До свидания!")
            break

def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Играть с ботом")
        print("2. Играть 1 на 1")
        print("3. Выйти")

        choice = input("Выберите режим (1, 2 или 3): ")

        if choice == '1':
            play_with_bot()
        elif choice == '2':
            play_1vs1()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main_menu()
