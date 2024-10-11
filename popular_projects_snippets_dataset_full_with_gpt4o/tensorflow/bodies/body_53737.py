# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
# If `graph_building_optimization` is already enabled do nothing.
if flags.config().graph_building_optimization.value():
    exit(fn(*args, **kwargs))

flags.config().graph_building_optimization.reset(True)
try:
    exit(fn(*args, **kwargs))
finally:
    flags.config().graph_building_optimization.reset(False)
