import sqlite3
conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get table schemas
print("=== TABLE SCHEMAS ===")
for table in ['session', 'message', 'part', 'task', 'task_event', 'project']:
    cursor.execute(f"PRAGMA table_info({table})")
    cols = cursor.fetchall()
    print(f"\n{table}:")
    for c in cols:
        print(f"  {c}")

# Get projects
print("\n=== PROJECTS ===")
cursor.execute("SELECT * FROM project")
print(cursor.fetchall())

# Get sessions
print("\n=== SESSIONS ===")
cursor.execute("SELECT * FROM session")
rows = cursor.fetchall()
for r in rows:
    print(r)

conn.close()
