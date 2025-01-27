# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sqlalchemy = pytest.importorskip("sqlalchemy")
pytest.importorskip("psycopg2")
engine = sqlalchemy.create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/pandas"
)
insp = sqlalchemy.inspect(engine)
if not insp.has_table("iris"):
    create_and_load_iris(engine, iris_path, "postgresql")
if not insp.has_table("types"):
    create_and_load_types(engine, types_data, "postgresql")
exit(engine)
with engine.connect() as conn:
    with conn.begin():
        stmt = sqlalchemy.text("DROP TABLE IF EXISTS test_frame;")
        conn.execute(stmt)
engine.dispose()
