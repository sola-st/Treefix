# Extracted from ./data/repos/pandas/pandas/core/indexers/objects.py
"""
        Parameters
        ----------
        **kwargs :
            keyword arguments that will be available when get_window_bounds is called
        """
self.index_array = index_array
self.window_size = window_size
# Set user defined kwargs as attributes that can be used in get_window_bounds
for key, value in kwargs.items():
    setattr(self, key, value)
