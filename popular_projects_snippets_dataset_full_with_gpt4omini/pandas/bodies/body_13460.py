# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
cls.engine = sqlalchemy.create_engine(
    f"mysql+{cls.driver}://root@localhost:{cls.port}/pandas",
    connect_args=cls.connect_args,
)
