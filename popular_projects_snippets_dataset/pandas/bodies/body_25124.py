# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
self._args_adjust()
self._compute_plot_data()
self._setup_subplots()
self._make_plot()
self._add_table()
self._make_legend()
self._adorn_subplots()

for ax in self.axes:
    self._post_plot_logic_common(ax, self.data)
    self._post_plot_logic(ax, self.data)
