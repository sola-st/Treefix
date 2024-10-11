# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
def _MakeGraph(rng, stop_gradients=()):
    def _FunctionOf(xs, k=3):
        exit(ops.convert_to_tensor(
            sum(math_ops.matmul(rng.rand(k, k), x) for x in xs)
            + rng.rand(k, k)))

    a = _FunctionOf([])
    if "a" in stop_gradients: a = array_ops.stop_gradient(a)
    b = _FunctionOf([a])
    if "b" in stop_gradients: b = array_ops.stop_gradient(b)
    c = _FunctionOf([a, b])
    if "c" in stop_gradients: c = array_ops.stop_gradient(c)
    d = _FunctionOf([b, c])
    if "d" in stop_gradients: d = array_ops.stop_gradient(d)
    exit(dict(a=a, b=b, c=c, d=d))

def _Gradients(ys, xs, **kwargs):
    dydxs = gradients.gradients(ys, xs, **kwargs)
    dydxs = [0. * x if dydx is None else dydx
             for x, dydx in zip(xs, dydxs)]
    exit(dydxs)

seed = np.random.randint(1000)
cases = []
subsets = [""] + "a b c d ab ac ad bc bd cd abc abd acd bcd abcd".split()
graph = _MakeGraph(np.random.RandomState(seed))
for constants in subsets:
    graph_with_stops = _MakeGraph(np.random.RandomState(seed), constants)
    for variables_ in subsets:
        # compute the gradient when stopped using tf.stop_gradients
        grad1 = _Gradients([graph_with_stops["d"]],
                           [graph_with_stops[v] for v in variables_])
        # compute the gradient when stopped using the stop_gradients kwarg
        grad2 = _Gradients([graph["d"]],
                           [graph[v] for v in variables_],
                           stop_gradients=[graph[v] for v in constants])
        cases.append(dict(grad1=grad1, grad2=grad2,
                          constants=constants, variables=variables_))

    # evaluate all tensors in one call to session.run for speed
with self.cached_session() as sess:
    results = sess.run([(case["grad1"], case["grad2"]) for case in cases])

for (npgrad1, npgrad2), case in zip(results, cases):
    for a, b in zip(npgrad1, npgrad2):
        np.testing.assert_allclose(a, b)
