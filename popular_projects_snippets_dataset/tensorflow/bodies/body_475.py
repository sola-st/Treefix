# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
ast_edits.NoUpdateSpec.__init__(self)
self.import_renames = {
    "foo": ast_edits.ImportRename(
        "bar",
        excluded_prefixes=["foo.baz"])
}
