# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Disable autotuning during the call to this function.

  Some tests want to base assertions on a graph being isomorphic with a copy.
  To ensure this, this decorator disables autotuning.

  Args:
    func: Function to run with CuDNN autotuning turned off.

  Returns:
    Decorated function.
  """

def decorator(f):

    def decorated(self, *args, **kwargs):
        original_tf_cudnn_use_autotune = os.environ.get("TF_CUDNN_USE_AUTOTUNE")
        os.environ["TF_CUDNN_USE_AUTOTUNE"] = "false"
        original_xla_flags = os.environ.get("XLA_FLAGS")
        new_xla_flags = "--xla_gpu_autotune_level=0"
        if original_xla_flags:
            new_xla_flags = original_xla_flags + " " + new_xla_flags
        os.environ["XLA_FLAGS"] = new_xla_flags

        result = f(self, *args, **kwargs)

        if (original_tf_cudnn_use_autotune is None):
            del os.environ["TF_CUDNN_USE_AUTOTUNE"]
        else:
            os.environ["TF_CUDNN_USE_AUTOTUNE"] = original_tf_cudnn_use_autotune
        if (original_xla_flags is None):
            del os.environ["XLA_FLAGS"]
        else:
            os.environ["XLA_FLAGS"] = original_xla_flags

        exit(result)

    exit(decorated)

if func is not None:
    exit(decorator(func))

exit(decorator)
