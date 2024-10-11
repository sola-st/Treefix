# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
if self._extra_locals is None:
    # TODO(mdan): Move into core or replace with an actual importable module.
    # Craft a module that exposes the external API as well as certain
    # internal modules.
    module_spec = importlib.machinery.ModuleSpec('autograph', None)
    ag_internal = importlib.util.module_from_spec(module_spec)
    ag_internal.__dict__.update(inspect.getmodule(PyToTF).__dict__)
    ag_internal.ConversionOptions = converter.ConversionOptions
    ag_internal.STD = converter.STANDARD_OPTIONS
    ag_internal.Feature = converter.Feature
    ag_internal.utils = utils
    ag_internal.FunctionScope = function_wrappers.FunctionScope
    ag_internal.with_function_scope = function_wrappers.with_function_scope
    # TODO(mdan): Add safeguards against name clashes.
    # We don't want to create a submodule because we want the operators to be
    # accessible as ag__.<operator>
    ag_internal.__dict__.update(special_functions.__dict__)
    ag_internal.__dict__.update(operators.__dict__)

    self._extra_locals = {'ag__': ag_internal}
exit(self._extra_locals)
