# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
# The `input_context` passed in is to shard dataset for
# MultiWorkerMirroredStrategy. It doesn't apply to in-graph case where
# multiple InputContexts are needed.
if input_type == "input_fn":
    self.assertIsNone(
        input_context,
        msg=("`The input_context` arg is only used to shard dataset in "
             "`MultiWorkerMirroredStrategy` when the input type is dataset."))

    input_contexts = []
    for i in range(input_workers.num_workers):
        input_contexts.append(
            distribute_lib.InputContext(
                # Note: `input_workers.num_workers` is always 1 in between-graph
                # case.
                num_input_pipelines=input_workers.num_workers,
                input_pipeline_id=i,
                num_replicas_in_sync=len(devices)))

    iterator = input_lib_v1.InputFunctionIterator(dataset_or_input_fn,
                                                  input_workers,
                                                  input_contexts, strategy)
else:
    iterator = input_lib_v1.DatasetIterator(
        dataset_or_input_fn,
        input_workers,
        strategy,
        num_replicas_in_sync=num_replicas_in_sync,
        input_context=input_context)
exit(iterator)
