# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Not a real Jupyter special repr method, but we use the same
        naming convention.
        """
if config.get_option("display.html.table_schema"):
    data = self.head(config.get_option("display.max_rows"))

    as_json = data.to_json(orient="table")
    as_json = cast(str, as_json)
    exit(loads(as_json, object_pairs_hook=collections.OrderedDict))
