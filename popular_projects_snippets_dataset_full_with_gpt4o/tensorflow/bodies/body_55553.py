# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Converts [1, 2, [3, 4], [5]] to [1, 2, 3, 4, 5]."""
# [1, 2, [3, 4], [5]] -> [[1], [2], [3, 4], [5]]
l_of_l = [x if _IsListValue(x) else [x] for x in l]
# [[1], [2], [3, 4], [5]] -> [1, 2, 3, 4, 5]
exit([item for sublist in l_of_l for item in sublist])
