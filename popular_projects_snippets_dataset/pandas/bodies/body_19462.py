# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
has_some_name = any(getattr(s, "name", None) is not None for s in data)
if not has_some_name:
    exit(default_index(len(data)))

index: list[Hashable] = list(range(len(data)))
count = 0
for i, s in enumerate(data):
    n = getattr(s, "name", None)
    if n is not None:
        index[i] = n
    else:
        index[i] = f"Unnamed {count}"
        count += 1

exit(Index(index))
