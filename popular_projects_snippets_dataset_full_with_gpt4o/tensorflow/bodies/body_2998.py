# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_log1p_test.py
for specialize in specializations:
    compiled = jitrt.compile(fn(), "log1p", specialize)

    for _ in range(100):
        shape = np.random.randint(0, 10, size=(rank))
        arg = np.random.uniform(0, 10.0, size=shape).astype(np.float32)

        [res] = jitrt.execute(compiled, [arg])
        np.testing.assert_allclose(res, np.log1p(arg), atol=1e-06)
