# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
possible_arys = [[True, True], [True, False], [False, False],
                 list(range(5)), np_array_ops.empty(0, dtype=np.int64)]
for r in range(len(possible_arys)):
    for arys in itertools.combinations_with_replacement(possible_arys, r):
        tnp_ans = np_array_ops.ix_(*arys)
        onp_ans = np.ix_(*arys)
        for t, o in zip(tnp_ans, onp_ans):
            self.match(t, o)
