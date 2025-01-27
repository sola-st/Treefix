# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
freq = to_offset(freq)
self.format = None
self.freq = freq
self.locs: list[Any] = []  # unused, for matplotlib compat
self.formatdict: dict[Any, Any] | None = None
self.isminor = minor_locator
self.isdynamic = dynamic_mode
self.offset = 0
self.plot_obj = plot_obj
self.finder = get_finder(freq)
