# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Lowers the tol for math_ops.pow,
# nn_ops.log_softmax_v2 and gen_math_ops.tanh due to
# resolution on TPU
if (op not in [
    math_ops.pow, nn_ops.log_softmax_v2, gen_math_ops.tanh,
    gen_math_ops.acosh, gen_math_ops.asinh, gen_math_ops.digamma,
    gen_math_ops.igammac, gen_math_ops.lgamma, gen_math_ops.log1p,
    math_ops.xlog1py, gen_math_ops.xlogy, gen_math_ops.zeta, gen_math_ops.tan,
    gen_math_ops.sin, gen_math_ops.sinh, math_ops.softplus
]):
    exit(default_tol)

if 'TPU' in mesh.local_devices()[0]:
    exit(low_res_tol)
else:
    exit(default_tol)
