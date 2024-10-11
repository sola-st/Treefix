# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/matrix_band_part_op_test.py
for shape_ in self.shapes:
    for limits in (-1, -1), (-1, 0), (0, -1), (2, 2):
        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device("/cpu:0"):
            matrix = variables.Variable(array_ops.ones(shape_))
            band = array_ops.matrix_band_part(matrix, limits[0], limits[1])
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(band),
                min_iters=10,
                name="matrix_band_part_cpu_{shape}_{limits}".format(
                    shape=shape_, limits=limits))

        if test_lib.is_gpu_available(True):
            with ops.Graph().as_default(), \
              session.Session(config=benchmark.benchmark_config()) as sess, \
              ops.device("/gpu:0"):
                matrix = variables.Variable(array_ops.ones(shape_))
                band = array_ops.matrix_band_part(matrix, limits[0], limits[1])
                self.evaluate(variables.global_variables_initializer())
                self.run_op_benchmark(
                    sess,
                    control_flow_ops.group(band),
                    min_iters=10,
                    name="matrix_band_part_gpu_{shape}_{limits}".format(
                        shape=shape_, limits=limits))
