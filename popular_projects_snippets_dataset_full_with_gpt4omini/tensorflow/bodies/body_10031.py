# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Function triggered by scan command."""
if _SMCLI_TAG_SET.value and _SMCLI_OP_DENYLIST.value:
    scan_meta_graph_def(
        saved_model_utils.get_meta_graph_def(
            _SMCLI_DIR.value, _SMCLI_TAG_SET.value),
        _get_op_denylist_set(_SMCLI_OP_DENYLIST.value))
elif _SMCLI_TAG_SET.value:
    scan_meta_graph_def(
        saved_model_utils.get_meta_graph_def(
            _SMCLI_DIR.value, _SMCLI_TAG_SET.value),
        _OP_DENYLIST)
else:
    saved_model = saved_model_utils.read_saved_model(_SMCLI_DIR.value)
    if _SMCLI_OP_DENYLIST.value:
        for meta_graph_def in saved_model.meta_graphs:
            scan_meta_graph_def(meta_graph_def,
                                _get_op_denylist_set(_SMCLI_OP_DENYLIST.value))
    else:
        for meta_graph_def in saved_model.meta_graphs:
            scan_meta_graph_def(meta_graph_def, _OP_DENYLIST)
