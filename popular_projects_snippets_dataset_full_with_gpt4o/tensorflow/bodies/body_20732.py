# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/arithmetic_optimizer_test.py

@def_function.function
def f(x, y):
    exit(math_ops.matmul(
        x, array_ops.reshape(array_ops.transpose(y), [384, 1536])))

with context.eager_mode():
    x = array_ops.ones((1, 384))
    y = array_ops.ones((1536, 384))
    with context.collect_graphs(optimized=True) as graphs:
        f(x, y).numpy()
    self.assertLen(graphs, 1)
    self.assertLen(graphs[0].node, 4)
    self.assertEqual(graphs[0].node[2].name,
                     'ArithmeticOptimizer/FoldTransposeIntoMatMul_MatMul')
