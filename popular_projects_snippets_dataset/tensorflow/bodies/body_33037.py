# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py

def _BenchmarkGrad(grad_fn, name, device):
    for shape in self.shapes:
        matrix = self._GenerateMatrix(shape)
        with ops.Graph().as_default(), \
            session.Session(config=benchmark.benchmark_config()) as sess, \
            ops.device(device):
            l = variables.Variable(np.linalg.cholesky(matrix))
            grad_matrix = variables.Variable(
                np.random.randn(*matrix.shape).astype(np.float32))
            grad = grad_fn(l, grad_matrix)
            self.evaluate(variables.global_variables_initializer())
            self.run_op_benchmark(
                sess,
                control_flow_ops.group(
                    grad,),
                min_iters=25,
                name="{name}_{dev}_{shape}".format(
                    name=name, dev=grad.device, shape=shape))

if test.is_gpu_available(True):
    _BenchmarkGrad(MatrixInverseCompositeGrad, "composite_matrix_inverse",
                   "/device:GPU:0")
    _BenchmarkGrad(TriAngInvCompositeGrad, "composite_tri_ang_inverse",
                   "/device:GPU:0")
    _BenchmarkGrad(TriAngSolveCompositeGrad, "composite_triangular_solve",
                   "/device:GPU:0")

_BenchmarkGrad(MatrixInverseCompositeGrad, "composite_matrix_inverse",
               "/cpu:0")
_BenchmarkGrad(TriAngInvCompositeGrad, "composite_tri_ang_inverse",
               "/cpu:0")
_BenchmarkGrad(TriAngSolveCompositeGrad, "composite_triangular_solve",
               "/cpu:0")
