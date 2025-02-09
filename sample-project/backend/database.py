import sqlite3

DB_NAME ="app.db"

def get_db_connection():
    try:
        conn=sqlite3.connect(DB_NAME)
        conn.row_factory=sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table():
    
    conn=get_db_connection()
    print("connection")
    if conn:
        try:
            cursor=conn.cursor()
            cursor.execute(
                '''
                    CREATE TABLE IF NOT EXISTS users(
                        ID Integer PRIMARY KEY AUTOINCREMENT,
                        name Text NOT NULL UNIQUE
                    )
                '''
            )
            print("Table created successfully!")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.commit()
            conn.close()

def insert_record(name):
    conn=get_db_connection()
    if conn:
        try:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO users(name) VALUES(?)",(name,))
            conn.commit()
            return True,None
        except sqlite3.IntegrityError:
            error_message =f" The name '{name}' already exists in the database"
            return False,error_message
        except sqlite3.Error as e:
            error_message=f"Error inserting record: {e}"
            print(error_message)
            return False,error_message
        finally:
            conn.close()
    
   

def get_users():
    
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows=cursor.fetchall()
    conn.close()
    users=[dict(row)  for row in rows]
    return users

def get_user_details(name):
    conn=get_db_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM users where name = ?",(name,))
    user=cursor.fecthone()
    conn.close()
    return user