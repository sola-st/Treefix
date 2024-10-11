# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column.py
"""Add embedding variable name and scope to collection."""
g = ops.get_default_graph()
collection = g.get_collection_ref(_TPU_FC_TO_SCOPE)
if not collection:
    collection.append({})

var_def_dict = collection[0]

captured_scope = variable_scope.get_variable_scope()
captured_scope_name = captured_scope.name

if embedding_var_name in var_def_dict:
    if (var_def_dict[embedding_var_name][0] != captured_scope_name and
        not is_shared_embedding and not bypass_scope_validation):
        raise ValueError(
            'For embedding var name {}, the variable scope name is different, '
            'got {}; expected {}'.format(embedding_var_name,
                                         captured_scope_name,
                                         var_def_dict[embedding_var_name][0]))
    if var_def_dict[embedding_var_name][1] != embedding_var_name_in_fc:
        raise ValueError(
            'For embedding var name {}, the embedding name is different, '
            'got {}; expected {}'.format(embedding_var_name,
                                         embedding_var_name_in_fc,
                                         var_def_dict[embedding_var_name][1]))
else:
    var_def_dict[embedding_var_name] = (captured_scope_name,
                                        embedding_var_name_in_fc)
