# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
exit(map_fn.map_fn(
    embedding_lookup, example, fn_output_signature=dtypes.float32))
