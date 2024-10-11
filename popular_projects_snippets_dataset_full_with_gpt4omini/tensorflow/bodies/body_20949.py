# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py

def _write_v1_simple_saved_model(export_dir):
    # Create v1 Saved Model with single variable `w0` with value 5.0.
    builder = saved_model_builder.SavedModelBuilder(export_dir)
    with ops.Graph().as_default():
        _ = resource_variable_ops.ResourceVariable(5.0)
        with self.cached_session() as session:
            session.run(variables.global_variables_initializer())
            builder.add_meta_graph_and_variables(session, ['foo'])
    builder.save()

test_dir = _test_dir(self.get_temp_dir(), 'saved_model')
_write_v1_simple_saved_model(test_dir)

with ops.Graph().as_default():
    # Load saved model with `load_v1_in_v2`.
    model = saved_model_load.load(test_dir)
    w0 = model.variables[0]
    # Define operation that increments `w0`.
    w_add = w0.assign_add(1.)
    gstep = training_util.get_or_create_global_step()
    new_gstep = state_ops.assign_add(gstep, 1)

    with monitored_session.MonitoredTrainingSession(
        checkpoint_dir=test_dir) as session:
        w1 = session.run(w_add)
        self.assertEqual(w1, 6.)
        session.run(new_gstep)
        w2 = session.run(w_add)
        self.assertEqual(w2, 7.)

    # Stop and resume training.
    with monitored_session.MonitoredTrainingSession(
        checkpoint_dir=test_dir) as session:
        # `w0` saves its value of 7.
        w3 = session.run(w_add)
        self.assertEqual(w3, 8.)
