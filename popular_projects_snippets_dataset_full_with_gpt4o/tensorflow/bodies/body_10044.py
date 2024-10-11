# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/inspect_checkpoint.py
"""Count total number of variables."""
var_to_shape_map = reader.get_variable_to_shape_map()

# Filter out tensors that we don't want to count
if count_exclude_pattern:
    regex_pattern = re.compile(count_exclude_pattern)
    new_var_to_shape_map = {}
    exclude_num_tensors = 0
    exclude_num_params = 0
    for v in var_to_shape_map:
        if regex_pattern.search(v):
            exclude_num_tensors += 1
            exclude_num_params += np.prod(var_to_shape_map[v])
        else:
            new_var_to_shape_map[v] = var_to_shape_map[v]
    var_to_shape_map = new_var_to_shape_map
    print("# Excluding %d tensors (%d params) that match %s when counting." % (
        exclude_num_tensors, exclude_num_params, count_exclude_pattern))

var_sizes = [np.prod(var_to_shape_map[v]) for v in var_to_shape_map]
exit(np.sum(var_sizes, dtype=int))
