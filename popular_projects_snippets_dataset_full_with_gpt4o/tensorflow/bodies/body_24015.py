# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mirrored = distributed_values.MirroredVariable(
    None, [variables.Variable(1.)], variables.VariableAggregation.SUM)
tpu = tpu_values.TPUMirroredVariable(
    strategy=None, values=[variables.Variable(42.)], aggregation=None)
aggregating = ps_values.AggregatingVariable(
    strategy=None, v=variables.Variable(1.), aggregation=None)

m = module.Module()
m.a = mirrored
m.b = tpu
m.c = aggregating
self.assertEqual(m.variables, (mirrored, tpu, aggregating))
