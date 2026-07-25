import sqlite3
import json

conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get the session summary (diffs) for the build session
print("=== SESSION SUMMARY ===")
cursor.execute("""
    SELECT summary_additions, summary_deletions, summary_files, summary_diffs
    FROM session
    WHERE id = 'ses_06644296afferzuRjVtxvQIWzs'
""")
row = cursor.fetchone()
if row:
    print(f"Additions: {row[0]}")
    print(f"Deletions: {row[1]}")
    print(f"Files: {row[2]}")
    print(f"Diffs: {str(row[3])[:2000]}")

# Get the user's actual message (the build task)
print("\n=== USER MESSAGE ===")
cursor.execute("""
    SELECT data FROM part
    WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs'
      AND json_extract(data, '$.type') = 'text'
    ORDER BY time_created
    LIMIT 1
""")
row = cursor.fetchone()
if row:
    data = json.loads(row[0])
    print(f"Text: {data.get('text', '')[:1000]}")

# Check for checkpoint parts
print("\n=== CHECKPOINT PARTS ===")
cursor.execute("""
    SELECT id, message_id, data
    FROM part
    WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs'
      AND json_extract(data, '$.type') = 'checkpoint'
    ORDER BY time_created
""")
rows = cursor.fetchall()
for row in rows:
    data = json.loads(row[2])
    print(f"Checkpoint: {str(data)[:1000]}")

conn.close()
