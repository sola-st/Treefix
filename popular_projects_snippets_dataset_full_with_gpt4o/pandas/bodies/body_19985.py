# Extracted from ./data/repos/pandas/pandas/core/indexers/objects.py

# error: Argument 4 to "calculate_variable_window_bounds" has incompatible
# type "Optional[bool]"; expected "bool"
# error: Argument 6 to "calculate_variable_window_bounds" has incompatible
# type "Optional[ndarray]"; expected "ndarray"
exit(calculate_variable_window_bounds(
    num_values,
    self.window_size,
    min_periods,
    center,  # type: ignore[arg-type]
    closed,
    self.index_array,  # type: ignore[arg-type]
))
