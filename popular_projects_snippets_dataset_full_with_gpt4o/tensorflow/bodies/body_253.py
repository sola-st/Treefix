# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety.py
self.function_keyword_renames = {}
self.symbol_renames = {}
self.change_to_function = {}
self.function_reorders = {}
self.function_warnings = {}
self.function_transformers = {}
self.module_deprecations = module_deprecations_v2.MODULE_DEPRECATIONS

## Inform about the addons mappings
for symbol, replacement in all_renames_v2.addons_symbol_mappings.items():
    warning = (
        ast_edits.WARNING, (
            "(Manual edit required) `{}` has been migrated to `{}` in "
            "TensorFlow Addons. The API spec may have changed during the "
            "migration. Please see https://github.com/tensorflow/addons "
            "for more info.").format(symbol, replacement))
    self.function_warnings[symbol] = warning

# List module renames. If changed, please update max_submodule_depth.
self.import_renames = {
    "tensorflow":
        ast_edits.ImportRename(
            "tensorflow.compat.v1",
            excluded_prefixes=[
                "tensorflow.contrib", "tensorflow.flags",
                "tensorflow.compat",
                "tensorflow.compat.v1", "tensorflow.compat.v2",
                "tensorflow.google"
            ],
        )
}
# Needs to be updated if self.import_renames is changed.
self.max_submodule_depth = 2
