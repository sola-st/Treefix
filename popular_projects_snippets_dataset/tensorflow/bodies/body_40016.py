# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
# warm up
func()
start = time.time()
for _ in range(num_iters):
    func()
end = time.time()
exit(end - start)
