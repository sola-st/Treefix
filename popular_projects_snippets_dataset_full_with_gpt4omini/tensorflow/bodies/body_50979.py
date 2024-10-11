# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_signature_defs")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Graph with a single variable and a single entry in the signature def
    # map.  SavedModel is invoked to add with weights.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        # Build and populate an empty SignatureDef for testing.
        foo_signature = signature_def_utils.build_signature_def(
            dict(), dict(), "foo")
        builder.add_meta_graph_and_variables(
            sess, ["foo"], signature_def_map={"foo_key": foo_signature})

    # Graph with the same single variable and multiple entries in the
    # signature def map. No weights are saved by SavedModel.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 43)
        # Build and populate a different SignatureDef for testing.
        bar_signature = signature_def_utils.build_signature_def(
            dict(), dict(), "bar")
        # Also, build a different SignatureDef corresponding to "foo_key"
        # defined in the previous graph.
        foo_new_signature = signature_def_utils.build_signature_def(
            dict(), dict(), "foo_new")
        builder.add_meta_graph(["bar"],
                               signature_def_map={
                                   "bar_key": bar_signature,
                                   "foo_key": foo_new_signature
                               })

    # Save the SavedModel to disk.
    builder.save()

    # Restore the graph with tag "foo". The single entry in the SignatureDef
    # map corresponding to "foo_key" should exist.
    with self.session(graph=ops.Graph()) as sess:
        foo_graph = loader.load(sess, ["foo"], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

        foo_signature = foo_graph.signature_def
        self.assertEqual(len(foo_signature), 1)
        self.assertEqual("foo", foo_signature["foo_key"].method_name)

    # Restore the graph with tag "bar". The SignatureDef map should have two
    # entries. One corresponding to "bar_key" and another corresponding to the
    # new value of "foo_key".
    with self.session(graph=ops.Graph()) as sess:
        bar_graph = loader.load(sess, ["bar"], export_dir)
        self.assertEqual(
            42,
            self._eval(ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0]))

        bar_signature = bar_graph.signature_def
        self.assertEqual(len(bar_signature), 2)
        self.assertEqual("bar", bar_signature["bar_key"].method_name)
        self.assertEqual("foo_new", bar_signature["foo_key"].method_name)
