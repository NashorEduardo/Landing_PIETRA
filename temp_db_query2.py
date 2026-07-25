import sqlite3
conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get sessions
print("=== SESSIONS ===")
cursor.execute("SELECT id, time_created, data FROM session ORDER BY time_created DESC LIMIT 10")
sessions = cursor.fetchall()
for s in sessions:
    print(s)

# Get messages with user role (actual user requests)
print("\n=== USER MESSAGES ===")
cursor.execute("SELECT id, session_id, time_created, substr(data, 1, 500) FROM message WHERE json_extract(data, '$.role') = 'user' ORDER BY time_created DESC LIMIT 20")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
