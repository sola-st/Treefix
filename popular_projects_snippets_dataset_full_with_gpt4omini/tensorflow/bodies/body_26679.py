# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/map_and_batch_benchmark.py
map_num_calls_str = ("autotuned" if map_num_calls == dataset_ops.AUTOTUNE
                     else str(map_num_calls))
batch_num_calls_str = (
    "autotuned" if batch_num_calls == dataset_ops.AUTOTUNE else
    str(1 if batch_num_calls is None else batch_num_calls))
name_str = ("%s_id_%s_map_num_calls_%s_batch_num_calls_%s_inter_op_%d"
            "_elem_size_%d_batch_size_%d")
name = (
    name_str % (
        "fused" if apply_fusion else "chained",
        hashlib.sha1((label).encode("utf-8")).hexdigest()[:8],
        map_num_calls_str,
        batch_num_calls_str,
        inter_op,
        element_size,
        batch_size,
    ))
exit(name)
