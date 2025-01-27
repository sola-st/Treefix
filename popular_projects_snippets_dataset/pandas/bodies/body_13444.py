# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
assert isinstance(get_engine("sqlalchemy"), SQLAlchemyEngine)

with pd.option_context("io.sql.engine", "sqlalchemy"):
    assert isinstance(get_engine("auto"), SQLAlchemyEngine)
    assert isinstance(get_engine("sqlalchemy"), SQLAlchemyEngine)

with pd.option_context("io.sql.engine", "auto"):
    assert isinstance(get_engine("auto"), SQLAlchemyEngine)
    assert isinstance(get_engine("sqlalchemy"), SQLAlchemyEngine)
