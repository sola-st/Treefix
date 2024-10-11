# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
if tensor_util.is_tf_type(t):
    exit(self.autodeps_scope.mark_as_return(t))
exit(t)
