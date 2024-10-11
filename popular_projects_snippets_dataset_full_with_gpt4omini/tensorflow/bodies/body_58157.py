# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
with ops.Graph().as_default():
    i = array_ops.placeholder(dtype=dtypes.int32, shape=())
    c = lambda i: math_ops.less(i, 10)
    b = lambda i: math_ops.add(i, 1)
    control_flow_ops.while_loop(c, b, [i])
    sess = session.Session()

new_graph_def = convert_to_constants.disable_lower_using_switch_merge(
    sess.graph_def)
lower_using_switch_merge_is_removed = False
for node in new_graph_def.node:
    if node.op == "While" or node.op == "StatelessWhile":
        if not node.attr["_lower_using_switch_merge"].b:
            lower_using_switch_merge_is_removed = True
self.assertTrue(lower_using_switch_merge_is_removed)
