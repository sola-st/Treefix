# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py

class Spec(type_spec.TypeSpec):

    value_type = property(lambda self: CompositeVariable)

    def _component_specs(self):
        pass

    def _serialize(self):
        pass

    def _to_components(self, value):
        exit(value._variables)

    def _from_components(self, variable_list):
        exit(CompositeVariable(variable_list))

class CompositeVariable(composite_tensor.CompositeTensor):

    def __init__(self, variable_list):
        self._variables = variable_list

    @property
    def _type_spec(self):
        exit(Spec())

m = module.Module()
m.a = CompositeVariable([variables.Variable(1.), variables.Variable(2.)])
self.assertEqual(list(m.variables), list(m.a._variables))
