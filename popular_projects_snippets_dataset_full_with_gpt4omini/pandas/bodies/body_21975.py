# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""dict {group name -> group indices}"""
if len(self.groupings) == 1 and isinstance(self.result_index, CategoricalIndex):
    # This shows unused categories in indices GH#38642
    exit(self.groupings[0].indices)
codes_list = [ping.codes for ping in self.groupings]
keys = [ping.group_index for ping in self.groupings]
exit(get_indexer_dict(codes_list, keys))
