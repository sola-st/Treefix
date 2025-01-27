# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_scatter_ops_test.py
np.random.seed(8)
with self.cached_session(use_gpu=False):
    for indices_shape in (2,), (3, 7), (3, 4, 7):
        for extra_shape in (), (5,), (5, 9):
            # Generate random indices with no duplicates for easy numpy comparison
            sparse_dim = len(indices_shape) - 1
            indices = np.random.randint(
                indices_shape[sparse_dim], size=indices_shape, dtype=itype)
            updates = _AsType(
                np.random.randn(*(indices_shape + extra_shape)), vtype)

            old = _AsType(np.random.randn(*(indices_shape + extra_shape)), vtype)

            # Scatter via numpy
            new = old.copy()
            np_scatter = _TF_OPS_TO_NUMPY[tf_scatter]
            np_scatter(new, indices, updates)
            # Scatter via tensorflow
            ref = variables.Variable(old)
            self.evaluate(variables.variables_initializer([ref]))

            if method:
                ref.batch_scatter_update(
                    indexed_slices.IndexedSlices(indices, updates))
            else:
                self.evaluate(tf_scatter(ref, indices, updates))
            self.assertAllClose(ref, new)
