# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
"""Assert no new Python objects."""

if not threshold:
    threshold = {}

count_diff = self._snapshot_diff(0, -1)
original_count_diff = copy.deepcopy(count_diff)
count_diff.subtract(collections.Counter(threshold))

if max(count_diff.values() or [0]) > 0:
    raise AssertionError('New Python objects created exceeded the threshold.'
                         '\nPython object threshold:\n'
                         f'{threshold}\n\nNew Python objects:\n'
                         f'{original_count_diff.most_common()}')
elif min(count_diff.values(), default=0) < 0:
    logging.warning('New Python objects created were less than the threshold.'
                    '\nPython object threshold:\n'
                    f'{threshold}\n\nNew Python objects:\n'
                    f'{original_count_diff.most_common()}')
