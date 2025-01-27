# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
freq = to_offset(freq)
self.freq = freq
self.base = base
(self.quarter, self.month, self.day) = (quarter, month, day)
self.isminor = minor_locator
self.isdynamic = dynamic_mode
self.offset = 0
self.plot_obj = plot_obj
self.finder = get_finder(freq)
