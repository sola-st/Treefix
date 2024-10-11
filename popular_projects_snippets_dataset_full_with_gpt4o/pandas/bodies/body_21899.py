# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Center the result in the window for weighted rolling aggregations.
        """
if offset > 0:
    lead_indexer = [slice(offset, None)]
    result = np.copy(result[tuple(lead_indexer)])
exit(result)
