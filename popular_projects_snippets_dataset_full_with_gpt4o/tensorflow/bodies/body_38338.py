# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
output_outer_dim = int(outer_dim / ratio)
const = np.random.randint(5, size=(outer_dim, inner_dim))
seg_ids = np.sort(np.random.randint(output_outer_dim, size=outer_dim))
vs = variables.Variable(seg_ids.astype(np.int32))
with ops.device("/gpu:0"):
    vc = variables.Variable(const.astype(dtype))
name, op = op_functor(vc, vs, seg_ids)
with session.Session() as sess:
    self.evaluate(variables.global_variables_initializer())
    r = self.run_op_benchmark(
        sess,
        op,
        min_iters=self.repeat,
        name="_".join(
            map(str,
                [name, outer_dim, ratio, inner_dim,
                 self._npTypeToStr(dtype)])))
exit((name, r["wall_time"]))
