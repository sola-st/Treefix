# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Function triggered by aot_compile_cpu command."""
checkpoint_path = (
    _SMCLI_CHECKPOINT_PATH.value
    or os.path.join(_SMCLI_DIR.value, 'variables/variables'))
if not _SMCLI_VARIABLES_TO_FEED.value:
    variables_to_feed = []
elif _SMCLI_VARIABLES_TO_FEED.value.lower() == 'all':
    variables_to_feed = None  # We will identify them after.
else:
    variables_to_feed = _SMCLI_VARIABLES_TO_FEED.value.split(',')

saved_model_aot_compile.aot_compile_cpu_meta_graph_def(
    checkpoint_path=checkpoint_path,
    meta_graph_def=saved_model_utils.get_meta_graph_def(
        _SMCLI_DIR.value, _SMCLI_TAG_SET.value),
    signature_def_key=_SMCLI_SIGNATURE_DEF_KEY.value,
    variables_to_feed=variables_to_feed,
    output_prefix=_SMCLI_OUTPUT_PREFIX.value,
    target_triple=_SMCLI_TARGET_TRIPLE.value,
    target_cpu=_SMCLI_TARGET_CPU.value,
    cpp_class=_SMCLI_CPP_CLASS.value,
    multithreading=(
        _SMCLI_MULTITHREADING.value.lower() not in ('f', 'false', '0')))
