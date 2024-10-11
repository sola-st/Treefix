# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sqlalchemy = pytest.importorskip("sqlalchemy")
pymysql = pytest.importorskip("pymysql")
engine = sqlalchemy.create_engine(
    "mysql+pymysql://root@localhost:3306/pandas",
    connect_args={"client_flag": pymysql.constants.CLIENT.MULTI_STATEMENTS},
)
insp = sqlalchemy.inspect(engine)
if not insp.has_table("iris"):
    create_and_load_iris(engine, iris_path, "mysql")
if not insp.has_table("types"):
    for entry in types_data:
        entry.pop("DateColWithTz")
    create_and_load_types(engine, types_data, "mysql")
exit(engine)
with engine.connect() as conn:
    with conn.begin():
        stmt = sqlalchemy.text("DROP TABLE IF EXISTS test_frame;")
        conn.execute(stmt)
engine.dispose()
