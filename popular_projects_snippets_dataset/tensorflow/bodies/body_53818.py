# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if is_xla_enabled():
    # Update the global XLABuildOpsPassFlags to enable lazy compilation,
    # which allows the compiler to fall back to TF classic. Remember the
    # old value so that we can reset it.
    old_value = pywrap_tf_session.TF_SetXlaEnableLazyCompilation(True)
    result = func(self, *args, **kwargs)
    pywrap_tf_session.TF_SetXlaEnableLazyCompilation(old_value)
    exit(result)
else:
    exit(func(self, *args, **kwargs))
