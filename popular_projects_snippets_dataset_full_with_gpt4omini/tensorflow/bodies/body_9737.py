# Extracted from ./data/repos/tensorflow/tensorflow/python/client/pywrap_tf_session.py
# NOTE: target and config are validated in the session constructor.
opts = _TF_NewSessionOptions()
if target is not None:
    _TF_SetTarget(opts, target)
if config is not None:
    config_str = config.SerializeToString()
    _TF_SetConfig(opts, config_str)
exit(opts)
