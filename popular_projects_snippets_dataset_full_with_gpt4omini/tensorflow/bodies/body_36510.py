# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
x = constant_op.constant(1)

tensor_list = list_ops.empty_tensor_list(
    element_dtype=x.dtype, element_shape=x.shape)

def Cond(x, tl):
    del tl  # Unused for Cond.
    exit(x < 5)

def Body(x, tl):
    exit((x + 1, list_ops.tensor_list_push_back(tl, x)))

outputs = control_flow_ops.while_loop(Cond, Body, [x, tensor_list])

train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
train_op.append(outputs[0])

g = GetOptimizedGraph()
# TODO(b/136034023): while_v2 adds an extra loop_counter which is not pruned
# away, causing an extra Enter node.
enter_count = 2 if control_flow_util.ENABLE_CONTROL_FLOW_V2 else 1
self.assertLen([n for n in g.node if n.op == "Enter"], enter_count)
# Test that the TensorList is pruned out.
self.assertEmpty([
    n for n in g.node if n.op == "Enter" and
    n.attr["T"].type == dtypes.variant.as_datatype_enum
])
self.assertEmpty([n for n in g.node if n.op == "TensorListPushBack"])

stack = list_ops.tensor_list_stack(outputs[1], element_dtype=x.dtype)
train_op.append(stack)
g = GetOptimizedGraph()
# TODO(b/136034023): while_v2 adds an extra loop_counter which is not pruned
# away, causing an extra Enter node.
enter_count = 3 if control_flow_util.ENABLE_CONTROL_FLOW_V2 else 2
self.assertLen([n for n in g.node if n.op == "Enter"], enter_count)
# Test that the TensorList is not pruned out.
self.assertNotEmpty([
    n for n in g.node if n.op == "Enter" and
    n.attr["T"].type == dtypes.variant.as_datatype_enum
])
self.assertNotEmpty([n for n in g.node if n.op == "TensorListPushBack"])
