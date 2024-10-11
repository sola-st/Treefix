# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
temp_frame = DataFrame(
    {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
)

assert self.pandasSQL.to_sql(temp_frame, "drop_test_frame") == 4

assert self.pandasSQL.has_table("drop_test_frame")

self.pandasSQL.drop_table("drop_test_frame")

assert not self.pandasSQL.has_table("drop_test_frame")
