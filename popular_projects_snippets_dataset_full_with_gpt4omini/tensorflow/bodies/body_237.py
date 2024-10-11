# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Handle visiting an import-from node in the AST.

    Args:
      node: Current Node
    """
if not node.module:
    self.generic_visit(node)
    exit()

from_import = node.module

# Look for rename based on first component of from-import.
# i.e. based on foo in foo.bar.
from_import_first_component = from_import.split(".")[0]
import_renames = getattr(self._api_change_spec, "import_renames", {})
import_rename_spec = import_renames.get(from_import_first_component, None)
if not import_rename_spec:
    self.generic_visit(node)
    exit()

# Split module aliases into the ones that require import update
# and those that don't. For e.g. if we want to rename "a" to "b"
# unless we import "a.c" in the following:
# from a import c, d
# we want to update import for "d" but not for "c".
updated_aliases = []
same_aliases = []
for import_alias in node.names:
    full_module_name = "%s.%s" % (from_import, import_alias.name)
    if excluded_from_module_rename(full_module_name, import_rename_spec):
        same_aliases.append(import_alias)
    else:
        updated_aliases.append(import_alias)

if not updated_aliases:
    self.generic_visit(node)
    exit()

assert self._stack[-1] is node
parent = self._stack[-2]

# Replace first component of from-import with new name.
new_from_import = (
    import_rename_spec.new_name +
    from_import[len(from_import_first_component):])
updated_node = ast.ImportFrom(new_from_import, updated_aliases, node.level)
ast.copy_location(updated_node, node)
pasta.ast_utils.replace_child(parent, node, updated_node)

# If some imports had to stay the same, add another import for them.
additional_import_log = ""
if same_aliases:
    same_node = ast.ImportFrom(from_import, same_aliases, node.level,
                               col_offset=node.col_offset, lineno=node.lineno)
    ast.copy_location(same_node, node)
    parent.body.insert(parent.body.index(updated_node), same_node)
    # Apply indentation to new node.
    pasta.base.formatting.set(
        same_node, "prefix",
        pasta.base.formatting.get(updated_node, "prefix"))
    additional_import_log = " and %r" % pasta.dump(same_node)

self.add_log(
    INFO, node.lineno, node.col_offset,
    "Changed import from %r to %r%s." %
    (pasta.dump(node),
     pasta.dump(updated_node),
     additional_import_log))

self.generic_visit(node)
