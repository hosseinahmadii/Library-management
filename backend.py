import sqlite3
## INTEGER PRIMARY KEY  --> خودش میاد مدیریت میکنه و یه عدد انخاب میکنه و یه دونه یه دونه اضافه میکنه

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text, year INTEGER, isbn INTEGER )")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn)) ## نال اول برای اینکه خود کامپیوتر قرار بود مقدارش هندل بکنه بقیه همه به ترتیب داخل یک توپل قرار می دیم اگر قفط یکی بود آخرش یک کاما بزار که بفهمه تاپل هست
    conn.commit()
    conn.close()


def view(): ## میخوایم همه آیتم هایی که داخل دیتا بیس هستش دریافت بکنم
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()    ## میاد یک لیست که داخلش تاپل هست بر میگردونه
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
# insert("csharp", "sara", 2015, 2565)
# delete(5)
# update(1, "python ebook", "mohammad", 2020, 56458)
# print(view())
