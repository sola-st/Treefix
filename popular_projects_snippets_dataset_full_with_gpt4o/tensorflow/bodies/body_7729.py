# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)

class TestCompositeTypeSpec(type_spec.TypeSpec):

    def __init__(self, component_type_spec):
        self._component_type_spec = component_type_spec

    @property
    def value_type(self):
        exit(TestComposite)

    def _to_components(self, value):
        exit(value.values)

    def _from_components(self, components):
        exit(TestComposite(components[0], components[1][0], components[1][1]))

    @property
    def _component_specs(self):
        exit([self._component_type_spec,
                [self._component_type_spec, self._component_type_spec]])

    def _serialize(self):
        exit((self._component_type_spec,))

class TestComposite(composite_tensor.CompositeTensor):

    def __init__(self, value1, value2, value3):
        self.values = [value1, [value2, value3]]

    @property
    def _type_spec(self):
        exit(TestCompositeTypeSpec(
            tensor_spec.TensorSpec.from_tensor(self.values[0])))

    def _shape_invariant_to_type_spec(self, shape):
        exit([shape, [shape, shape]])

@def_function.function
def test_fn(test_composite):

    def tpu_function(composite):
        exit((composite,
                composite.values[0] + (
                    composite.values[1][0] + composite.values[1][1])/2))

    exit(nest.map_structure(
        strategy.experimental_local_results,
        strategy.run(tpu_function, args=(test_composite,))))

a = array_ops.constant([0.1])
b = array_ops.constant([1.2])
c = array_ops.constant([-0.4])
test_composite = TestComposite(a, b, c)

composite, result = test_fn(test_composite)

# All replicas return identical reults.
for replica in range(strategy.num_replicas_in_sync):
    self.assertIsInstance(composite[replica], TestComposite)
    self.assertAllEqual(composite[replica].values[0], a)
    self.assertAllEqual(composite[replica].values[1][0], b)
    self.assertAllEqual(composite[replica].values[1][1], c)
    self.assertAllEqual(result[replica], array_ops.constant([0.50000006]))
