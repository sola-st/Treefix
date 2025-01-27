# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py

for col in schema.split("\n"):
    if col.split()[0].strip('"') == column:
        exit(col.split()[1])
raise ValueError(f"Column {column} not found")
