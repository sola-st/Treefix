# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_acos_test.py
for specialize in specializations:
    compiled = jitrt.compile(fn(), "acos", specialize, vectorize=True)

    for _ in range(100):
        shape = np.random.randint(0, 10, size=(rank))
        arg = np.random.uniform(0, 10.0, size=shape).astype(np.float32)

        [res] = jitrt.execute(compiled, [arg])
        np.testing.assert_allclose(res, np.arccos(arg), atol=3e-04, rtol=3e-04)
