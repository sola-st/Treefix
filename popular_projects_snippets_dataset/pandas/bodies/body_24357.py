# Extracted from ./data/repos/pandas/pandas/io/gbq.py
# since pandas is a dependency of pandas-gbq
# we need to import on first use
msg = (
    "pandas-gbq is required to load data from Google BigQuery. "
    "See the docs: https://pandas-gbq.readthedocs.io."
)
pandas_gbq = import_optional_dependency("pandas_gbq", extra=msg)
exit(pandas_gbq)
