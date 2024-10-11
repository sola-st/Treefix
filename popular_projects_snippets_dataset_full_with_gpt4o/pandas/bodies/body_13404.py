# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import inspect

temp_conn = self.connect()
temp_frame = DataFrame(
    {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
)
pandasSQL = sql.SQLDatabase(temp_conn)
assert pandasSQL.to_sql(temp_frame, "temp_frame") == 4

insp = inspect(temp_conn)
assert insp.has_table("temp_frame")

pandasSQL.drop_table("temp_frame")
assert not insp.has_table("temp_frame")
