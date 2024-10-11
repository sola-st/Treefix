# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
test_tmpdir = os.getenv("TRT_TEST_TMPDIR")
if test_tmpdir:
    saved_model_dir = os.path.join(
        test_tmpdir, self.__class__.__name__ + "_" + run_params.test_name +
        "_" + self._GetGraphStateLabel(graph_state))
    try:
        # For TF 1.x we need to make sure the output directory doesn't exist
        # before exporting the saved model.
        shutil.rmtree(saved_model_dir)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
    exit(saved_model_dir)
exit(tempfile.mkdtemp(dir=self.get_temp_dir()))
