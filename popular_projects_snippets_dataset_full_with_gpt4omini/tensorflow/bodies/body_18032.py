# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = constant_op.constant([1, 2, 3])

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    with ops.control_dependencies([
        logging_ops.print_v2(
            x1, "x1", array_ops.shape(x1), summarize=10)]):
        exit(array_ops.identity(x1))

self._test_loop_fn(loop_fn, 3)

with self.captureWritesToStream(sys.stderr) as printed:
    self.evaluate(pfor_control_flow_ops.pfor(loop_fn, 3))
self.assertIn("[1 2 3] x1 []", printed.contents())
