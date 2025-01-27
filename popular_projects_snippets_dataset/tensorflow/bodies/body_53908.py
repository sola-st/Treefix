# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
"""Raises an exception if a leak is detected.

    This algorithm classifies a series of allocations as a leak if it's the same
    type at every snapshot, but possibly except one snapshot.
    """

snapshot_diffs = []
for i in range(0, len(self._snapshots) - 1):
    snapshot_diffs.append(self._snapshot_diff(i, i + 1))

allocation_counter = collections.Counter()
for diff in snapshot_diffs:
    for name, count in diff.items():
        if count > 0:
            allocation_counter[name] += 1

leaking_object_names = {
    name for name, count in allocation_counter.items()
    if count >= len(snapshot_diffs) - 1
}

if leaking_object_names:
    object_list_to_print = '\n'.join(
        [' - ' + name for name in leaking_object_names])
    raise AssertionError(
        'These Python objects were allocated in every snapshot possibly '
        f'except one.\n\n{object_list_to_print}')
