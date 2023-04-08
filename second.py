"""
    В N корзинах находятся золотые монеты. Корзины пронумерованы числами от 1 до N. Во всех корзинах, кроме одной,
монеты весят по w граммов. В одной корзине монеты фальшивые и весят w–d граммов. Волшебник берет 1 монету из первой
корзины, 2 монеты из второй корзины, и так далее, и, наконец, N-1 монету из (N-1)-й корзины. Из N-й корзины он не
берет ничего. Он взвешивает взятые монеты и сразу указывает на корзину с фальшивыми монетами. Напишите программу,
которая сможет выполнять такое волшебство. Дано: четыре целых числа: N, w, d и P – суммарный вес отобранных монет.
Найти номер корзины с фальшивыми монетами.
"""


def fun(n: int, w: int, d: int, p: int) -> int():
    """
    function to find the number of the basket with counterfeit coins
    :param n: the number of baskets
    :param w: the weight of the coins in most baskets
    :param d: the weight difference of counterfeit coins
    :param p: the total weight of selected coins
    :return:
    """
    try:
        total_weight = (n * (n + 1) // 2) * w - p  # total weight
        fake_basket = (total_weight + d) // (n - 1)  # fake basket
        print(f'fake basket: {fake_basket}')
    except (ZeroDivisionError, UnboundLocalError):
        print('something went wrong enter the correct data!!!')


if __name__ == "__main__":
    try:
        fun(
            n=int(input("enter the number of baskets: ")),
            w=int(input("enter the weight of the coins in most baskets: ")),
            d=int(input("enter the weight difference of counterfeit coins: ")),
            p=int(input("enter the total weight of selected coins: "))
        )
    except ValueError:
        print('something went wrong enter the correct data!!!')
