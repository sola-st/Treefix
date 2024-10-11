# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
g = ops.Graph()
with g.as_default():
    variables.Variable(10.0, name="v")
# Export and import the graph into a new graph.
g_copy = self._ExportAndImportGraph(g)
with g_copy.as_default():
    ema = moving_averages.ExponentialMovingAverage(0.25, name="foo_avg")
    vars_to_restore = ema.variables_to_restore()
    # There should only be one variable in vars_to_restore. This is important
    # to check because when importing from a GraphDef, TF makes duplicate
    # python Variable objects referring to the same underlying variable. We
    # need to be sure that two variables referring to the same variable don't
    # both get added to vars_to_restore.
    self.assertEqual(len(vars_to_restore), 1)
    self.assertIn("v/foo_avg", vars_to_restore)
