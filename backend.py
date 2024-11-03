import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREAT TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text, year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isnb):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (NULL ,?,?,?,?)",(title, author,year,isnb))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows



connect()
insert("")
   