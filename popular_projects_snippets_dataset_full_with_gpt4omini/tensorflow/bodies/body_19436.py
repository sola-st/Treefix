# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_base_test.py
if FLAGS.project is not None or FLAGS.zone is not None:
    self.skipTest(
        'Skipping tests for oss as it is slow to run every test in cloud tpu.'
    )
