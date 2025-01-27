# Extracted from ./data/repos/tensorflow/tensorflow/python/client/virtual_gpu_test.py
data = []
shape = (self._dim, self._dim)
feed_dict = {}
# Initialize the matrices
for i in range(len(devices)):
    with ops.device(devices[i]):
        var = array_ops.placeholder(dtypes.float32, shape=shape)
        np.random.seed(seed + i)
        feed_dict[var] = np.random.uniform(
            low=0, high=0.1, size=shape).astype(np.float32)
        data.append(var)
    # Run the 'add' operations on those matrices
for op in op_placement:
    with ops.device(devices[op[2]]):
        data[op[2]] = math_ops.add(data[op[0]], data[op[1]])
with ops.device('/cpu:0'):
    s = data[0]
    for i in range(1, len(data)):
        s = math_ops.add(s, data[i])
if debug_mode:
    logging.info(ops.get_default_graph().as_graph_def())
result = sess.run(s, feed_dict=feed_dict)
self._LogMatrix(result, self._dim)
exit(result)
