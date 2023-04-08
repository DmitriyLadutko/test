import requests
from collections import Counter
import logging

"""
    Необходимо получить HTML-код страницы www.python.org, и посчитать сколько раз какие символы встречается в коде
страницы. Формат вывода определяете сами. Вывод программы разместите в файле readme.md.
"""
_logger = logging.getLogger(__name__)


def fun():
    """
    function of parsing the page and counting the number of elements is completed without decomposition
    :return:
    """
    url = "https://www.python.org/"
    response = requests.get(url)
    if response.status_code == 200:
        html_code = response.content.decode('utf-8')
        char_counts = Counter(html_code)  # TODO can be decomposed
        for char, count in char_counts.most_common():
            with open('readme.md', 'a') as f:
                f.write(f'{char} - {count}')
    else:
        _logger.error(f'error when connecting to - {url}')


if __name__ == "__main__":
    fun()
