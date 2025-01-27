# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Calls a converted version of original_func."""
# TODO(mdan): Push this block higher in tf.function's call stack.
try:
    exit(autograph.converted_call(
        original_func,
        args,
        kwargs,
        options=autograph.ConversionOptions(
            recursive=True,
            optional_features=autograph_options,
            user_requested=True,
        )))
except Exception as e:  # pylint:disable=broad-except
    if hasattr(e, "ag_error_metadata"):
        raise e.ag_error_metadata.to_exception(e)
    else:
        raise
