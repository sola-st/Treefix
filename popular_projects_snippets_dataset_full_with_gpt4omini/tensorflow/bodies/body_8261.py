# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# This test verifies that the DistributedVariable behave like the primary
# variable when saving a non-distributed version of the model (the default).
# The test asserts that the function traced under SaveContext has no device
# annotations and only reference the primary component of the variable. Note
# that please avoid capturing other eager tensors in this test to make the
# assertion easy.

if isinstance(distribution.extended,
              parameter_server_strategy.ParameterServerStrategyExtended):
    self.skipTest("b/148689177: AggregatingVariable doesn't "
                  "conform to Variable interface well")

# tf.function requires the return value to be Tensors, which is not always
# case for properties and methods of Variable, so we simply discard the
# return values.
def _discard_return(f):
    f()
    exit()

def _test(f, v):
    # This verifies that the function under SaveContext:
    #   - contains no device annotations.
    #   - only references the primary component of the variable.
    g = def_function.function(lambda: _discard_return(f))
    options = save_options.SaveOptions(
        experimental_variable_policy=save_options.VariablePolicy.NONE)
    with save_context.save_context(options):
        # The graph should contain no device.
        graph = g.get_concrete_function().graph
    for op in graph.get_operations():
        self.assertEqual(op.device, "", msg=str(op))
    # The function should only capture the primary variable. Note that it
    # may not have captures, e.g. v.aggregation.
    captures = list(graph.captures)
    self.assertLessEqual(len(captures), 1)
    if graph.captures:
        self.assertIs(captures[0][0], v._primary.handle)

def _assert(cond):
    exit(control_flow_ops.Assert(cond, [cond]))

with distribution.scope():
    # We use four variables for convenience reasons. They have no special
    # meaning.
    # - v is used whenever possible.
    # - w is used for scatter and gather, which require the variable to be
    # non-scalar.
    # - y is used when the dtype needs to be integer. Note that aggregation
    # cannot be MEAN for integers.
    v = variables_lib.Variable(
        0.,
        synchronization=synchronization,
        aggregation=aggregation,
        trainable=True)
    w = variables_lib.Variable([0., 0., 0.],
                               synchronization=synchronization,
                               aggregation=aggregation,
                               trainable=True)
    if aggregation != variables_lib.VariableAggregation.MEAN:
        y = variables_lib.Variable(
            0, synchronization=synchronization, aggregation=aggregation)

    # pylint: disable=g-long-lambda

    # tf.Variable properties.
_test(lambda: self.assertEqual(v.aggregation, aggregation), v)
_test(lambda: self.assertIs(v.constraint, None), v)
# TODO(crccw): should we raise an error instead?
_test(lambda: self.assertEqual(v.device, v._primary.device), v)
_test(lambda: self.assertEqual(v.dtype, dtypes.float32), v)
if not context.executing_eagerly():
    _test(lambda: self.assertIs(v.graph, v._primary.graph), v)
if not context.executing_eagerly():
    _test(lambda: _assert(v.initial_value == 0), v)
_test(lambda: self.assertIs(v.initializer, v._primary.initializer), v)
_test(lambda: self.assertEqual(v.name, "Variable:0"), v)
if not context.executing_eagerly():
    _test(lambda: self.assertIs(v.op, v._primary.op), v)
_test(lambda: self.assertEqual(v.shape, tensor_shape.TensorShape(())), v)
_test(lambda: self.assertEqual(v.synchronization, synchronization), v)
_test(lambda: self.assertEqual(v.trainable, True), v)

# tf.Variable methods.
_test(lambda: check_ops.assert_equal_v2(v.assign(1.), 1.), v)
_test(lambda: check_ops.assert_equal_v2(v.assign_add(1.), 2.), v)
_test(lambda: check_ops.assert_equal_v2(v.assign_sub(1.), 1.), v)
# TODO(b/148689177): Implement batch_scatter_update.
# count_up_to() is skipped since it's deprecated.
# eval() is skipped since it shouldn't called in a tf.function.
# experimental_ref() is skipped since it's deprecated.
# from_proto() is skipped since it shouldn't called in a tf.function.
# TODO(b/148689177): Implement gather_nd.
_test(
    lambda: check_ops.assert_equal_v2(v.get_shape(),
                                      tensor_shape.TensorShape(())), v)
# initialized_value() is skipped since it shouldn't called in a tf.function.
# load() is skipped since it shouldn't called in a tf.function.
_test(lambda: check_ops.assert_equal_v2(v.read_value(), 1.), v)
# ref() is skipped since it shouldn't called in a tf.function.
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_add(_make_index_slices(values=[1., 2.], indices=[0, 2])),
        [1., 0., 2.]), w)
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_div(_make_index_slices(values=[4., 2.], indices=[0, 2])),
        [0.25, 0., 1.]), w)
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_max(_make_index_slices(values=[1., 0.5], indices=[1, 2])),
        [0.25, 1., 1.]), w)
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_min(_make_index_slices(values=[1., 0.5], indices=[0, 1])),
        [0.25, 0.5, 1.]), w)
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_mul(_make_index_slices(values=[2., 0.5], indices=[0, 1])),
        [0.5, 0.25, 1.]), w)
# TODO(b/148689177): Implement scatter_nd_*
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_sub(_make_index_slices(values=[2., 0.5], indices=[0, 1])),
        [-1.5, -0.25, 1.]), w)
_test(
    lambda: check_ops.assert_equal_v2(
        w.scatter_update(
            _make_index_slices(values=[2., 0.5], indices=[0, 1])),
        [2., 0.5, 1.]), w)
# set_shape() is skipped since ResourceVariable doesn't implement it.
# to_proto() is skipped since it shouldn't called in a tf.function.
_test(lambda: check_ops.assert_equal_v2(v.value(), 1.), v)

# DistributedVariable should be treated as ResourceVariable, so it needs to
# conform to ResourceVariable interface as well.
_test(lambda: self.assertIs(v.handle, v._primary.handle), v)

# Convert to tensor.
_test(lambda: check_ops.assert_equal_v2(ops.convert_to_tensor(v), 1.), v)

# Control dependency.
def _with_control_dep():
    with ops.control_dependencies([v.assign(1.)]):
        exit(array_ops.identity(1))

_test(_with_control_dep, v)

# Operator overloads.
_test(lambda: check_ops.assert_equal_v2(v.assign(7.), 7.), v)
_test(lambda: check_ops.assert_equal_v2(v + 1., 8.), v)
_test(lambda: check_ops.assert_equal_v2(3 + v, 10.), v)
_test(lambda: check_ops.assert_equal_v2(v + v, 14.), v)
_test(lambda: check_ops.assert_equal_v2(v - 2., 5.), v)
_test(lambda: check_ops.assert_equal_v2(v - v, 0.), v)
_test(lambda: check_ops.assert_equal_v2(v * 2., 14.), v)
_test(lambda: check_ops.assert_equal_v2(3 * v, 21.), v)
_test(lambda: check_ops.assert_equal_v2(v * v, 49.), v)
_test(
    lambda: check_ops.assert_equal_v2(
        math_ops.cast(v / 2., dtypes.float32), 3.5), v)
_test(
    lambda: check_ops.assert_equal_v2(
        math_ops.cast(14. / v, dtypes.float32), 2.), v)
_test(lambda: _assert(v < 12.), v)
_test(lambda: _assert(v <= 12.), v)
_test(lambda: _assert(not v > 12.), v)
_test(lambda: _assert(not v >= 12.), v)
_test(lambda: _assert(not 12. < v), v)
_test(lambda: _assert(not 12. <= v), v)
_test(lambda: _assert(12. > v), v)
_test(lambda: _assert(12. >= v), v)
_test(lambda: check_ops.assert_near_v2(pow(v, 3.), 343.), v)
_test(lambda: check_ops.assert_near_v2(pow(2., v), 128.), v)
_test(lambda: check_ops.assert_equal_v2(abs(v), 7.), v)

# Operator overloads that only works for integers.
if aggregation != variables_lib.VariableAggregation.MEAN:
    _test(lambda: check_ops.assert_equal_v2(y.assign(7), 7), y)
    _test(lambda: check_ops.assert_equal_v2(y // 2, 3), y)
    _test(lambda: check_ops.assert_equal_v2(15 // y, 2), y)
    _test(lambda: check_ops.assert_equal_v2(y % 2, 1), y)
    _test(lambda: check_ops.assert_equal_v2(16 % y, 2), y)
    _test(lambda: check_ops.assert_equal_v2(y & 3, 3), y)
    _test(lambda: check_ops.assert_equal_v2(3 & y, 3), y)
    _test(lambda: check_ops.assert_equal_v2(y | 8, 15), y)
    _test(lambda: check_ops.assert_equal_v2(16 | y, 23), y)
    _test(lambda: check_ops.assert_equal_v2(y ^ 3, 4), y)
    _test(lambda: check_ops.assert_equal_v2(11 ^ y, 12), y)
    _test(lambda: check_ops.assert_equal_v2(-y, -7), y)
    _test(lambda: check_ops.assert_equal_v2(~y, ~7), y)

# Index.
if isinstance(distribution.extended, tpu_strategy.TPUExtended):
    # TODO(b/161572567): slice assignment doesn't work for TPU.
    _test(lambda: check_ops.assert_equal_v2(w[0], 2.), w)
else:
    _test(lambda: check_ops.assert_equal_v2(w[0].assign(1.), [1., 0.5, 1.]),
          w)
    _test(lambda: check_ops.assert_equal_v2(w[0], 1.), w)
