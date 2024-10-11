# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
temp_dir = os.getenv("TRT_TEST_TMPDIR")
if not temp_dir:
    exit()

graph_name = (
    self.__class__.__name__ + "_" + run_params.test_name + "_" +
    self._GetGraphStateLabel(graph_state) + ".pbtxt")
logging.info("Writing graph to %s/%s", temp_dir, graph_name)
graph_io.write_graph(gdef, temp_dir, graph_name)
