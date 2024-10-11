# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# gets a DBAPI connection that can provide a cursor
dbapi_conn = conn.connection
with dbapi_conn.cursor() as cur:
    s_buf = StringIO()
    writer = csv.writer(s_buf)
    writer.writerows(data_iter)
    s_buf.seek(0)

    columns = ", ".join([f'"{k}"' for k in keys])
    if table.schema:
        table_name = f"{table.schema}.{table.name}"
    else:
        table_name = table.name

    sql_query = f"COPY {table_name} ({columns}) FROM STDIN WITH CSV"
    cur.copy_expert(sql=sql_query, file=s_buf)
exit(expected_count)
