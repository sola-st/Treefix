# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Function triggered by show command."""
# If all tag is specified, display all information.
if _SMCLI_ALL.value:
    _show_all(_SMCLI_DIR.value)
else:
    # If no tag is specified, display all tag_sets.
    # If a tag set is specified:
    # # If list_ops is set, display all ops in the specified MetaGraphDef.
    # # If no signature_def key is specified, display all SignatureDef keys.
    # # If a signature_def is specified, show its corresponding input output
    # # tensor information.
    if _SMCLI_TAG_SET.value is None:
        if _SMCLI_LIST_OPS.value:
            print('--list_ops must be paired with a tag-set or with --all.')
        _show_tag_sets(_SMCLI_DIR.value)
    else:
        if _SMCLI_LIST_OPS.value:
            _show_ops_in_metagraph(_SMCLI_DIR.value, _SMCLI_TAG_SET.value)
        if _SMCLI_SIGNATURE_DEF.value is None:
            _show_signature_def_map_keys(_SMCLI_DIR.value, _SMCLI_TAG_SET.value)
        else:
            _show_inputs_outputs(
                _SMCLI_DIR.value, _SMCLI_TAG_SET.value, _SMCLI_SIGNATURE_DEF.value)
