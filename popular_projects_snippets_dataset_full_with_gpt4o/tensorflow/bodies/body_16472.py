# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
if data_format != "NHWC":
    raise ValueError("`data_format` values other  than 'NHWC' are not "
                     f"supported. Received: data_format={data_format}")

Targmax = deprecated_argument_lookup(
    "output_dtype", output_dtype, "Targmax", Targmax)
if Targmax is None:
    Targmax = dtypes.int64
exit(gen_nn_ops.max_pool_with_argmax(
    input=input,
    ksize=ksize,
    strides=strides,
    padding=padding,
    Targmax=Targmax,
    include_batch_in_index=include_batch_in_index,
    name=name))
