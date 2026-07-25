import sqlite3
import json

conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get ALL tool calls from build session
print("=== ALL TOOL CALLS FROM BUILD SESSION ===")
cursor.execute("""
    SELECT p.id, p.message_id, p.time_created, p.data
    FROM part p
    WHERE p.session_id = 'ses_06644296afferzuRjVtxvQIWzs'
      AND json_extract(p.data, '$.type') = 'tool'
    ORDER BY p.time_created
""")
rows = cursor.fetchall()
for row in rows:
    data = json.loads(row[3])
    tool = data.get('tool', 'unknown')
    state = data.get('state', {})
    inp = state.get('input', {})
    out = str(state.get('output', ''))[:500]
    print(f"\nTool: {tool}")
    print(f"Input: {json.dumps(inp)[:500]}")
    print(f"Output: {out}")

# Get tasks for this session
print("\n=== TASKS ===")
cursor.execute("SELECT * FROM task WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs'")
tasks = cursor.fetchall()
for t in tasks:
    print(t)

# Get task events
print("\n=== TASK EVENTS ===")
cursor.execute("SELECT * FROM task_event WHERE session_id = 'ses_06644296afferzuRjVtxvQIWzs'")
events = cursor.fetchall()
for e in events:
    print(e)

conn.close()
