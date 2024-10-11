# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
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
