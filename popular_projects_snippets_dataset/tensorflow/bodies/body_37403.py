# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with summary_ops.create_file_writer_v2(logdir).as_default():
    summary_ops.write('tag', 1, step=0)
