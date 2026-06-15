from load.db_connection import get_engine

engine = get_engine()

try:
    with engine.connect() as conn:
        print("Database Connected Successfully!")
except Exception as e:
    print("Connection Failed")
    print(e)
