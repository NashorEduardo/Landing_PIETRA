import sqlite3
import json

conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get ALL parts from build session with their full data
print("=== ALL PARTS FROM BUILD SESSION (detailed) ===")
cursor.execute("""
    SELECT id, message_id, time_created, data
    FROM part
    WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs'
    ORDER BY time_created
""")
rows = cursor.fetchall()
for row in rows:
    data = json.loads(row[3])
    ptype = data.get('type', 'unknown')
    if ptype == 'patch':
        print(f"\n[PATCH] msg={row[1]}")
        print(f"  Hash: {data.get('hash')}")
        print(f"  Files: {data.get('files')}")
        print(f"  Full data: {json.dumps(data, indent=2)[:2000]}")
    elif ptype == 'text':
        text = data.get('text', '')
        if text.strip():
            print(f"\n[TEXT] msg={row[1]}: {text[:300]}")

conn.close()
