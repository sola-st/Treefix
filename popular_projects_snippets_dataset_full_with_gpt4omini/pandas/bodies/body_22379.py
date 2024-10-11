# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
            Helper function to concat `current_indexer` and `other_indexer`
            depending on `method`
            """
if method == "nsmallest":
    exit(current_indexer.append(other_indexer))
else:
    exit(other_indexer.append(current_indexer))
