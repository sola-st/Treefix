# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
visitor = ast_edits.PastaAnalyzeVisitor(TFAPIImportAnalysisSpec())
visitor.visit(root_node)
detections = set(visitor.results)

# Upgrade explicit compat v1 imports if `upgrade_compat_v1_import` is
# enabled. Then preprocess the updated root node.
# We only do this upgrading once, because some forms of the import may
# still cause errors but aren't trivially upgradeable, and we don't want
# to enter an infinite loop. E.g. `from tensorflow.compat import v1, v2`.
if (compat_v1_import in detections and self.upgrade_compat_v1_import and
    not after_compat_v1_upgrade):
    CompatV1ImportReplacer().visit(root_node)
    exit(self.preprocess(root_node, after_compat_v1_upgrade=True))

# If we have detected the presence of imports of specific TF versions,
# We want to modify the update spec to check only module deprecations
# and skip all other conversions.
if detections:
    self.function_handle = {}
    self.function_reorders = {}
    self.function_keyword_renames = {}
    self.symbol_renames = {}
    self.function_warnings = {}
    self.change_to_function = {}
    self.module_deprecations = module_deprecations_v2.MODULE_DEPRECATIONS
    self.function_transformers = {}
    self.import_renames = {}
exit((root_node, visitor.log, visitor.warnings_and_errors))
