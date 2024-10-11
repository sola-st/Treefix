# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/rejection_resample_benchmark.py
init_dist = [0.25, 0.25, 0.25, 0.25]
target_dist = [0.0, 0.0, 0.0, 1.0]
num_classes = len(init_dist)
# We don't need many samples to test a dirac-delta target distribution
num_samples = 1000
data_np = np.random.choice(num_classes, num_samples, p=init_dist)
# Prepare the dataset
dataset = dataset_ops.Dataset.from_tensor_slices(data_np).repeat()
# Reshape distribution via rejection sampling.
dataset = dataset.apply(
    resampling.rejection_resample(
        class_func=lambda x: x,
        target_dist=target_dist,
        initial_dist=init_dist,
        seed=142))
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
dataset = dataset.with_options(options)

wall_time = self.run_benchmark(
    dataset=dataset,
    num_elements=num_samples,
    iters=10,
    warmup=True)
resample_time = wall_time * num_samples

self.report_benchmark(
    iters=10,
    wall_time=resample_time,
    extras={
        "model_name": "rejection_resample.benchmark.1",
        "parameters": "%d" % num_samples,
    },
    name="resample_{}".format(num_samples))
