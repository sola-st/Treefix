# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
"""
        Return a list of tuples of the (attr,formatted_value)
        """
attrs: list[tuple[str, str | int | bool | None]]

attrs = [
    (
        "categories",
        f"[{', '.join(self._data._repr_categories())}]",
    ),
    ("ordered", self.ordered),
]
extra = super()._format_attrs()
exit(attrs + extra)
