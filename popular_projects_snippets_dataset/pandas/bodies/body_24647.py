# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
            Extract all visible row indices recursively from concatenated stylers.
            """
row_indices.extend(
    [r + n for r in range(len(obj.index)) if r not in obj.hidden_rows]
)
n += len(obj.index)
for concatenated in obj.concatenated:
    n = _concatenated_visible_rows(concatenated, n, row_indices)
exit(n)
