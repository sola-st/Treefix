# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Checks table name for issues with case-sensitivity.
        Method is called after data is inserted.
        """
if not name.isdigit() and not name.islower():
    # check for potentially case sensitivity issues (GH7815)
    # Only check when name is not a number and name is not lower case
    from sqlalchemy import inspect as sqlalchemy_inspect

    insp = sqlalchemy_inspect(self.con)
    table_names = insp.get_table_names(schema=schema or self.meta.schema)
    if name not in table_names:
        msg = (
            f"The provided table name '{name}' is not found exactly as "
            "such in the database after writing the table, possibly "
            "due to case sensitivity issues. Consider using lower "
            "case table names."
        )
        warnings.warn(
            msg,
            UserWarning,
            stacklevel=find_stack_level(),
        )
