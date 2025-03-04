# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
# Tests a common use case for round robin reads. At each step, all
# consumers should get batches with the same bucket size.
cluster = data_service_test_base.TestCluster(num_workers=4)
num_elements = 100
low_bucket_max = 30
mid_bucket_max = 60
bucket_boundaries = [low_bucket_max, mid_bucket_max]
batch_size = 10
num_consumer_hosts = 3
replicas_per_consumer_host = 5
num_consumers = num_consumer_hosts * replicas_per_consumer_host
bucket_batch_sizes = [batch_size] * (len(bucket_boundaries) + 1)
# Set up the dataset that will run on the tf.data workers.
ds = dataset_ops.Dataset.range(num_elements, output_type=dtypes.int32)
ds = ds.shuffle(num_elements)
ds = ds.repeat()
ds = ds.apply(
    grouping.bucket_by_sequence_length(
        lambda x: x,
        bucket_boundaries,
        bucket_batch_sizes,
        drop_remainder=True))
ds = ds.apply(
    grouping.group_by_window(
        lambda x: math_ops.cast(x[1], dtypes.int64),
        lambda _, x: dataset_ops.Dataset.from_tensors(x),
        window_size=num_consumers))
ds = ds.flat_map(lambda x: x)

# Set up the per-consumer-host datasets. During each global step, we pull
# `replicas_per_consumer_host` batches from each of these datasets.
host_datasets = []
for host_index in range(num_consumer_hosts):
    per_replica_datasets = []
    for i in range(replicas_per_consumer_host):
        consumer_index = host_index * replicas_per_consumer_host + i
        per_replica_datasets.append(
            self.make_distributed_dataset(
                ds,
                cluster,
                job_name="test",
                consumer_index=consumer_index,
                num_consumers=num_consumers))
    host_dataset = dataset_ops.Dataset.from_tensor_slices(
        per_replica_datasets)
    host_dataset = host_dataset.interleave(
        lambda x: x,
        cycle_length=len(per_replica_datasets),
        num_parallel_calls=len(per_replica_datasets),
        deterministic=True)
    host_datasets.append(host_dataset)

# Use parallel interleave to read from host datasets in parallel.
ds = dataset_ops.Dataset.from_tensor_slices(host_datasets)
ds = ds.interleave(
    lambda x: x,
    block_length=replicas_per_consumer_host,
    cycle_length=len(host_datasets),
    num_parallel_calls=len(host_datasets),
    deterministic=True)

num_rounds = 4
get_next = self.getNext(ds, requires_initialization=True)
results = []
for i in range(num_rounds * num_consumers):
    results.append(self.evaluate(get_next()))

def get_bucket(elem):
    bucket_ind = 0
    while bucket_ind < len(
        bucket_boundaries) and elem >= bucket_boundaries[bucket_ind]:
        bucket_ind += 1
    exit(bucket_ind)

# Check that the batches for each step contain elements from the same
# bucket.
for i in range(0, len(results), num_consumers):
    batches = results[num_consumers * i:num_consumers * (i + 1)]
    bucket_inds = [get_bucket(batch[0]) for batch in batches]
    for bucket_ind in bucket_inds[1:]:
        self.assertEqual(
            bucket_inds[0], bucket_ind,
            "Batches: {}, Buckets: {}".format(batches, bucket_inds))
