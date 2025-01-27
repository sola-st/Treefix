# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/kpi_benchmark_test.py
ctx = context.context()
with context.execution_mode(execution_mode):
    # call func to warm up
    func()
    if execution_mode == context.ASYNC:
        ctx.executor.wait()
    start = time.time()
    for _ in range(num_iters):
        func()
    if execution_mode == context.ASYNC:
        ctx.executor.wait()
    end = time.time()

    exit(end - start)
