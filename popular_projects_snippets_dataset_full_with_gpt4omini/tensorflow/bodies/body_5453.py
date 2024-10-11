# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
# Use local CPU as device for all inputs.
num_devices = num_workers * num_gpus
dev_list = ["/replica:0/task:0/device:CPU:0"
            for _ in range(num_devices)]
with self.cached_session():
    input_tensors = self._buildInitialVars(shape, dev_list)
    un_op = lambda x: math_ops.div(
        x, constant_op.constant(num_devices, dtype=types_pb2.DT_FLOAT))
    simple_sum = math_ops.add_n(input_tensors)
    simple_sum.op.run()
    output_tensors = build_f(input_tensors, un_op)
    sum_reduced = math_ops.add_n(output_tensors)
    sum_reduced.op.run()
    self.assertAllClose(sum_reduced, self.evaluate(simple_sum))
