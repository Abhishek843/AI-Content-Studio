import psycopg2

def save_result(state):
    try:
        conn = psycopg2.connect("postgresql://user:pass@localhost/db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO videos(topic, script, score) VALUES (%s,%s,%s)",
            (state.topic, state.script, state.score)
        )

        conn.commit()
        conn.close()
    except Exception as e:
        print("DB Error:", e)