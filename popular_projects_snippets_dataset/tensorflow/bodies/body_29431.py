# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
np.random.seed(8)
ref_shapes = [(3, 6), (3, 6), (3, 6, 9), (3, 6, 9), (3, 6, 9), (3, 6, 9)]
indices_shapes = [(2,), (2, 2), (2,), (2, 2), (2, 3), (2, 3, 3)]
with test_util.device(use_gpu=True):
    for ref_shape, indices_shape in zip(ref_shapes, indices_shapes):
        num_updates = indices_shape[0]
        ixdim = indices_shape[-1]

        indexable_area_shape = ()
        for i in range(ixdim):
            indexable_area_shape += (ref_shape[i],)
        all_indices = [
            list(coord) for coord, _ in np.ndenumerate(
                np.empty(indexable_area_shape, vtype))
        ]
        np.random.shuffle(all_indices)
        indices = np.array(all_indices[:num_updates])

        if num_updates > 1 and repeat_indices:
            indices = indices[:num_updates // 2]
            for _ in range(num_updates - num_updates // 2):
                indices = np.append(
                    indices, [indices[np.random.randint(num_updates // 2)]], axis=0)
            np.random.shuffle(indices)
        indices = _AsType(indices[:num_updates], itype)

        updates_shape = (num_updates,)
        for i in range(ixdim, len(ref_shape)):
            updates_shape += (ref_shape[i],)
        updates = _AsType(np.random.randn(*(updates_shape)), vtype)
        ref = _AsType(np.random.randn(*(ref_shape)), vtype)

        # Scatter via numpy
        new = ref.copy()
        np_scatter(new, indices, updates)
        # Scatter via tensorflow
        ref_var = variables.VariableV1(ref)
        self.evaluate(ref_var.initializer)
        self.evaluate(tf_scatter(ref_var, indices, updates))

        # Compare
        tol = 1e-6 if vtype != dtypes.bfloat16.as_numpy_dtype else 1e-2
        self.assertAllClose(new, self.evaluate(ref_var), rtol=tol, atol=tol)
