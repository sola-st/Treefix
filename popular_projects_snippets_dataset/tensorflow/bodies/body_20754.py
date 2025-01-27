# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
random_seed.set_random_seed(0)
x = random_ops.truncated_normal([2, 5, 5, 4], seed=0)
scale = constant_op.constant(0.1, shape=[4])
offset = constant_op.constant(0.3, shape=[4])
y, mean, _ = nn.fused_batch_norm(x, scale, offset)
mul = math_ops.add(y, mean)
output = array_ops.identity(mul)
exit(output)
