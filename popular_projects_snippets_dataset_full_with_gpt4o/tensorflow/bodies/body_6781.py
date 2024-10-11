# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
strategy, _, _ = create_test_objects(num_gpus=1)
with ops.Graph().as_default(), strategy.scope():
    created_step = training_util.create_global_step()
    get_step = training_util.get_global_step()
    self.assertEqual(created_step, get_step,
                     msg=('created_step %s type %s vs. get_step %s type %s' %
                          (id(created_step), created_step.__class__.__name__,
                           id(get_step), get_step.__class__.__name__)))
    self.assertIs(resource_variable_ops.ResourceVariable, type(created_step))
    self.assertIs(resource_variable_ops.ResourceVariable, type(get_step))
    # All variables have an _distribute_strategy parameter. Only variable
    # subclasses in distribution strategy expose it publicly.
    self.assertFalse(hasattr(strategy, 'distribute_strategy'))
    self.assertIs(strategy, created_step._distribute_strategy)
