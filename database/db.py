import psycopg2

DB_HOST = '127.0.0.1'
DB_USER = 'postgres'
DB_PASSWORD = '06062014AA_ss'
DB_NAME = 'AvatarMe'
DB_PORT = '5432'

async def sql_start():
    global connection
    global cursor
    connection = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, port=DB_PORT)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user_data(user_id INTEGER PRIMARY KEY, username TEXT, name TEXT, surname TEXT, date TEXT);')
    cursor.execute('CREATE TABLE IF NOT EXISTS user_tarif(user_id INTEGER PRIMARY KEY, tries INTEGER);')
    cursor.execute('SELECT version();')
    print(cursor.fetchone())

async def sql_add_user(user_id, username, name, surname, date):
    try:
        cursor.execute(f"INSERT INTO user_data(user_id, username, name, surname, date) VALUES({user_id}, '{username}', '{name}', '{surname}', '{date}')")
    except Exception as ex:
        print('[DATABASE] USER ALREADY EXISTS', ex)
        user_is_registered = True
        return user_is_registered
    finally:
        cursor.execute(f'INSERT INTO user_tarif(user_id, tries) VALUES({user_id}, 1);')

async def sql_add_10(user_id):
    cursor.execute(f'UPDATE user_tarif SET tries = 10')

async def sql_add_25(user_id):
    cursor.execute(f'UPDATE user_tarif SET tries = 25')

async def sql_add_50(user_id):
    cursor.execute(f'UPDATE user_tarif SET tries = 50')

async def sql_add_100(user_id):
    cursor.execute(f'UPDATE user_tarif SET tries = 100')

async def sql_get_tries(user_id):
    cursor.execute(f'SELECT tries FROM user_tarif WHERE user_id = "{user_id}"')
    result = cursor.fetchone()
    return result

async def sql_update_tries(user_id):
    cursor.execute(f"SELECT tries FROM user_tarif WHERE user_id = '{user_id}'")
    result = cursor.fetchone()[0]
    if result != 0:
        result = result - 1
        cursor.execute(f"UPDATE user_tarif SET tries = {result}")
        return True
    else:
        return False
# cursor.close()
# connection.close()