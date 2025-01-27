# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Add imports for all destination modules in self._module_imports."""
# Import all required modules in their parent modules.
# For e.g. if we import 'foo.bar.Value'. Then, we also
# import 'bar' in 'foo'.
imported_modules = set(self._module_imports.keys())
for module in imported_modules:
    if not module:
        continue
    module_split = module.split('.')
    parent_module = ''  # we import submodules in their parent_module

    for submodule_index in range(len(module_split)):
        if submodule_index > 0:
            submodule = module_split[submodule_index - 1]
            parent_module += '.' + submodule if parent_module else submodule
        import_from = self._output_package
        if self._lazy_loading:
            import_from += '.' + '.'.join(module_split[:submodule_index + 1])
            self.add_import(
                symbol=None,
                source_module_name='',
                source_name=import_from,
                dest_module_name=parent_module,
                dest_name=module_split[submodule_index])
        else:
            if self._use_relative_imports:
                import_from = '.'
            elif submodule_index > 0:
                import_from += '.' + '.'.join(module_split[:submodule_index])
            self.add_import(
                symbol=None,
                source_module_name=import_from,
                source_name=module_split[submodule_index],
                dest_module_name=parent_module,
                dest_name=module_split[submodule_index])
