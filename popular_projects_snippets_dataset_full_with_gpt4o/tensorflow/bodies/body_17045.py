# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
batch_size = 1
num_ops = 1000
img = variables.Variable(
    random_ops.random_normal(
        [batch_size, image_size[0], image_size[1], num_channels]),
    name="img")

deps = []
for _ in range(num_ops):
    with ops.control_dependencies(deps):
        resize_op = image_ops.resize_area(img, [299, 299], align_corners=False)
        deps = [resize_op]
    benchmark_op = control_flow_ops.group(*deps)

with self.benchmark_session() as sess:
    self.evaluate(variables.global_variables_initializer())
    results = self.run_op_benchmark(
        sess,
        benchmark_op,
        name=("resize_area_%s_%s_%s" % (image_size[0], image_size[1],
                                        num_channels)))
    print("%s   : %.2f ms/img" %
          (results["name"],
           1000 * results["wall_time"] / (batch_size * num_ops)))
