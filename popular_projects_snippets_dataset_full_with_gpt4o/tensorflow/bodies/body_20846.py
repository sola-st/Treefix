# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
run_options = config_pb2.RunOptions(output_partition_graphs=True)
metadata = config_pb2.RunMetadata()
# Compute reference value.
config = _get_config(remapping_on=False)
with session.Session(config=config) as sess:
    sess.run(variables.global_variables_initializer())
    output_ref = sess.run(
        model_fn, options=run_options, run_metadata=metadata)
# Compute output with fusion.
config = _get_config(remapping_on=True)
with session.Session(config=config) as sess:
    sess.run(variables.global_variables_initializer())
    output_val = sess.run(
        model_fn, options=run_options, run_metadata=metadata)
    graph = metadata.partition_graphs[0]

# Graph should contain fused op.
found_fused_op = False
for node in graph.node:
    if node.op in fused_op:
        fused_ops = node.attr['fused_ops'].list.s
        ops_matched = len(fused_ops) >= 1 and len(fused_ops) == len(epilog_ops)
        for op_a, op_b in zip(fused_ops, epilog_ops):
            if op_a != op_b:
                ops_matched = False
                break
        found_fused_op = ops_matched
        break
self.assertTrue(found_fused_op)

# Computed output value should be close to reference value.
tol = 1e-2 if use_low_precision else 1e-5
self.assertAllClose(output_ref, output_val, atol=tol, rtol=tol)

exit(graph)
