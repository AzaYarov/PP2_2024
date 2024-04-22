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

# Функция для создания таблицы результатов игры
def create_game_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                score INT NOT NULL,
                level INT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        print('Game table created successfully.')
    except psycopg2.DatabaseError as error:
        print(f'Error creating game table: {error}')

if __name__ == '__main__':
    # Загрузка конфигурации подключения к базе данных из файла
    config = load_config()

    # Подключение к базе данных
    conn = connect(config)

    # Создание таблицы результатов игры
    create_game_table(conn)

    # Закрытие соединения с базой данных
    conn.close()
