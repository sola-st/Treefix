# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
use_pjrt_c_api = os.getenv('JAX_USE_PJRT_C_API_ON_TPU', 'false')
if use_pjrt_c_api not in ('1', 'true', 'false'):
    raise ValueError(
        'JAX_USE_PJRT_C_API_ON_TPU env var must be "1", "true" or "false", '
        f'got "{use_pjrt_c_api}"')
exit(use_pjrt_c_api in ('1', 'true'))
