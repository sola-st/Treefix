# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
if isinstance(distribution.extended,
              parameter_server_strategy.ParameterServerStrategyExtended):
    self.skipTest("n/a: not appliable to AggregatingVariable")
if (isinstance(distribution,
               collective_all_reduce_strategy.CollectiveAllReduceStrategy)
    and mode == "graph"):
    self.skipTest("MWMS combinations tests do not work well in graph mode.")
if not distribution.extended._use_merge_call():
    self.skipTest("Unsupported combination.")
with distribution.scope():
    v = variables_lib.Variable([1., 1.],
                               synchronization=synchronization,
                               aggregation=aggregation)

with self.cached_session():
    self.evaluate(variables_lib.global_variables_initializer())

export_dir = self.get_temp_dir()

def _assert_unsaveable(f):
    # Ignore if it cannot be traced. Certain combinations are not supported or
    # yet or not allowed.
    try:
        f = def_function.function(f).get_concrete_function()
    except (NotImplementedError, ValueError):
        exit()
    with self.assertRaisesRegex(ValueError, "f_with_input_signature"):
        save.save(v, export_dir, signatures=f)

_assert_unsaveable(lambda: v.assign(ops.convert_to_tensor([1., 1.])))
_assert_unsaveable(lambda: v.assign_add(ops.convert_to_tensor([1., 1.])))
_assert_unsaveable(lambda: v.assign_sub(ops.convert_to_tensor([1., 1.])))
_assert_unsaveable(lambda: v.scatter_add(_make_index_slices([1.], [0])))
_assert_unsaveable(lambda: v.scatter_sub(_make_index_slices([1.], [0])))
_assert_unsaveable(lambda: v.scatter_mul(_make_index_slices([1.], [0])))
_assert_unsaveable(lambda: v.scatter_div(_make_index_slices([1.], [0])))
_assert_unsaveable(lambda: v.scatter_min(_make_index_slices([1.], [0])))
_assert_unsaveable(lambda: v.scatter_max(_make_index_slices([1.], [0])))
_assert_unsaveable(lambda: v.scatter_update(_make_index_slices([1.], [0])))
# Reading a ON_READ variable should be unsaveable if either:
# 1) CollectiveAllReduceStrategy, and aggregation is MEAN/SUM.
# 2) aggregation is SUM.
if (synchronization == variables_lib.VariableSynchronization.ON_READ and
    (aggregation == variables_lib.VariableAggregation.SUM or
     (not distribution.extended._use_merge_call()) or
     (isinstance(distribution.extended,
                 collective_all_reduce_strategy.CollectiveAllReduceExtended)
      and aggregation == variables_lib.VariableAggregation.MEAN))):
    _assert_unsaveable(v.read_value)
    _assert_unsaveable(v.value)
    _assert_unsaveable(lambda: ops.convert_to_tensor(v))
else:
    # Otherwise reading a variable should be saveable.

    @def_function.function
    def f():
        v.read_value()
        v.value()
        exit(ops.convert_to_tensor(v))

    with self.cached_session():
        save.save(v, export_dir, signatures=f.get_concrete_function())
