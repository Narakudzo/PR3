import random


class Player(object):

    def __init__(self, money):

        """Constructor"""

        self.money = float(money)

    def check_money_for_final(self):

        if self.money >= 1000:

            return False

        else:

            return True


def work_distribution_of_leaflets(money):
    money_add = 7

    print("Было заработано на раздаче листовок: ", money_add, "\nВсего денег: ", money + money_add)

    return money + money_add


def work_programming(money):
    money_add = 15

    print("Было заработано на программировании: ", money_add, "\nВсего денег: ", money + money_add)

    return money + money_add


def lucky_rate(money):
    lucky = random.randint(0, 100)

    if lucky >= 50:

        money_add = money * 0.5

        print("Было заработано на ставке: ", money_add, "\nВсего денег: ", money + money_add)

    else:

        money_add = 0

        money = 0

        print("Всё было потеряно!\nВсего денег: ", money + money_add)

    return money + money_add


if __name__ == "__main__":

    player = Player(200.0)

    while player.check_money_for_final():

        print("Количество денег: ", player.money)

        print("1) Раздавать листовки \n2) Программировать \n3) Сыграть ставку\n")

        ans = input()

        if ans == '1':

            player.money = work_distribution_of_leaflets(player.money)

        elif ans == '2':

            player.money = work_programming(player.money)

        elif ans == '3':

            player.money = lucky_rate(player.money)

        if player.money == 0.0:
            print("Вы проиграли")

            break

        if not (player.check_money_for_final()):
            print("Вы победили!")

            break