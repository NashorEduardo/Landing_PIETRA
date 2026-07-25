import sqlite3
import json

conn = sqlite3.connect(r'C:\Users\Asus\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# Get parts for the build session - focus on text and tool parts
print("=== PARTS FOR ses_06644296afferzuRjVtxvQIWzs ===")
cursor.execute("""
    SELECT p.id, p.message_id, p.time_created, p.data
    FROM part p
    WHERE p.session_id = 'ses_06644296afferzuRjVtxvQIWzs'
    ORDER BY p.time_created
""")
rows = cursor.fetchall()
for row in rows:
    data = json.loads(row[3])
    ptype = data.get('type', 'unknown')
    if ptype == 'text':
        print(f"[TEXT] msg={row[1]}: {data.get('text', '')[:500]}")
    elif ptype == 'tool':
        tool = data.get('tool', 'unknown')
        state = data.get('state', {})
        inp = str(state.get('input', ''))[:300]
        out = str(state.get('output', ''))[:300]
        print(f"[TOOL:{tool}] msg={row[1]}: input={inp}... output={out}...")
    elif ptype == 'step-start':
        print(f"[STEP-START] msg={row[1]}")
    elif ptype == 'step-finish':
        print(f"[STEP-FINISH] msg={row[1]} tokens={data.get('tokens', {})}")
    elif ptype == 'checkpoint':
        print(f"[CHECKPOINT] msg={row[1]}: {str(data)[:200]}")
    else:
        print(f"[{ptype}] msg={row[1]}: {str(data)[:200]}")

conn.close()
