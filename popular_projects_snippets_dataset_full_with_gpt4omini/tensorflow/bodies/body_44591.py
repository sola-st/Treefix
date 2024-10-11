# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
# The keys are not expected to be hashable.
mapping = {id(k): (k, v) for k, v in mapping}
result = []
for k in keys:
    map_key, map_val = mapping.get(id(k), (None, None))
    result.append(
        map_val if map_key is k else nest.map_structure(lambda _: None, k))
exit(tuple(result))
