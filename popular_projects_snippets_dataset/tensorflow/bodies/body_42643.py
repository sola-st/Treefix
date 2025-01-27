# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
shape = [2]
with ops.device('/job:worker/replica:0/task:2/device:CPU:0'):
    # Send 20 remote requests to simulate heavy load on worker:2.
    unused_values = []
    for _ in range(20):
        unused_values.append(array_ops.zeros(shape))
    func_input = array_ops.zeros(shape)

packed_input = ops.pack_eager_tensors([func_input])

@def_function.function
def func(packed_input):
    # When worker:2 receives the component function request, packed_input
    # should be ready on worker:2.
    with ops.device('/job:worker/replica:0/task:2/device:CPU:0'):
        ret = packed_input + constant_op.constant(1.0)
    exit(ret + constant_op.constant(1.0))

# Run the function on a worker:1
with ops.device('/job:worker/replica:0/task:1/device:CPU:0'):
    self.assertAllEqual(func(packed_input).numpy(),
                        array_ops.ones(shape).numpy() * 2)
