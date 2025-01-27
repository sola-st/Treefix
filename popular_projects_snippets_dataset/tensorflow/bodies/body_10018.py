# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints tag-set, ops, SignatureDef, and Inputs/Outputs of SavedModel.

  Prints all tag-set, ops, SignatureDef and Inputs/Outputs information stored in
  SavedModel directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
  """
tag_sets = saved_model_utils.get_saved_model_tag_sets(saved_model_dir)
for tag_set in sorted(tag_sets):
    print("\nMetaGraphDef with tag-set: '%s' "
          "contains the following SignatureDefs:" % ', '.join(tag_set))

    tag_set = ','.join(tag_set)
    signature_def_map = get_signature_def_map(saved_model_dir, tag_set)
    for signature_def_key in sorted(signature_def_map.keys()):
        print('\nsignature_def[\'' + signature_def_key + '\']:')
        _show_inputs_outputs(saved_model_dir, tag_set, signature_def_key,
                             indent=1)
    _show_ops_in_metagraph(saved_model_dir, tag_set)
_show_defined_functions(saved_model_dir)
