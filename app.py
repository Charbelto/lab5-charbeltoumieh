import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        country TEXT NOT NULL
        );
        ''')
        conn.commit()
        print("User table created successfully")
    except Exception as e:
        print(f"User table creation failed: {str(e)}")
    finally:
        conn.close()

def insert_user(user):
    inserted_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
                    (user['name'], user['email'], user['phone'], user['address'], user['country']))
        conn.commit()
        inserted_user = get_user_by_id(cur.lastrowid)
    except:
        conn.rollback()
    finally:
        conn.close()
    return inserted_user

user = {
    "name": "Charbel Toumieh",
    "email": "cct08@mail.aub.edu",
    "phone": "81289227",
    "address": "Beirut, Lebanon",
    "country": "Lebanon"
}

def insert_default_user():
    user = {
        "name": "Charbel Toumieh",
        "email": "cct08@mail.aub.edu",
        "phone": "81289227",
        "address": "Beirut, Lebanon",
        "country": "Lebanon"
    }
    
    # Check if the user exists and insert if not
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (user["email"],))
        row = cur.fetchone()
        
        if row:
            print(f"User {user['name']} already exists in the database.")
        else:
            cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
                        (user['name'], user['email'], user['phone'], user['address'], user['country']))
            conn.commit()
            print(f"Inserted user {user['name']} into the database.")
    except Exception as e:
        print(f"Failed to insert default user: {str(e)}")
    finally:
        conn.close()

def get_users():
    users = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        # convert row objects to dictionary
        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["name"] = i["name"]
            user["email"] = i["email"]
            user["phone"] = i["phone"]
            user["address"] = i["address"]
            user["country"] = i["country"]
            users.append(user)
    except:
        users = []
    return users

def get_user_by_id(user_id):
    user = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        # convert row object to dictionary
        user["user_id"] = row["user_id"]
        user["name"] = row["name"]
        user["email"] = row["email"]
        user["phone"] = row["phone"]
        user["address"] = row["address"]
        user["country"] = row["country"]
    except:
        user = {}
    return user

def update_user(user):
    updated_user = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone=?, address = ?, country = ? WHERE user_id=?",
                    (user["name"], user["email"], user["phone"], user["address"], user["country"], user["user_id"]))
        conn.commit()
        # return the user
        updated_user = get_user_by_id(user["user_id"])
    except:
        conn.rollback()
        updated_user = {}
    finally:
        conn.close()
    return updated_user

def delete_user(user_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from users WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()
    return message

if __name__ == "__main__":
    # Create the database table when app starts
    create_db_table()
    insert_default_user()