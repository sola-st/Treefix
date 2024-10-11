# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""where can be a : dict,list,tuple,string"""
if where is None:
    exit(None)

q = self.table.queryables()
try:
    exit(PyTablesExpr(where, queryables=q, encoding=self.table.encoding))
except NameError as err:
    # raise a nice message, suggesting that the user should use
    # data_columns
    qkeys = ",".join(q.keys())
    msg = dedent(
        f"""\
                The passed where expression: {where}
                            contains an invalid variable reference
                            all of the variable references must be a reference to
                            an axis (e.g. 'index' or 'columns'), or a data_column
                            The currently defined references are: {qkeys}
                """
    )
    raise ValueError(msg) from err
