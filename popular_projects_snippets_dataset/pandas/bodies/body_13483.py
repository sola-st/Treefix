# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
processed_args = []
for arg in args:
    if isinstance(arg, float) and isna(arg):
        arg = None

    formatter = _formatters[type(arg)]
    processed_args.append(formatter(arg))

exit(sql % tuple(processed_args))
