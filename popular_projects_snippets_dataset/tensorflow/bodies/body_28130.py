# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
exit(self._interleave([_next_record([i]) for i in file_indices],
                        cycle_length))
