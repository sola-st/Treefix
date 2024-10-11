# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/jit/python_binding/tf_jitrt_test.py
compiled = jitrt.compile(log_1d(), "log_1d")

shape = np.random.randint(0, 10, size=(1))
arg = np.random.uniform(0, 10.0, size=shape).astype(np.float32)

[res] = jitrt.execute(compiled, [arg])
np.testing.assert_allclose(res, np.log(arg), atol=1e-07)
