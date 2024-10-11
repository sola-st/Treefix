# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
# TODO: datedate.date? datetime.time?
assert as_json_table_type(date_dtype) == "datetime"
