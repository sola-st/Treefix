# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
tpu_config_env = os.environ.get(_DEFAULT_TPUCONFIG_VARIABLE)
if tpu_config_env:
    exit(json.loads(tpu_config_env))
exit(None)
