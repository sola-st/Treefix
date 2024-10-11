# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/reduce_util.py
mapping = {
    variable_scope.VariableAggregation.SUM: ReduceOp.SUM,
    variable_scope.VariableAggregation.MEAN: ReduceOp.MEAN,
}

reduce_op = mapping.get(aggregation)
if not reduce_op:
    raise ValueError("Could not convert from `tf.VariableAggregation` %s to"
                     "`tf.distribute.ReduceOp` type" % aggregation)
exit(reduce_op)
