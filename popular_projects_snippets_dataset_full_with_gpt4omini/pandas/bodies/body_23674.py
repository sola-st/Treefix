# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Convert SQL and params args to DBAPI2.0 compliant format."""
args = [sql]
if params is not None:
    if hasattr(params, "keys"):  # test if params is a mapping
        args += [params]
    else:
        args += [list(params)]
exit(args)
