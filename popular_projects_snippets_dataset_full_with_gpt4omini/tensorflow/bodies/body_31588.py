# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# (data_format, use_gpu) tuple
if one_dimensional:
    configs0 = [
        ("NWC", False),
        ("NWC", True),
        ("NCW", True),
    ]
else:
    configs0 = [
        ("NHWC", False),
        ("NHWC", True),
        ("NCHW", True),
    ]
    # NCHW_VECT_C only supported for max_pool.
    if (v1_fn == nn_ops.max_pool or v1_fn == nn_ops.max_pool1d or
        v2_fn == nn_ops.max_pool_v2 or v2_fn == gen_nn_ops.max_pool_v2):
        configs0.append(("NCHW_VECT_C", True))

  # (data_format, use_gpu, data_type) tuple
configs1 = []
for data_format, use_gpu in configs0:
    configs1.append((data_format, use_gpu, dtypes.float32))

    # In our test, VECT_C always uses float32.  (It gets converted to int8 in
    # the test runner.)
    if data_format == "NCHW_VECT_C":
        continue

    configs1 += [(data_format, use_gpu, dtypes.float16),
                 (data_format, use_gpu, dtypes.float64)]

    if use_gpu:
        configs1 += [(data_format, use_gpu, dtypes.bfloat16)]

  # Convert from tuple to dict and add v1/v2 versions.
ret = []
for data_format, use_gpu, data_type in configs1:
    ret.append({
        "pool_func": v1_fn,
        "data_format": data_format,
        "data_type": data_type,
        "use_gpu": use_gpu,
        "v2": False
    })
    if v2_fn:
        ret.append({
            "pool_func": v2_fn,
            "data_format": data_format,
            "data_type": data_type,
            "use_gpu": use_gpu,
            "v2": False
        })
        ret.append({
            "pool_func": v2_fn,
            "data_format": data_format,
            "data_type": data_type,
            "use_gpu": use_gpu,
            "v2": True
        })

  # Filter out GPU configs if necessary.
if not allow_gpu:
    ret = [c for c in ret if not c["use_gpu"]]

exit(ret)
