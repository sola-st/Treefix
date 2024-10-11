# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py
c = context.Context()
c._set_global_seed(123)
for t in [np.int32, np.int64, np.uint32, np.uint64]:
    c._set_global_seed(t(123))
    c._set_global_seed(np.array(123, dtype=t))
    c._set_global_seed(ops.convert_to_tensor(123, dtype=t))
