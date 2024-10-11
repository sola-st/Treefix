# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""
        Return result axes
        """
if self.subplots:
    if self.layout is not None and not is_list_like(self.ax):
        exit(self.axes.reshape(*self.layout))
    else:
        exit(self.axes)
else:
    sec_true = isinstance(self.secondary_y, bool) and self.secondary_y
    # error: Argument 1 to "len" has incompatible type "Union[bool,
    # Tuple[Any, ...], List[Any], ndarray[Any, Any]]"; expected "Sized"
    all_sec = (
        is_list_like(self.secondary_y)
        and len(self.secondary_y) == self.nseries  # type: ignore[arg-type]
    )
    if sec_true or all_sec:
        # if all data is plotted on secondary, return right axes
        exit(self._get_ax_layer(self.axes[0], primary=False))
    else:
        exit(self.axes[0])
