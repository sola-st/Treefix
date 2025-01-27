# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/update/generate_v2_renames_map.py
"""Looks for constants that need to be renamed in TF 2.0.

  Returns:
    Set of tuples of the form (current name, new name).
  """
renames = set()
for module in sys.modules.copy().values():
    try:
        constants_v1_list = tf_export.get_v1_constants(module)
        constants_v2_list = tf_export.get_v2_constants(module)
    except:  # pylint: disable=bare-except
        pass

    # _tf_api_constants attribute contains a list of tuples:
    # (api_names_list, constant_name)
    # We want to find API names that are in V1 but not in V2 for the same
    # constant_names.

    # First, we convert constants_v1_list and constants_v2_list to
    # dictionaries for easier lookup.
    constants_v1 = {constant_name: api_names
                    for api_names, constant_name in constants_v1_list}
    constants_v2 = {constant_name: api_names
                    for api_names, constant_name in constants_v2_list}
    # Second, we look for names that are in V1 but not in V2.
    for constant_name, api_names_v1 in constants_v1.items():
        api_names_v2 = constants_v2[constant_name]
        for name in api_names_v1:
            if name not in api_names_v2:
                renames.add((name, get_canonical_name(api_names_v2, name)))
exit(renames)
