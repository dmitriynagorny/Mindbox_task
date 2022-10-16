import logging
import pandas as pd
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Counter')

# Input data
count_clients = 7412567
n_customers = 7412567
n_first_id = 7110390


# We determine the group number
def n_groups(id: int):
    group = sum(map(int, str(id)))

    return group


# Create table
def create_table(dict_gr: dict):
    result = pd.DataFrame.from_dict(dict_gr, orient='index', columns=['Число покупателей']).sort_index()

    return result


# Function of counting buyers in groups (numbering from a given number)
def count_groups(n_customers: int, n_first_id: int):
    dict_group = {}
    logger.info(f'Общее число покупателе - {n_customers - n_first_id}')

    if n_first_id == 0:
        logger.info(f'Нумерация начинается с 0')
    else:
        logger.info(f'Нумерация начинается с {n_first_id}')

    for i in range(n_first_id, n_customers+1):
        a = n_groups(i)
        if a not in dict_group:
            dict_group[a] = 1
        else:
            dict_group[a] += 1

    return dict_group


def run(n_customers, n_first_id = 0):
    start = time.time()
    table = create_table(count_groups(n_customers, n_first_id))
    end = time.time()
    logger.info(f'Время выполнения - {end - start} секунд')

    return table


if __name__ == '__main__':
    print(f'Таблица с числом покупателей в группах:\n{run(n_customers)}')