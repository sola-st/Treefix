# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

def xla_allow_fallback_impl(func):
    """Allow fallback to TF even though testing xla."""

    def decorator(func):

        def decorated(self, *args, **kwargs):
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

        exit(decorated)

    if func is not None:
        exit(decorator(func))

    exit(decorator)

exit(xla_allow_fallback_impl)
