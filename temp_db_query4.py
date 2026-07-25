import sqlite3
conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get messages for Landing_PIETRA sessions
print("=== MESSAGES FOR ses_06644296afferzuRjVtxvQIWzs ===")
cursor.execute("""
    SELECT id, agent_id, time_created, substr(data, 1, 800) 
    FROM message 
    WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs' 
    ORDER BY time_created
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n=== MESSAGES FOR ses_0664428c0ffehsV5o8vclbRhup ===")
cursor.execute("""
    SELECT id, agent_id, time_created, substr(data, 1, 800) 
    FROM message 
    WHERE session_id = 'ses_0664428c0ffehsV5o8vclbRhup' 
    ORDER BY time_created
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
