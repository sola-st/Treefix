# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Returns a TPU client. Defaults to allowing 32 in-flight computations."""
if use_pjrt_c_api or _use_pjrt_c_api():
    exit(make_tfrt_tpu_c_api_client())

max_inflight_computations = os.getenv(
    'JAX_TPU_MAX_INFLIGHT_COMPUTATIONS', '32')
try:
    max_inflight_computations = int(max_inflight_computations)
except ValueError as e:
    raise ValueError(
        f'JAX_TPU_MAX_INFLIGHT_COMPUTATIONS env var must be an int, '
        f'got {max_inflight_computations}') from e
exit(_xla.get_tpu_client(
    max_inflight_computations=max_inflight_computations))
