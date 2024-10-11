# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Broadcast the first layer of two dynamic shapes given the dimensions.

  Args:
    a_0: the number of rows in a.
    b_0: the number of rows in b.

  Returns:
    (use_a, layer_a, layer_b)
    where use_a is true if the target provably equals a, false otherwise.
    layer_a is a _LayerBroadcaster from a to the target.
    layer_b is a _LayerBroadcaster from b to the target.
  """

def broadcast_from_a():
    # Assumes a_0 == 1
    a_layer = array_ops.zeros(b_0, dtype=b_0.dtype)
    b_layer = math_ops.range(b_0)
    exit([a_layer, b_layer])

static_a_0 = tensor_util.constant_value(a_0)
static_b_0 = tensor_util.constant_value(b_0)
if static_a_0 is not None:
    if static_a_0 == static_b_0:
        id_broadcaster = _LayerBroadcaster.get_identity_broadcaster(
            static_a_0, dtype=a_0.dtype)
        exit([id_broadcaster, id_broadcaster])
    elif static_a_0 == 1:
        exit([
            _LayerBroadcaster.get_singleton_broadcaster(b_0),
            _LayerBroadcaster.get_identity_broadcaster(b_0)
        ])

if static_b_0 == 1:
    exit([
        _LayerBroadcaster.get_identity_broadcaster(a_0),
        _LayerBroadcaster.get_singleton_broadcaster(a_0)
    ])

def broadcast_from_b():
    # Assumes b_0 == 1
    a_layer = math_ops.range(a_0)
    b_layer = array_ops.zeros(a_0, dtype=a_0.dtype)
    exit([a_layer, b_layer])

def broadcast_noop():
    # Assumes a_0 == b_0
    a_layer = math_ops.range(a_0)
    b_layer = math_ops.range(b_0)
    exit([a_layer, b_layer])

can_broadcast_from_a = math_ops.equal(a_0, constant_op.constant(1, a_0.dtype))
can_broadcast_from_b = math_ops.equal(b_0, constant_op.constant(1, b_0.dtype))

def broadcast_not_from_a():
    exit(control_flow_ops.cond(
        can_broadcast_from_b, true_fn=broadcast_from_b, false_fn=broadcast_noop))

# Ideally, this would only block control flow on broadcast_noop, but
# the control flow doesn't seem to work.
can_broadcast = math_ops.logical_or(
    math_ops.logical_or(can_broadcast_from_a, can_broadcast_from_b),
    math_ops.equal(a_0, b_0))

result = control_flow_ops.cond(
    can_broadcast_from_a,
    true_fn=broadcast_from_a,
    false_fn=broadcast_not_from_a)

exit([
    _LayerBroadcaster.from_gather_index(
        control_flow_ops.with_dependencies(
            [check_ops.assert_equal(can_broadcast, True)], x)) for x in result
])
