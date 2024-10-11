# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cost_analyzer_test.py
image = array_ops.placeholder(dtypes.float32, shape=[1, 28, 28, 1])
label = array_ops.placeholder(dtypes.float32, shape=[1, 10])
w = variables.Variable(
    random_ops.truncated_normal([5, 5, 1, 32], stddev=0.1))
b = variables.Variable(random_ops.truncated_normal([32], stddev=0.1))
conv = nn_ops.conv2d(image, w, strides=[1, 1, 1, 1], padding="SAME")
h_conv = nn_ops.relu(conv + b)
h_conv_flat = array_ops.reshape(h_conv, [1, -1])

w_fc = variables.Variable(
    random_ops.truncated_normal([25088, 10], stddev=0.1))
b_fc = variables.Variable(random_ops.truncated_normal([10], stddev=0.1))
y_conv = nn_ops.softmax(math_ops.matmul(h_conv_flat, w_fc) + b_fc)

cross_entropy = math_ops.reduce_mean(
    -math_ops.reduce_sum(label * math_ops.log(y_conv), axis=[1]))
_ = adam.AdamOptimizer(1e-4).minimize(cross_entropy)

mg = meta_graph.create_meta_graph_def(graph=ops.get_default_graph())
report = cost_analyzer.GenerateCostReport(mg)

# Print the report to make it easier to debug
print("{}".format(report))

self.assertTrue(b"MatMul" in report)
self.assertTrue(b"ApplyAdam" in report)
self.assertTrue(b"Conv2DBackpropFilter" in report)
self.assertTrue(b"Softmax" in report)

# When mkl is enabled, Conv2D and MatMul op followed by
# 1-dimension Add in this graph will be fused, but not
# in the mkl disabled case.
expected_matmul_count = 2
op_types = [b"MatMul", b"Conv2DBackpropFilter"]

if not test_util.IsMklEnabled():
    self.assertTrue(b"Conv2D" in report)
    expected_matmul_count = 3
    op_types.append(b"Conv2D")

for op_type in op_types:
    matcher = re.compile(
        br"\s+" + op_type + br",\s*(\d+),\s*(\d+),\s*([\d\.eE+-]+)%,\s*" +
        br"([\d\.eE+-]+)%,\s*(-?\d+),\s*(\d+),", re.MULTILINE)
    m = matcher.search(report)

    op_count = int(m.group(1))
    # upper = int(m.group(5))
    lower = int(m.group(6))
    if op_type == b"MatMul":
        self.assertEqual(expected_matmul_count, op_count)
    else:
        self.assertEqual(1, op_count)
    self.assertTrue(0 <= lower)
    # self.assertTrue(0 < upper)
    # self.assertTrue(lower <= upper)
