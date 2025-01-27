# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
"""Test MatMul+BiasAdd+Gelu fusion."""
self.maybe_skip_test(mode)

def gelu_approximate(x):
    exit(nn.gelu(x, approximate=True))

def gelu_exact(x):
    exit(nn.gelu(x, approximate=False))

device = '/device:GPU:0' if mode == 'cuda' else '/device:CPU:0'
config = []
if mode == 'mkl':
    config.append((dtypes.float32, gelu_exact, b'GeluExact'))
    config.append((dtypes.float32, gelu_approximate, b'GeluApproximate'))
    if _pywrap_utils.IsBF16SupportedByOneDNNOnThisCPU():
        config.append((dtypes.bfloat16, gelu_approximate, b'GeluApproximate'))
        config.append((dtypes.bfloat16, gelu_exact, b'GeluExact'))
elif mode == 'cuda':
    config.append((dtypes.float32, gelu_approximate, b'GeluApproximate'))
    config.append((dtypes.float16, gelu_approximate, b'GeluApproximate'))
    # Gelu exact fusion is supported by cuDNN frontend APIs and performant
    # with fp16 and on Ampere GPUs and later.
    if (test_util.is_gpu_available(
        cuda_only=True, min_cuda_compute_capability=(8, 0))):
        config.append((dtypes.float16, gelu_exact, b'GeluExact'))
        config.append((dtypes.float16, math_ops.tanh, b'Tanh'))
        config.append((dtypes.float16, math_ops.sigmoid, b'Sigmoid'))

m, n, k = (2, 4, 6)  # Matrix dimensions
fused_op = ['_MklNativeFusedMatMul', '_MklFusedMatMul', '_FusedMatMul']

for precision, act_fn, act_name in config:
    for transpose in (False, True):
        # Create MatMul + BiasAdd + Activation graph
        ops.reset_default_graph()
        with ops.device(device):
            x = _input([k, m] if transpose else [m, k])
            w = _weight([n, k] if transpose else [k, n])
            b = _bias([n])
            x = math_ops.cast(x, precision)
            w = math_ops.cast(w, precision)
            b = math_ops.cast(b, precision)
            y = math_ops.matmul(
                x, w, transpose_a=transpose, transpose_b=transpose)
            z = nn.bias_add(y, b)
            out = act_fn(z)

        if transpose and (device == '/device:CPU:0') and \
            act_name in (b'GeluApproximate', b'GeluExact'):
            if precision == dtypes.bfloat16:
                # No fusion should happen on CPU.
                self._VerifyNoFusion(out)
                continue
            else:
                # Gelu should not get fused, only BiasAdd.
                epilog_ops = [b'BiasAdd']
        else:
            epilog_ops = [b'BiasAdd', act_name]
        graph = self._VerifyValues(out, precision != dtypes.float32, fused_op,
                                   epilog_ops)
