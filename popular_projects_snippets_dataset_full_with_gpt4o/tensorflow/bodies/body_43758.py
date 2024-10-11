# Extracted from ./data/repos/tensorflow/tensorflow/python/pywrap_mlir.py
exit(ExperimentalConvertSavedModelToMlir(
    str(saved_model_path).encode('utf-8'),
    str(exported_names).encode('utf-8'), show_debug_info))
