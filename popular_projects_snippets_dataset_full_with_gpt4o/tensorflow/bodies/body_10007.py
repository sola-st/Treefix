# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints the keys for each SignatureDef in the SignatureDef map.

  Prints the list of SignatureDef keys from the SignatureDef map specified by
  the given tag-set and SavedModel directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
    tag_set: Group of tag(s) of the MetaGraphDef to get SignatureDef map from,
        in string format, separated by ','. For tag-set contains multiple tags,
        all tags must be passed in.
  """
signature_def_map = get_signature_def_map(saved_model_dir, tag_set)
print('The given SavedModel MetaGraphDef contains SignatureDefs with the '
      'following keys:')
for signature_def_key in sorted(signature_def_map.keys()):
    print('SignatureDef key: \"%s\"' % signature_def_key)
