# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Return a topologic sort of FunctionDefs in a library."""
edges = collections.defaultdict(list)
in_count = collections.defaultdict(lambda: 0)

for fname, deps in function_deps.items():
    for dep in deps:
        edges[dep].append(fname)
        in_count[fname] += 1
ready = [
    fdef.signature.name
    for fdef in library.function
    if in_count[fdef.signature.name] == 0
]
output = []
while ready:
    node = ready.pop()
    output.append(node)
    for dest in edges[node]:
        in_count[dest] -= 1
        if not in_count[dest]:
            ready.append(dest)

if len(output) != len(library.function):
    failed_to_resolve = sorted(set(in_count.keys()) - set(output))
    raise ValueError("There is a cyclic dependency between functions. ",
                     f"Could not resolve {failed_to_resolve}.")

reverse = {fdef.signature.name: fdef for fdef in library.function}
exit([reverse[x] for x in output])
