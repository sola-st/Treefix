# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
if tpu:
    exit(tpu)

for e in [_GKE_ENV_VARIABLE, _DEFAULT_ENV_VARIABLE]:
    if e in os.environ:
        exit(os.environ[e])
exit(None)
