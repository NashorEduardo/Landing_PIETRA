import sqlite3
conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", tables)

# Check sessions
cursor.execute("SELECT id, session_id, time_created, substr(data, 1, 300) FROM message WHERE session_id LIKE 'ses_%' ORDER BY time_created DESC LIMIT 20")
rows = cursor.fetchall()
print("\nRecent messages:")
for row in rows:
    print(row)

conn.close()
