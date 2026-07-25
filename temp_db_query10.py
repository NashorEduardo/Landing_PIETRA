import sqlite3
import json

conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get parts from checkpoint writer session
print("=== PARTS FROM ses_06642d58cffekwDwnWK0RQ97Uo (checkpoint-writer) ===")
cursor.execute("""
    SELECT id, message_id, time_created, data
    FROM part
    WHERE session_id = 'ses_06642d58cffekwDwnWK0RQ97Uo'
    ORDER BY time_created
""")
rows = cursor.fetchall()
for row in rows:
    data = json.loads(row[3])
    ptype = data.get('type', 'unknown')
    if ptype == 'text':
        text = data.get('text', '')
        if text.strip():
            print(f"\n[TEXT] msg={row[1]}: {text[:2000]}")
    elif ptype == 'tool':
        tool = data.get('tool', 'unknown')
        state = data.get('state', {})
        print(f"\n[TOOL:{tool}] msg={row[1]}")
        print(f"  Input: {json.dumps(state.get('input', {}))[:500]}")
        out = str(state.get('output', ''))[:500]
        print(f"  Output: {out}")

# Also check all sessions for this project
print("\n\n=== ALL SESSIONS FOR THIS PROJECT ===")
cursor.execute("""
    SELECT id, title, time_created, time_updated
    FROM session
    WHERE project_id = 'af152432-0137-4fc6-8f02-4a2e2a434aee'
    ORDER BY time_created
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
