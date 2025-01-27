# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH8624
# test that categorical gets written correctly as dense column
df = DataFrame(
    {
        "person_id": [1, 2, 3],
        "person_name": ["John P. Doe", "Jane Dove", "John P. Doe"],
    }
)
df2 = df.copy()
df2["person_name"] = df2["person_name"].astype("category")

df2.to_sql("test_categorical", self.conn, index=False)
res = sql.read_sql_query("SELECT * FROM test_categorical", self.conn)

tm.assert_frame_equal(res, df)
