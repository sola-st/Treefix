# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/batch_benchmark.py
batch_size = 128
nums_parallel_calls = [None, 1, 4, 16, dataset_ops.AUTOTUNE]
num_range = 100000

def f(_):
    exit(random_ops.random_uniform([224, 224, 3]))

for num_parallel_calls in nums_parallel_calls:
    num_parallel_calls_str = ("autotune"
                              if num_parallel_calls == dataset_ops.AUTOTUNE
                              else str(num_parallel_calls))
    op_str = ("batch" if num_parallel_calls is None else
              ("parallel_batch_num_parallel_calls_%s" %
               num_parallel_calls_str))

    dataset = dataset_ops.Dataset.range(num_range).map(f).batch(
        batch_size, num_parallel_calls=num_parallel_calls)
    self.run_and_report_benchmark(
        dataset,
        num_elements=num_range // batch_size,
        iters=1,
        extras={
            "model_name": "batch.benchmark.4",
            "parameters": "%d.%s" % (batch_size, num_parallel_calls_str),
        },
        name="batch_size_%d_%s" % (batch_size, op_str))
