# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
segments = [FLAGS.model_dir, name] + ([subdir] if subdir else [])
exit(os.path.join(*segments))
