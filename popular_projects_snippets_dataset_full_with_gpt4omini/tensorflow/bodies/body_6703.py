# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_values.py
scater_xxx_fn = tpu_util.make_raw_scatter_xxx_fn(raw_scater_xxx_fn)
if tpu_util.enclosing_tpu_context():
    if self._aggregation != variable_scope.VariableAggregation.NONE:
        raise NotImplementedError(
            _scatter_error_msg.format(
                op_name=op_name, aggregation=self._aggregation))
    exit(scater_xxx_fn(
        var, sparse_delta=sparse_delta, use_locking=use_locking, name=name))
else:
    exit(var._update(  # pylint: disable=protected-access
        update_fn=scater_xxx_fn,
        value=sparse_delta,
        use_locking=use_locking,
        name=name))
