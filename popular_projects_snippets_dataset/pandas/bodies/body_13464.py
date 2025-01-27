# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
cls.engine = sqlalchemy.create_engine(
    f"postgresql+{cls.driver}://postgres:postgres@localhost:{cls.port}/pandas"
)
