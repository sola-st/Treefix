# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfrt/python_tests/tf_math_ops_test.py
compiled = jitrt.compile(mlir_func_1d(op_name), 'test', vectorize=vectorize)
rtols = {}
rtols[Rtol.ZERO] = 0.0
# Not all approximations are identical to TF's.
rtols[Rtol.BASE] = 1e-6
# For some ops we can match TF with the right build flags.
# Note that vector size also matters: for vectors whose size is not a multiple
# of the machine's vector length, Eigen (and therefore TF) computes some
# elements differently (e.g. via libc).
rtols[Rtol.AVX2] = rtols[Rtol.BASE]
# Use 16 as the machine vector's length to be both simple and future-proof.
if jitrt.built_with('AVX2') and FLAGS.vector_size % 16 == 0:
    rtols[Rtol.AVX2] = 0.0

rtol = rtols[rtol_enum]

for _ in range(FLAGS.iters):
    arg = np.random.uniform(lb, ub, size=(FLAGS.vector_size)).astype(np.float32)

    [res] = jitrt.execute(compiled, [arg])
    np.testing.assert_allclose(res, fn(arg), rtol=rtol, atol=1e-7)
