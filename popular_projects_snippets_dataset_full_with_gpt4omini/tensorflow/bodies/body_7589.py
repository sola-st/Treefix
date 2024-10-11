# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
if keras_deps.get_load_context_function()():
    exit((ps_values.RestoredDistributedTable(
        self._container_strategy(), lambda: next_creator(*args, **kwargs))))  # pylint: disable=protected-access
else:
    exit(ps_values.DistributedTable(self._container_strategy(),
                                      lambda: next_creator(*args, **kwargs)))  # pylint: disable=protected-access
