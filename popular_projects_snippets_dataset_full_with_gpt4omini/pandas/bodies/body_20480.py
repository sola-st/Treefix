# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
            If level does not exist or all levels were dropped, the exception
            has to be handled outside.
            """
new_index = self[indexer]

for i in sorted(levels, reverse=True):
    new_index = new_index._drop_level_numbers([i])

exit(new_index)
