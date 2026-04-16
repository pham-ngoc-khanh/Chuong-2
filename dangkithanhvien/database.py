import sqlite3

def init_db():
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ho TEXT NOT NULL,
            ten TEXT NOT NULL,
            email_phone TEXT NOT NULL,
            password TEXT NOT NULL,
            birthday TEXT NOT NULL,
            gender TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_member(ho, ten, email_phone, password, birthday, gender):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO members (ho, ten, email_phone, password, birthday, gender)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (ho, ten, email_phone, password, birthday, gender))
    conn.commit()
    conn.close()

def get_all_members():
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_member(member_id):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
    conn.commit()
    conn.close()

def update_member(member_id, ho, ten, email_phone, password, birthday, gender):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE members 
        SET ho=?, ten=?, email_phone=?, password=?, birthday=?, gender=?
        WHERE id=?
    ''', (ho, ten, email_phone, password, birthday, gender, member_id))
    conn.commit()
    conn.close()
