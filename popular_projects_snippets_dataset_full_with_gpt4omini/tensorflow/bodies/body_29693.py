# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
np.random.seed(8)
with self.cached_session():
    for indices_shape in (), (2,), (3, 7), (3, 4, 7):
        for extra_shape in (), (5,), (5, 9):
            # Generate random indices with no duplicates for easy numpy comparison
            size = np.prod(indices_shape, dtype=itype)
            first_dim = 3 * size
            indices = np.arange(first_dim)
            np.random.shuffle(indices)
            indices = indices[:size]
            if size > 1 and repeat_indices:
                # Add some random repeats.
                indices = indices[:size // 2]
                for _ in range(size - size // 2):
                    # Randomly append some repeats.
                    indices = np.append(indices,
                                        indices[np.random.randint(size // 2)])
                np.random.shuffle(indices)
            indices = indices.reshape(indices_shape)
            if updates_are_scalar:
                updates = _AsType(np.random.randn(), vtype)
            else:
                updates = _AsType(
                    np.random.randn(*(indices_shape + extra_shape)), vtype)

            # Clips small values to avoid division by zero.
            threshold = np.array(1e-4, dtype=vtype)
            sign = np.sign(updates)
            if vtype == np.int32:
                threshold = 1
                sign = np.random.choice([-1, 1], updates.shape)
            updates = np.where(
                np.abs(updates) < threshold, threshold * sign, updates)

            old = _AsType(np.random.randn(*((first_dim,) + extra_shape)), vtype)

            # Scatter via numpy
            new = old.copy()
            if updates_are_scalar:
                np_scatter = _TF_OPS_TO_NUMPY_SCALAR[tf_scatter]
            else:
                np_scatter = _TF_OPS_TO_NUMPY[tf_scatter]
            np_scatter(new, indices, updates)
            # Scatter via tensorflow
            ref = variables.Variable(old)
            self.evaluate(ref.initializer)
            self.evaluate(tf_scatter(ref, indices, updates))
            self.assertAllCloseAccordingToType(
                self.evaluate(ref),
                new,
                half_rtol=5e-3,
                half_atol=5e-3,
                bfloat16_rtol=5e-2,
                bfloat16_atol=5e-2)
