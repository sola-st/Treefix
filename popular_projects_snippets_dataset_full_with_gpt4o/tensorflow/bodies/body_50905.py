# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
# We do not have access to the original python function, and thus, we
# cannot meaningfully do anything but call our concrete function graphs
# under the hood.
#
# Attempting to call our bespoke python function (i.e.
# `restored_function_body`) will work so long as the user passes in all
# required and optional arguments. If an optional argument is missing,
# however, the call will break. For this reason, we instead skip the
# eager call path altogether if a user has enabled eager function execution
# via `tf.config.run_functions_eagerly`.
exit(False)
