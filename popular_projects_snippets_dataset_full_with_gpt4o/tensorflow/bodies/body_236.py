# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Handle visiting an import node in the AST.

    Args:
      node: Current Node
    """
new_aliases = []
import_updated = False
import_renames = getattr(self._api_change_spec, "import_renames", {})
max_submodule_depth = getattr(self._api_change_spec, "max_submodule_depth",
                              1)
inserts_after_imports = getattr(self._api_change_spec,
                                "inserts_after_imports", {})

# This loop processes imports in the format
# import foo as f, bar as b
for import_alias in node.names:
    all_import_components = import_alias.name.split(".")
    # Look for rename, starting with longest import levels.
    found_update = False
    for i in reversed(list(range(1, max_submodule_depth + 1))):
        import_component = all_import_components[0]
        for j in range(1, min(i, len(all_import_components))):
            import_component += "." + all_import_components[j]
        import_rename_spec = import_renames.get(import_component, None)

        if not import_rename_spec or excluded_from_module_rename(
            import_alias.name, import_rename_spec):
            continue

        new_name = (
            import_rename_spec.new_name +
            import_alias.name[len(import_component):])

        # If current import is
        #   import foo
        # then new import should preserve imported name:
        #   import new_foo as foo
        # This happens when module has just one component.
        new_asname = import_alias.asname
        if not new_asname and "." not in import_alias.name:
            new_asname = import_alias.name

        new_alias = ast.alias(name=new_name, asname=new_asname)
        new_aliases.append(new_alias)
        import_updated = True
        found_update = True

        # Insert any followup lines that should happen after this import.
        full_import = (import_alias.name, import_alias.asname)
        insert_offset = 1
        for line_to_insert in inserts_after_imports.get(full_import, []):
            assert self._stack[-1] is node
            parent = self._stack[-2]

            new_line_node = pasta.parse(line_to_insert)
            ast.copy_location(new_line_node, node)
            parent.body.insert(
                parent.body.index(node) + insert_offset, new_line_node)
            insert_offset += 1

            # Insert a newline after the import if necessary
            old_suffix = pasta.base.formatting.get(node, "suffix")
            if old_suffix is None:
                old_suffix = os.linesep
            if os.linesep not in old_suffix:
                pasta.base.formatting.set(node, "suffix", old_suffix + os.linesep)

            # Apply indentation to new node.
            pasta.base.formatting.set(new_line_node, "prefix",
                                      pasta.base.formatting.get(node, "prefix"))
            pasta.base.formatting.set(new_line_node, "suffix", os.linesep)
            self.add_log(
                INFO, node.lineno, node.col_offset,
                "Adding `%s` after import of %s" %
                (new_line_node, import_alias.name))
        # Find one match, break
        if found_update:
            break
      # No rename is found for all levels
    if not found_update:
        new_aliases.append(import_alias)  # no change needed

    # Replace the node if at least one import needs to be updated.
if import_updated:
    assert self._stack[-1] is node
    parent = self._stack[-2]

    new_node = ast.Import(new_aliases)
    ast.copy_location(new_node, node)
    pasta.ast_utils.replace_child(parent, node, new_node)
    self.add_log(
        INFO, node.lineno, node.col_offset,
        "Changed import from %r to %r." %
        (pasta.dump(node), pasta.dump(new_node)))

self.generic_visit(node)
