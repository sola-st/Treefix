# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""A transformation that moves dataset processing to the tf.data service.

  When you iterate over a dataset containing the `distribute` transformation,
  the tf.data service creates a "job" which produces data for the dataset
  iteration.

  The tf.data service uses a cluster of workers to prepare data for training
  your model.
  The `processing_mode` argument to `tf.data.experimental.service.distribute`
  describes how to leverage multiple workers to process the input dataset.
  Currently, there are two processing modes to choose from: "distributed_epoch"
  and "parallel_epochs".

  "distributed_epoch" means that the dataset will be split across all tf.data
  service workers.
  The dispatcher produces "splits" for the dataset and sends them to workers for
  further processing. For example, if a dataset begins with a list of filenames,
  the dispatcher will iterate through the filenames and send the filenames to
  tf.data workers, which will perform the rest of the dataset transformations on
  those files. "distributed_epoch" is useful when your model needs to see each
  element of the dataset exactly once, or if it needs to see the data in a
  generally-sequential order. "distributed_epoch" only works for datasets with
  splittable sources, such as `Dataset.from_tensor_slices`,
  `Dataset.list_files`, or `Dataset.range`.

  "parallel_epochs" means that the entire input dataset will be processed
  independently by each of the tf.data service workers.
  For this reason, it is important to shuffle data (e.g. filenames)
  non-deterministically, so that each worker will process the elements of the
  dataset in a different order. "parallel_epochs" can be used to distribute
  datasets that aren't splittable.

  With two workers, "parallel_epochs" will produce every element of the dataset
  twice:

  >>> dispatcher = tf.data.experimental.service.DispatchServer()
  >>> dispatcher_address = dispatcher.target.split("://")[1]
  >>> # Start two workers
  >>> workers = [
  ...     tf.data.experimental.service.WorkerServer(
  ...         tf.data.experimental.service.WorkerConfig(
  ...             dispatcher_address=dispatcher_address)) for _ in range(2)
  ... ]
  >>> dataset = tf.data.Dataset.range(10)
  >>> dataset = dataset.apply(tf.data.experimental.service.distribute(
  ...     processing_mode="parallel_epochs", service=dispatcher.target))
  >>> print(sorted(list(dataset.as_numpy_iterator())))
  [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]

  "distributed_epoch", on the other hand, will still produce each element once:

  >>> dispatcher = tf.data.experimental.service.DispatchServer()
  >>> dispatcher_address = dispatcher.target.split("://")[1]
  >>> workers = [
  ...     tf.data.experimental.service.WorkerServer(
  ...         tf.data.experimental.service.WorkerConfig(
  ...             dispatcher_address=dispatcher_address)) for _ in range(2)
  ... ]
  >>> dataset = tf.data.Dataset.range(10)
  >>> dataset = dataset.apply(tf.data.experimental.service.distribute(
  ...     processing_mode="distributed_epoch", service=dispatcher.target))
  >>> print(sorted(list(dataset.as_numpy_iterator())))
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  When using `apply(tf.data.experimental.service.distribute(...))`, the dataset
  before the `apply` transformation executes within the tf.data service, while
  the operations after `apply` happen within the local process.

  >>> dispatcher = tf.data.experimental.service.DispatchServer()
  >>> dispatcher_address = dispatcher.target.split("://")[1]
  >>> workers = [
  ...     tf.data.experimental.service.WorkerServer(
  ...         tf.data.experimental.service.WorkerConfig(
  ...             dispatcher_address=dispatcher_address)) for _ in range(2)
  ... ]
  >>> dataset = tf.data.Dataset.range(5)
  >>> dataset = dataset.map(lambda x: x*x)
  >>> dataset = dataset.apply(
  ...    tf.data.experimental.service.distribute("parallel_epochs",
  ...                                            dispatcher.target))
  >>> dataset = dataset.map(lambda x: x+1)
  >>> print(sorted(list(dataset.as_numpy_iterator())))
  [1, 1, 2, 2, 5, 5, 10, 10, 17, 17]

  In the above example, the dataset operations (before applying the `distribute`
  function on the elements) will be executed on the tf.data workers,
  and the elements are provided over RPC. The remaining transformations
  (after the call to `distribute`) will be executed locally. The dispatcher
  and the workers will bind to usused free ports (which are chosen at random),
  in order to communicate with each other. However, to bind them to specific
  ports, the `port` parameter can be passed.

  The `job_name` argument allows jobs to be shared across multiple
  datasets. Instead of each dataset creating its own job, all
  datasets with the same `job_name` will consume from the same job. A new job
  will be created for each iteration of the dataset (with each repetition of
  `Dataset.repeat` counting as a new iteration). Suppose the `DispatchServer`
  is serving on `localhost:5000` and two training workers (in either a single
  client or multi-client setup) iterate over the below dataset, and there is a
  single tf.data worker:

  ```
  range5_dataset = tf.data.Dataset.range(5)
  dataset = range5_dataset.apply(tf.data.experimental.service.distribute(
      "parallel_epochs", "localhost:5000", job_name="my_job_name"))
  for iteration in range(3):
    print(list(dataset))
  ```

  The elements of each job will be split between the two processes, with
  elements being consumed by the processes on a first-come first-served basis.
  One possible result is that process 1 prints

  ```
  [0, 2, 4]
  [0, 1, 3]
  [1]
  ```

  and process 2 prints

  ```
  [1, 3]
  [2, 4]
  [0, 2, 3, 4]
  ```

  Job names must not be re-used across different training jobs within the
  lifetime of the tf.data service. In general, the tf.data service is expected
  to live for the duration of a single training job.
  To use the tf.data service with multiple training jobs, make sure to use
  different job names to avoid conflicts. For example, suppose a training job
  calls `distribute` with `job_name="job"` and reads until end of input. If
  another independent job connects to the same tf.data service and tries to read
  from `job_name="job"`, it will immediately receive end of input, without
  getting any data.

  **Coordinated data read**

  By default, when multiple consumers read from the same job, they receive data
  on a first-come first-served basis. In some use cases, it is advantageous to
  coordinate the consumers. At each step, consumers read data from the same
  worker.

  For example, the tf.data service can be used to coordinate example sizes
  across a cluster during synchronous training, so that during each step all
  replicas train on similar-sized elements. To achieve this, define a dataset
  which generates rounds of `num_consumers` consecutive similar-sized batches,
  then enable coordinated reads by setting `consumer_index` and `num_consumers`.

  NOTE: To keep consumers in sync, round robin data consumption requires that
  the dataset have infinite cardinality. You can get this by adding `.repeat()`
  at the end of the dataset definition.

  **Keras and Distribution Strategies**

  The dataset produced by the `distribute` transformation can be passed to
  Keras' `Model.fit` or Distribution Strategy's
  `tf.distribute.Strategy.experimental_distribute_dataset` like any other
  `tf.data.Dataset`. We recommend setting a `job_name` on the call to
  `distribute` so that if there are multiple workers, they read data from the
  same job. Note that the autosharding normally performed by
  `experimental_distribute_dataset` will be disabled when setting a `job_name`,
  since sharing the job already results in splitting data across the workers.
  When using a shared job, data will be dynamically balanced across workers, so
  that they reach end of input about the same time. This results in better
  worker utilization than with autosharding, where each worker processes an
  independent set of files, and some workers may run out of data earlier than
  others.

  Args:
    processing_mode: A `tf.data.experimental.service.ShardingPolicy` specifying
      how to shard the dataset among tf.data workers. See
      `tf.data.experimental.service.ShardingPolicy` for details. For backwards
      compatibility, `processing_mode` may also be set to the strings
      `"parallel_epochs"` or `"distributed_epoch"`, which are respectively
      equivalent to `ShardingPolicy.OFF` and `ShardingPolicy.DYNAMIC`.
    service: A string or a tuple indicating how to connect to the tf.data
      service. If it's a string, it should be in the format
      `[<protocol>://]<address>`, where `<address>` identifies the dispatcher
        address and `<protocol>` can optionally be used to override the default
        protocol to use. If it's a tuple, it should be (protocol, address).
    job_name: (Optional.) The name of the job. If provided, it must be a
      non-empty string. This argument makes it possible for multiple datasets to
      share the same job. The default behavior is that the dataset creates
      anonymous, exclusively owned jobs.
    consumer_index: (Optional.) The index of the consumer in the range from `0`
      to `num_consumers`. Must be specified alongside `num_consumers`. When
      specified, consumers will read from the job in a strict round-robin order,
      instead of the default first-come-first-served order.
    num_consumers: (Optional.) The number of consumers which will consume from
      the job. Must be specified alongside `consumer_index`. When specified,
      consumers will read from the job in a strict round-robin order, instead of
      the default first-come-first-served order. When `num_consumers` is
      specified, the dataset must have infinite cardinality to prevent a
      producer from running out of data early and causing consumers to go out of
      sync.
    max_outstanding_requests: (Optional.) A limit on how many elements may be
      requested at the same time. You can use this option to control the amount
      of memory used, since `distribute` won't use more than `element_size` *
      `max_outstanding_requests` of memory.
    data_transfer_protocol: (Optional.) The protocol to use for transferring
      data with the tf.data service. By default, data is transferred using gRPC.
    compression: How to compress the dataset's elements before transferring them
      over the network. "AUTO" leaves the decision of how to compress up to the
      tf.data service runtime. `None` indicates not to compress.
    cross_trainer_cache: (Optional.) If a `CrossTrainerCache` object is
      provided, dataset iteration will be shared across concurrently running
      trainers. See
      https://www.tensorflow.org/api_docs/python/tf/data/experimental/service#sharing_tfdata_service_with_concurrent_trainers
      for details.
    target_workers: (Optional.) Which workers to read from. If `"AUTO"`, tf.data
      runtime decides which workers to read from. If `"ANY"`, reads from any
      tf.data service workers. If `"LOCAL"`, only reads from local in-processs
      tf.data service workers. `"AUTO"` works well for most cases, while users
      can specify other targets. For example, `"LOCAL"` helps avoid RPCs and
      data copy if every TF worker colocates with a tf.data service worker.
      Consumers of a shared job must use the same `target_workers`. Defaults to
      `"AUTO"`.

  Returns:
    Dataset: A `Dataset` of the elements produced by the data service.
  """
_validate_job_name(job_name)
exit(_distribute(
    processing_mode=processing_mode,
    service=service,
    job_name=job_name,
    consumer_index=consumer_index,
    num_consumers=num_consumers,
    max_outstanding_requests=max_outstanding_requests,
    data_transfer_protocol=data_transfer_protocol,
    compression=compression,
    cross_trainer_cache=cross_trainer_cache,
    target_workers=target_workers))
