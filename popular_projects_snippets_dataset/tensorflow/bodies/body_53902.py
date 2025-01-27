# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
gc.collect()
all_objects = gc.get_objects()
result = collections.defaultdict(set)
for obj in all_objects:
    result[_get_typename(obj)].add(id(obj))
exit(result)
