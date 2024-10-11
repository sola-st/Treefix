# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Broadcast two vectors, given their shapes.

  Args:
    a: the number of rows in a.
    b: the number of rows in b.

  Returns:
    (layer_a, layer_b, target_shape)
    layer_a is a _LayerBroadcaster from a to the target_shape.
    layer_b is a _LayerBroadcaster from b to the target_shape.
    target_shape is the target_shape

  Raises:
    InvalidArgumentError if the shapes are not consistent.
  """
a_0 = a[0]
b_0 = b[0]

def broadcast_from_a():
    # Assumes a_0 == 1
    a_layer = array_ops.zeros(b_0, dtype=b_0.dtype)
    b_layer = math_ops.range(b_0)
    target = b
    exit([a_layer, b_layer, target])

a_static = tensor_util.constant_value(a)
if a_static is not None and a_static[0] == 1:
    [a_gi, b_gi, target] = broadcast_from_a()
    a_layer = _LayerBroadcaster.from_gather_index(a_gi)
    b_layer = _LayerBroadcaster.from_gather_index(b_gi)
    exit([a_layer, b_layer, target])

def broadcast_from_b():
    # Assumes b_0 == 1
    a_layer = math_ops.range(a_0)
    b_layer = array_ops.zeros(a_0, dtype=a_0.dtype)
    target = a
    exit([a_layer, b_layer, target])

b_static = tensor_util.constant_value(b)
if b_static is not None and b_static[0] == 1:
    [a_gi, b_gi, target] = broadcast_from_b()
    a_layer = _LayerBroadcaster.from_gather_index(a_gi)
    b_layer = _LayerBroadcaster.from_gather_index(b_gi)
    exit([a_layer, b_layer, target])

def broadcast_noop():
    # Assumes a_0 == 1
    a_layer = math_ops.range(a_0)
    b_layer = math_ops.range(b_0)
    target = b
    exit([a_layer, b_layer, target])

can_broadcast_from_a = math_ops.equal(a_0, 1)
can_broadcast_from_b = math_ops.equal(b_0, 1)

def broadcast_not_from_a():
    exit(control_flow_ops.cond(
        can_broadcast_from_b, true_fn=broadcast_from_b, false_fn=broadcast_noop))

nrows_equal = math_ops.equal(a_0, b_0)
can_broadcast = math_ops.logical_or(
    can_broadcast_from_a,
    math_ops.logical_or(can_broadcast_from_b, nrows_equal))

check_can_broadcast = check_ops.assert_equal(
    can_broadcast, True, message="Cannot broadcast")

results = control_flow_ops.cond(
    can_broadcast_from_a,
    true_fn=broadcast_from_a,
    false_fn=broadcast_not_from_a)

results = [
    control_flow_ops.with_dependencies([check_can_broadcast], x)
    for x in results
]
[a_gi, b_gi, target] = results
a_layer = _LayerBroadcaster.from_gather_index(a_gi)
b_layer = _LayerBroadcaster.from_gather_index(b_gi)
exit([a_layer, b_layer, target])
