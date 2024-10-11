# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Falls back to calling the function unconverted, in case of error."""
# TODO(mdan): Consider adding an internal metric.
warning_template = (
    'AutoGraph could not transform %s and will run it as-is.\n'
    '%s'
    'Cause: %s\n'
    'To silence this warning, decorate the function with'
    ' @tf.autograph.experimental.do_not_convert')
if isinstance(exc, errors.InaccessibleSourceCodeError):
    if ag_ctx.INSPECT_SOURCE_SUPPORTED:
        logging.warning(warning_template, f, '', exc)
elif isinstance(exc, errors.UnsupportedLanguageElementError):
    if not conversion.is_in_allowlist_cache(f, options):
        logging.warning(warning_template, f, '', exc)
else:
    file_bug_message = (
        'Please report this to the TensorFlow team. When filing the bug, set'
        ' the verbosity to 10 (on Linux, `export AUTOGRAPH_VERBOSITY=10`) and'
        ' attach the full output.\n')
    logging.warning(warning_template, f, file_bug_message, exc)

exit(_call_unconverted(f, args, kwargs, options))
