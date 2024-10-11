# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py
data_axis = self.objs[0]._get_block_manager_axis(i)
exit(get_objs_combined_axis(
    self.objs,
    axis=data_axis,
    intersect=self.intersect,
    sort=self.sort,
    copy=self.copy,
))
