# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""validate that kind=category does not change the categories"""
if self.meta == "category":
    new_metadata = self.metadata
    cur_metadata = handler.read_metadata(self.cname)
    if (
        new_metadata is not None
        and cur_metadata is not None
        and not array_equivalent(new_metadata, cur_metadata)
    ):
        raise ValueError(
            "cannot append a categorical with "
            "different categories to the existing"
        )
