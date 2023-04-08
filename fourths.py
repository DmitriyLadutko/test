import json
from datetime import datetime as dt
from pathlib import Path
import os
import logging

"""
Дан json файл. Найдите в нём все поля "updated" и поменяйте значение на текущие дату и время в формате ISO 8601.
"""

_logger = logging.getLogger(__name__)


def create_file():
    """
    function to create a file if it does not exist
    :return:
    """
    if not os.path.isfile('data.json'):
        file = Path('data.json')
        file.touch(exist_ok=True)


def file_handling():
    """
    file function, data validation and writing
    :return:
    """
    with open('data.json', 'r') as file:
        try:
            data = json.load(file)
            for key, val in data.items():
                if isinstance(val, dict) and 'updated' in val:
                    data[key][val['updated']] = dt.utcnow().isoformat()

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=2)

        except json.decoder.JSONDecodeError:
            _logger.critical('CRITICAL: json file is not walid')


if __name__ == "__main__":
    create_file()
    file_handling()
