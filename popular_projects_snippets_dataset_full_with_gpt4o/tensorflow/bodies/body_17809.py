# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp = random_ops.random_uniform([3, 2])
output = nn.embedding_lookup(inp, [0, 2])
pfor_jacobian = gradients.jacobian(output, inp, use_pfor=True)
while_jacobian = gradients.jacobian(output, inp, use_pfor=False)
self.run_and_assert_equal(while_jacobian, pfor_jacobian)
