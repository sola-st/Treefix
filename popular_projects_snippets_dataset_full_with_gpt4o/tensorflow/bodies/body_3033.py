# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_pack_test.py
compiled = jitrt.compile(src, 'test')

arg0 = np.random.uniform(0, 10.0, size=shape).astype(dtype)
arg1 = np.random.uniform(0, 10.0, size=shape).astype(dtype)

[res] = jitrt.execute(compiled, [arg0, arg1])
np.testing.assert_allclose(res, np.array([arg0, arg1]), atol=0.0)
