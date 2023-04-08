"""
Дано положительное целочисленное 2-х байтное число. Нужно найти значение, которое будет, если поменять байты местами.
"""


def fun(number: int):
    """
    function for permuting bytes of a two-byte number
    :param number: two-byte number
    :return: None
    """
    res = ((number & 0x00ff) << 8) | ((number & 0xFF00) >> 8)
    print(f'result: {res}')


if __name__ == "__main__":
    try:
        fun(number=int(input("enter a single two-byte number: ")))
    except ValueError:
        print('something went wrong enter the correct data!!!')
