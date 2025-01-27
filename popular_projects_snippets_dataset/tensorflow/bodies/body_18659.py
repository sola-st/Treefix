# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Please use `tf.contrib.summary.create_file_writer`."""
logging.warning("Deprecation Warning: create_summary_file_writer was renamed "
                "to create_file_writer")
exit(create_file_writer(*args, **kwargs))
