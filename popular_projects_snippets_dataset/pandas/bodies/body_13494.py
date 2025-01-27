# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
df_if_exists_1 = DataFrame({"col1": [1, 2], "col2": ["A", "B"]})
df_if_exists_2 = DataFrame({"col1": [3, 4, 5], "col2": ["C", "D", "E"]})
table_name = "table_if_exists"
sql_select = f"SELECT * FROM {table_name}"

msg = "'notvalidvalue' is not valid for if_exists"
with pytest.raises(ValueError, match=msg):
    sql.to_sql(
        frame=df_if_exists_1,
        con=sqlite_buildin,
        name=table_name,
        if_exists="notvalidvalue",
    )
self.drop_table(table_name, sqlite_buildin)

# test if_exists='fail'
sql.to_sql(
    frame=df_if_exists_1, con=sqlite_buildin, name=table_name, if_exists="fail"
)
msg = "Table 'table_if_exists' already exists"
with pytest.raises(ValueError, match=msg):
    sql.to_sql(
        frame=df_if_exists_1,
        con=sqlite_buildin,
        name=table_name,
        if_exists="fail",
    )
# test if_exists='replace'
sql.to_sql(
    frame=df_if_exists_1,
    con=sqlite_buildin,
    name=table_name,
    if_exists="replace",
    index=False,
)
assert tquery(sql_select, con=sqlite_buildin) == [(1, "A"), (2, "B")]
assert (
    sql.to_sql(
        frame=df_if_exists_2,
        con=sqlite_buildin,
        name=table_name,
        if_exists="replace",
        index=False,
    )
    == 3
)
assert tquery(sql_select, con=sqlite_buildin) == [(3, "C"), (4, "D"), (5, "E")]
self.drop_table(table_name, sqlite_buildin)

# test if_exists='append'
assert (
    sql.to_sql(
        frame=df_if_exists_1,
        con=sqlite_buildin,
        name=table_name,
        if_exists="fail",
        index=False,
    )
    == 2
)
assert tquery(sql_select, con=sqlite_buildin) == [(1, "A"), (2, "B")]
assert (
    sql.to_sql(
        frame=df_if_exists_2,
        con=sqlite_buildin,
        name=table_name,
        if_exists="append",
        index=False,
    )
    == 3
)
assert tquery(sql_select, con=sqlite_buildin) == [
    (1, "A"),
    (2, "B"),
    (3, "C"),
    (4, "D"),
    (5, "E"),
]
self.drop_table(table_name, sqlite_buildin)
