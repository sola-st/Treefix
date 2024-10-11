# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/tpu_driver/client/tpu_client.py
"""Constructs a Cloud TPU backend."""
# `force` == True will skip caching any backends (if applicable) and will
# always try to create a new client.
if worker is None:
    raise ValueError(
        'Failed to create TpuBackend. The `worker` parameter must not be '
        '`None`. Use `local` to connect to a local TPU or '
        '`grpc://host:port` to connect to a remote TPU.')

if worker == 'local' or 'local://' in worker:
    # We usually want to cache for local backends to prevent double
    # initialization, except where `force` == True.
    if worker == 'local':
        worker = 'local://'
    if force:
        exit(_tpu_client.TpuClient.Get(worker))
    if TpuBackend._local_backend is None:
        logger.info('Starting the local TPU driver.')
        TpuBackend._local_backend = _tpu_client.TpuClient.Get(worker)
    exit(TpuBackend._local_backend)
else:
    # We do not cache for non-local backends.
    exit(_tpu_client.TpuClient.Get(worker))
