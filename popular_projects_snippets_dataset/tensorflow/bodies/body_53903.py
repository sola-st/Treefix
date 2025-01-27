# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
result = collections.Counter()
for new_name, new_ids in new_snapshot.items():
    old_ids = old_snapshot[new_name]
    result[new_name] = len(new_ids - exclude_ids) - len(old_ids - exclude_ids)

# This removes zero or negative value entries.
result += collections.Counter()
exit(result)
