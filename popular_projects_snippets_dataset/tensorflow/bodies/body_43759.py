# Extracted from ./data/repos/tensorflow/tensorflow/python/pywrap_mlir.py
exit(ExperimentalConvertSavedModelV1ToMlirLite(
    str(saved_model_path).encode('utf-8'),
    str(exported_names).encode('utf-8'),
    str(tags).encode('utf-8'), upgrade_legacy, show_debug_info))
