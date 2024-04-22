import psycopg2
from config import load_config

# Функция для подключения к базе данных
def connect(config):
    try:
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except psycopg2.DatabaseError as error:
        print(f'Error connecting to PostgreSQL: {error}')

# Функция для вставки данных игры в базу данных
def insert_game_data(conn, user_id, score, level):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
        conn.commit()
        cur.close()
        print('Game data inserted successfully.')
    except psycopg2.DatabaseError as error:
        print(f'Error inserting game data: {error}')

if __name__ == '__main__':
    # Загрузка конфигурации подключения к базе данных из файла
    config = load_config()

    # Подключение к базе данных
    conn = connect(config)

    # Предположим, что у вас есть значения user_id, score и level, которые вы хотите сохранить
    user_id = 1  # Пример
    score = 100  # Пример
    level = 3  # Пример

    # Вставка данных игры в базу данных
    insert_game_data(conn, user_id, score, level)

    # Закрытие соединения с базой данных
    conn.close()
