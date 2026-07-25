import sqlite3
import json

conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get the full last message from build session
print("=== LAST MESSAGE (final response) from build session ===")
cursor.execute("""
    SELECT id, data FROM part
    WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs'
      AND json_extract(data, '$.type') = 'text'
    ORDER BY time_created DESC
    LIMIT 1
""")
row = cursor.fetchone()
if row:
    data = json.loads(row[1])
    print(f"Full text: {data.get('text', '')}")

# Also get any write/edit tool calls
print("\n=== WRITE/EDIT TOOL CALLS ===")
cursor.execute("""
    SELECT p.id, p.message_id, p.data
    FROM part p
    WHERE p.session_id = 'ses_06644296afferzuRjVtxvQIWzs'
      AND json_extract(p.data, '$.type') = 'tool'
      AND json_extract(p.data, '$.tool') IN ('write', 'edit', 'patch')
    ORDER BY p.time_created
""")
rows = cursor.fetchall()
for row in rows:
    data = json.loads(row[2])
    state = data.get('state', {})
    print(f"\nTool: {data.get('tool')}")
    print(f"Input: {json.dumps(state.get('input', {}), indent=2)[:1500]}")
    out = str(state.get('output', ''))[:500]
    print(f"Output preview: {out}")

conn.close()
