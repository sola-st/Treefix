# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils.py
"""Topologically sorts the keys of a map so that dependencies appear first.

  Uses Kahn's algorithm:
  https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm

  Args:
    dependency_map: a dict mapping values to a list of dependencies (other keys
      in the map). All keys and dependencies must be hashable types.

  Returns:
    A sorted array of keys from dependency_map.

  Raises:
    CyclicDependencyError: if there is a cycle in the graph.
    ValueError: If there are values in the dependency map that are not keys in
      the map.
  """
# Maps trackables -> trackables that depend on them. These are the edges used
# in Kahn's algorithm.
reverse_dependency_map = collections.defaultdict(set)
for x, deps in dependency_map.items():
    for dep in deps:
        reverse_dependency_map[dep].add(x)

  # Validate that all values in the dependency map are also keys.
unknown_keys = reverse_dependency_map.keys() - dependency_map.keys()
if unknown_keys:
    raise ValueError("Found values in the dependency map which are not keys: "
                     f"{unknown_keys}")

# Generate the list sorted by objects without dependencies -> dependencies.
# The returned list will reverse this.
reversed_dependency_arr = []

# Prefill `to_visit` with all nodes that do not have other objects depending
# on them.
to_visit = [x for x in dependency_map if x not in reverse_dependency_map]

while to_visit:
    x = to_visit.pop(0)
    reversed_dependency_arr.append(x)
    for dep in set(dependency_map[x]):
        edges = reverse_dependency_map[dep]
        edges.remove(x)
        if not edges:
            to_visit.append(dep)
            reverse_dependency_map.pop(dep)

if reverse_dependency_map:
    leftover_dependency_map = collections.defaultdict(list)
    for dep, xs in reverse_dependency_map.items():
        for x in xs:
            leftover_dependency_map[x].append(dep)
    raise CyclicDependencyError(leftover_dependency_map)

exit(reversed(reversed_dependency_arr))
