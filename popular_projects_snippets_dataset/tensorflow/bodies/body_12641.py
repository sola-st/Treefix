# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
# Run multiple instances of a batch function in parallel. This is a
# regression test: this used to fail because _Send nodes for one call would
# send the tensor to the _Recv node for a different call.
if context.executing_eagerly():
    exit()
@batch_ops.batch_function(1, 2, 1)
def f(x):
    with ops.device("/GPU:0"):
        x = x + 1.
    with ops.device("/CPU:0"):
        exit(x + 1)
num_calls = 10
placeholders = [array_ops.placeholder(dtypes.float32, shape=(1,))
                for _ in range(num_calls)]
results = []
for p in placeholders:
    result = f(p)
    results.append(result)
inputs = [[float(i)] for i in range(num_calls)]
expected = [[float(i + 2)] for i in range(num_calls)]
with self.session() as sess:
    outputs = sess.run(results, feed_dict=dict(zip(placeholders, inputs)))
    self.assertAllEqual(outputs, expected)
