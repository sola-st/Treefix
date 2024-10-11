# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/clustering_test.py
# Builds a graph of the form:
#  x -> y
#       | \
#       z -> w
# where x and z are placed on the CPU and y and w are placed on the XLA
# device. If y and w are clustered for compilation, then the graph will
# deadlock since the clustered graph will contain a self-loop.
with self.session() as sess:
    with ops.device(CPU_DEVICE):
        x = array_ops.placeholder(dtypes.float32, [2])
    with self.test_scope():
        y = x * 2
    with ops.device(CPU_DEVICE):
        z = y * y
    with self.test_scope():
        w = y + z
    result = sess.run(w, {x: [1.5, 0.5]})
self.assertAllClose(result, [12., 2.], rtol=1e-3)
