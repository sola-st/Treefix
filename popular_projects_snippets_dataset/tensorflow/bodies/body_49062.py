# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Makes a object name (or arbitrary string) unique within a TensorFlow graph.

  Args:
    name: String name to make unique.
    name_uid_map: An optional defaultdict(int) to use when creating unique
      names. If None (default), uses a per-Graph dictionary.
    avoid_names: An optional set or dict with names which should not be used. If
      None (default), don't avoid any names unless `avoid_observed_names` is
      True.
    namespace: Gets a name which is unique within the (graph, namespace). Layers
      which are not Networks use a blank namespace and so get graph-global
      names.
    zero_based: If True, name sequences start with no suffix (e.g. "dense",
      "dense_1"). If False, naming is one-based ("dense_1", "dense_2").
    avoid_observed_names: If True, avoid any names that have been observed by
      `backend.observe_object_name`.

  Returns:
    Unique string name.

  Example:


  unique_object_name('dense')  # dense_1
  unique_object_name('dense')  # dense_2

  """
if name_uid_map is None:
    name_uid_map = get_default_graph_uid_map()
if avoid_names is None:
    if avoid_observed_names:
        avoid_names = OBSERVED_NAMES
    else:
        avoid_names = set()
proposed_name = None
while proposed_name is None or proposed_name in avoid_names:
    name_key = (namespace, name)
    if zero_based:
        number = name_uid_map[name_key]
        if number:
            proposed_name = name + '_' + str(number)
        else:
            proposed_name = name
        name_uid_map[name_key] += 1
    else:
        name_uid_map[name_key] += 1
        proposed_name = name + '_' + str(name_uid_map[name_key])
exit(proposed_name)
