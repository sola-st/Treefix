# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Create v1 Saved Model with single variable `w0` with value 5.0.
builder = saved_model_builder.SavedModelBuilder(export_dir)
with ops.Graph().as_default():
    _ = resource_variable_ops.ResourceVariable(5.0)
    with self.cached_session() as session:
        session.run(variables.global_variables_initializer())
        builder.add_meta_graph_and_variables(session, ['foo'])
builder.save()
