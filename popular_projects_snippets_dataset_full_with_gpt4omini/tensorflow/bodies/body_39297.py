# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/benchmarks_test.py
checkpoint_path = _save_checkpoint()
all_names, all_dtypes = zip(*py_checkpoint_reader.NewCheckpointReader(
    checkpoint_path).get_variable_to_dtype_map().items())

def _call_restore_v2():
    gen_io_ops.restore_v2(checkpoint_path, all_names, [""] * len(all_names),
                          all_dtypes)

self._run(_call_restore_v2, 3)
