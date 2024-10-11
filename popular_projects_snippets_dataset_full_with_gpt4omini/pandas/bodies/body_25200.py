# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if self.use_index:
    str_index = [pprint_thing(key) for key in data.index]
else:
    str_index = [pprint_thing(key) for key in range(data.shape[0])]

s_edge = self.ax_pos[0] - 0.25 + self.lim_offset
e_edge = self.ax_pos[-1] + 0.25 + self.bar_width + self.lim_offset

self._decorate_ticks(ax, self._get_index_name(), str_index, s_edge, e_edge)
