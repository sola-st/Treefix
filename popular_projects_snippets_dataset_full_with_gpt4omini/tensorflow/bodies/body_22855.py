# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py

output_saved_model_dir = self.mkdtemp()
output_graph_def = self._ConvertGraphV1(
    output_saved_model_dir=output_saved_model_dir, maximum_cached_engines=1)

# Test the output GraphDef.
with ops.Graph().as_default():
    importer.import_graph_def(output_graph_def, name="")
    with self.session(config=self._GetConfigProto()) as sess:
        # Run with batch size 1, the default engine embedded in the graphdef
        # will be used.
        self._TestRun(sess, 1)
        # Run with batch size 2, which exceed the max_batch_size, it should try
        # to fall back to TF function.
        self._TestRun(sess, 2)

    # Test the output SavedModel
with ops.Graph().as_default():
    with self.session(config=self._GetConfigProto()) as sess:
        loader.load(sess, [tag_constants.SERVING], output_saved_model_dir)
        # Run with batch size 1, the default engine embedded in the graphdef
        # will be used.
        self._TestRun(sess, 1)
        # Run with batch size 2, which exceed the max_batch_size, it should try
        # to fall back to TF function.
        self._TestRun(sess, 2)
