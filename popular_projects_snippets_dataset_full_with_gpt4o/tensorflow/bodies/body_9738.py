# Extracted from ./data/repos/tensorflow/tensorflow/python/client/pywrap_tf_session.py
opts = TF_NewSessionOptions(target=target, config=config)
try:
    TF_Reset_wrapper(opts, containers)
finally:
    TF_DeleteSessionOptions(opts)
