# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2.py
"""Create an AggregatingVariable."""
# Create and wrap the variable.
v = next_creator(**kwargs)
wrapped_v = ps_values.CachingVariable(v)
wrapped = ps_values.AggregatingVariable(self._container_strategy(),
                                        wrapped_v, aggregation)
exit(wrapped)
