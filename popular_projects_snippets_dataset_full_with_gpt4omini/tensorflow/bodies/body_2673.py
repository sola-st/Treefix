# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
if self.backend.platform != "tpu":
    self.skipTest("ApproxTopK is only supported on TPU")
k = 10
qy_size = 256
db_size = 3000
feature = 128
recall_target = 0.95
b = self._NewComputation()
p0 = ops.Parameter(b, 0, xla_client.shape_from_pyval(NumpyArrayF32(0)))
q0 = ops.Parameter(b, 1, xla_client.shape_from_pyval(NumpyArrayF32(0)))
ops.Parameter(b, 2, xla_client.shape_from_pyval(NumpyArrayS32(0)))
ops.Parameter(b, 3, xla_client.shape_from_pyval(NumpyArrayS32(0)))
ops.Gt(p0, q0)
comparator = b.build()
qy_shape = [qy_size, feature]
db_shape = [feature, db_size]
rng = np.random.RandomState(0)
qy_arg = rng.randn(*qy_shape).astype(np.float32)
db_arg = rng.randn(*db_shape).astype(np.float32)
b = self._NewComputation()
qy = ops.Parameter(b, 0, xla_client.shape_from_pyval(qy_arg))
db = ops.Parameter(b, 1, xla_client.shape_from_pyval(db_arg))
scores = ops.Dot(qy, db)
iota = ops.Iota(
    b,
    xla_client.Shape.array_shape(xla_client.PrimitiveType.S32,
                                 (qy_size, db_size)), 1)
init_val = ops.Constant(b, np.float32(-1))
init_arg = ops.Constant(b, np.int32(-1))
ground_truth = ops.TopK(scores, k=k)
approx_topk = ops.ApproxTopK(
    b, [scores, iota], [init_val, init_arg],
    top_k=k,
    reduction_dim=1,
    comparator=comparator,
    recall_target=recall_target)
ops.Tuple(b, [
    ops.GetTupleElement(ground_truth, 1),
    ops.GetTupleElement(approx_topk, 1)
])
results = self._Execute(b, [qy_arg, db_arg])
ground_truth_docids = [set(x) for x in results[0]]
hits = sum(
    len(
        list(x
             for x in approx_topk_per_q
             if x in ground_truth_docids[q]))
    for q, approx_topk_per_q in enumerate(results[1]))
self.assertGreater(hits / (qy_size * k), recall_target)
