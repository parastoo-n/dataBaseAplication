import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text, year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isnb):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author,year,isnb))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isnb=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isnb))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isnb):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=? , author=? , year=? , isbn=? WHERE id=?", (title,author,year,isnb,id))
    conn.commit()
    conn.close()
    
connect()
# insert("python ebook","mohammad",2015,2565)
# insert("csharp","sara",2015,2565)
# print(view())
# print(search(author="sara"))
# delete(2)
# update(1,"new book title","new author name",2020,56458)