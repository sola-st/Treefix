# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
class DangerousModule(module.Module):
    _TF_MODULE_IGNORED_PROPERTIES = frozenset(itertools.chain(
        ("dangerous_submodule", "dangerous_variable"),
        module.Module._TF_MODULE_IGNORED_PROPERTIES
    ))

mod = DangerousModule()
mod.dangerous_submodule = module.Module()
mod.dangerous_variable = variables.Variable(1.)
mod.normal_variable = variables.Variable(2.)

self.assertEmpty(mod.submodules)
self.assertLen(mod.variables, 1)
self.assertEqual(mod.variables[0], mod.normal_variable)
