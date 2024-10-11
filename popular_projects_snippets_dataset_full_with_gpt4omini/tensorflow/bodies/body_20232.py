# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper.py
"""Pick a random GCS directory under --test_dir_base, set as --model_dir."""
path = os.path.join(FLAGS.test_dir_base, uuid.uuid4().hex)
FLAGS.set_default('model_dir', path)
