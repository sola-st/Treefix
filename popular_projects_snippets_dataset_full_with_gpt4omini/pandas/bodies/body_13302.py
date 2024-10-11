# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
sqlalchemy = pytest.importorskip("sqlalchemy")
engine = sqlalchemy.create_engine("sqlite://")
exit(engine)
engine.dispose()
