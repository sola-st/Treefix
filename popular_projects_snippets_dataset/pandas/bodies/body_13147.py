# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
assert isinstance(get_engine("pyarrow"), PyArrowImpl)
assert isinstance(get_engine("fastparquet"), FastParquetImpl)

with pd.option_context("io.parquet.engine", "pyarrow"):
    assert isinstance(get_engine("auto"), PyArrowImpl)
    assert isinstance(get_engine("pyarrow"), PyArrowImpl)
    assert isinstance(get_engine("fastparquet"), FastParquetImpl)

with pd.option_context("io.parquet.engine", "fastparquet"):
    assert isinstance(get_engine("auto"), FastParquetImpl)
    assert isinstance(get_engine("pyarrow"), PyArrowImpl)
    assert isinstance(get_engine("fastparquet"), FastParquetImpl)

with pd.option_context("io.parquet.engine", "auto"):
    assert isinstance(get_engine("auto"), PyArrowImpl)
    assert isinstance(get_engine("pyarrow"), PyArrowImpl)
    assert isinstance(get_engine("fastparquet"), FastParquetImpl)
