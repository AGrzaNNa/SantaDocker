from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def is_table_exists(table_name):
    cursor.execute("PRAGMA table_info({})".format(table_name))
    return cursor.fetchall()

@app.post("/package")
async def post_package(name: str, elfID: int):
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS packages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                elfID INTEGER,
                name TEXT,
                status INTEGER DEFAULT 0
            )''')

    cursor.execute('INSERT INTO packages (elfID, name) VALUES (?, ?)', (elfID, name))
    conn.commit()
    return {"message": "Package added successfully"}


@app.put("/package")
async def put_package(pack_id: int, status: bool):
    if is_table_exists('packages'):
        cursor.execute('UPDATE packages SET status = ? WHERE id = ?', (int(status), pack_id))
        conn.commit()
        return {"message": "Package status updated successfully"}
    else:
        return {"message": "Table 'packages' does not exist"}

@app.get("/package")
async def get_package(pack_id: int):
    if is_table_exists('packages'):
        result = cursor.execute("SELECT * FROM packages WHERE id = ?", (pack_id,))
        data = result.fetchall()
        conn.commit()
        if data:
            return {"message": data}
        else:
            return {"message": "No package with that ID"}
    else:
        return {"message": "Table 'packages' does not exist"}

@app.delete("/package")
async def delete_packages():
    if is_table_exists('packages'):
        status = 1
        cursor.execute("DELETE FROM packages WHERE status = ?", (status,))
        conn.commit()
        return {"message": "Deleted all delivered packages"}
    else:
        return {"message": "Table 'packages' does not exist"}

@app.post("/elfs")
async def post_elf(elf_name: str):
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS elfs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    vacation INTEGER DEFAULT 0,
                    daternity INTEGER DEFAULT 0
                )
            ''')
    cursor.execute('INSERT INTO elfs (name) VALUES (?)', (elf_name,))
    conn.commit()
    return {"message": "Elf added successfully"}

@app.put("/elfs")
async def put_elf(elfID: int, vacation: bool, daternity: bool):
    if is_table_exists('elfs'):
        cursor.execute('UPDATE elfs SET vacation = ?, daternity = ? WHERE id = ?', (int(vacation), int(daternity), elfID))
        conn.commit()
        return {"message": "Elf information updated successfully"}
    else:
        return {"message": "Table 'elfs' does not exist"}

@app.get("/elfs")
async def get_elf(elfID: int):
    if is_table_exists('elfs'):
        result = cursor.execute("SELECT * FROM elfs WHERE id = ?", (elfID,))
        data = result.fetchall()
        conn.commit()
        if data:
            return {"message": data}
        else:
            return {"message": "No elf with that ID"}
    else:
        return {"message": "Table 'elfs' does not exist"}

@app.delete("/elfs")
async def delete_elf(elfID: int):
    if is_table_exists('elfs'):
        cursor.execute("DELETE FROM elfs WHERE id = ?", (elfID,))
        conn.commit()
        return {"message": "Elf successfully fired"}
    else:
        return {"message": "Table 'elfs' does not exist"}