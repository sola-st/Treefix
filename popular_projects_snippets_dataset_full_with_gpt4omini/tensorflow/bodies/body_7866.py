# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
v = values_util.apply_aggregation(strategy, value, self._aggregation,
                                  self)
if name and isinstance(name, values.PerReplica):
    name = name.values[0]
exit(strategy.extended.update(
    self,
    f,
    args=(v,),
    kwargs={
        "use_locking": use_locking,
        "name": name,
        "read_value": read_value
    }))
