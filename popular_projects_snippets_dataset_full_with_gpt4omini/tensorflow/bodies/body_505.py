# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
self.symbols_to_detect = {}
self.imports_to_detect = {
    ("tensorflow", None): UnaliasedTFImport(),
    ("tensorflow.compat.v1", "tf"): compat_v1_import,
    ("tensorflow.compat.v2", "tf"): compat_v2_import,
}
