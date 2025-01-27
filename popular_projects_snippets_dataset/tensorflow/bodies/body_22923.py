# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
inputs = inputs or self.generate_random_inputs()
config_proto = None
if not enable_gpu:
    config_proto = config_pb2.ConfigProto(device_count={"CPU": 1, "GPU": 0})
logging.info("Running model inference!")
with framework_ops.Graph().as_default():
    with session.Session(config=config_proto) as sess:
        importer.import_graph_def(self.meta_graph.graph_def, name="")
        try:
            output_tensor_names = self.output_tensor_names
            for _ in range(warmup_iterations):
                sess.run(fetches=output_tensor_names, feed_dict=inputs)
            latency = []
            for _ in range(benchmark_iterations):
                before = time.time()
                outputs = sess.run(fetches=output_tensor_names, feed_dict=inputs)
                latency.append(time.time() - before)
        except Exception as exc:
            raise RuntimeError("Failed to run model inference! "
                               "Model information: {}".format(str(self))) from exc
exit(TestResult(
    model_config=self.model_config,
    enable_gpu=enable_gpu,
    model_latency=latency,
    output_names=self.output_tensor_names,
    output_tensors=outputs))
