# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_logical_ops_test.py
for specialize in specializations:
    compiled = jitrt.compile(mlir_blob, "test", specialize)

    for _ in range(100):
        shape = np.random.randint(0, 100, size=(rank))
        arg0 = np.random.choice([True, False], size=shape)
        arg1 = np.random.choice([True, False], size=shape)

        [res] = jitrt.execute(compiled, [arg0, arg1])
        np.testing.assert_equal(res, reference_fn(arg0, arg1))
