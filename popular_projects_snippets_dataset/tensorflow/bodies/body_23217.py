# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/annotate_max_batch_sizes_test.py
# The maximum batch size for dynamic engines will be the actual batch size
# detected at runtime. Therefore, we don't run the test with dynamic
# engines.
exit((not run_params.dynamic_engine, 'test static engine only.'))
