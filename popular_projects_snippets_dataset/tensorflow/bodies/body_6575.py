# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if iteration_type == "for_loop" and not context.executing_eagerly():
    self.skipTest("unsupported test combination.")

if api_type == "wrap_into_iterator" and iteration_type == "for_loop":
    self.skipTest("unsupported test combination.")

if api_type == "wrap_into_iterator" and input_type == "input_fn":
    self.skipTest("unsupported test combination.")

devices = nest.flatten([ds for _, ds in worker_device_pairs])
input_workers = input_lib.InputWorkers(worker_device_pairs)

if api_type == "wrap_into_iterator":
    iterator = self._wrap_iterator(
        input_type,
        dataset_or_input_fn,
        input_workers,
        devices,
        num_replicas_in_sync,
        strategy,
        input_context=input_context)
else:
    # wrapping into a dataset:
    dataset = self._wrap_dataset(
        input_type,
        dataset_or_input_fn,
        input_workers,
        num_replicas_in_sync,
        strategy,
        input_context=input_context)

    if ops.executing_eagerly_outside_functions():
        iterator = iter(dataset)
    else:
        if isinstance(dataset, input_lib_v1.DistributedDatasetV1):
            iterator = dataset.make_initializable_iterator()
        else:
            self.skipTest("unsupported test combination")

if isinstance(iterator, composite_tensor.CompositeTensor):
    nest.assert_same_structure(
        iterator, iterator._type_spec, expand_composites=True)

if iteration_type == "get_next":
    evaluate = lambda x: sess.run(x) if sess else self.evaluate(x)
    if not ops.executing_eagerly_outside_functions():
        evaluate(control_flow_ops.group(iterator.initializer))

    def test_get_next(iterator):
        self._assert_iterator_values(iterator, expected_values, evaluate,
                                     devices)

        with self.assertRaises(errors.OutOfRangeError):
            self._assert_iterator_values(iterator, expected_values, evaluate,
                                         devices)

        # After re-initializing the iterator, should be able to iterate again.
        if not ops.executing_eagerly_outside_functions():
            evaluate(control_flow_ops.group(iterator.initializer))
        else:
            if api_type == "wrap_into_iterator":
                self.skipTest("unsupported test combination")
            else:
                iterator = iter(dataset)

        self._assert_iterator_values(iterator, expected_values, evaluate,
                                     devices)

    def test_get_next_as_optional(iterator):
        self._assert_iterator_values(
            iterator,
            expected_values,
            evaluate,
            devices,
            enable_get_next_as_optional=True)

        next_element = iterator.get_next_as_optional()
        self.assertFalse(self.evaluate(next_element.has_value()))
        with self.assertRaises(errors.InvalidArgumentError):
            self._assert_iterator_values(
                iterator, [0],
                evaluate,
                devices,
                enable_get_next_as_optional=True)

    test_get_next(iterator)

    # re-initializing the iterator
    if not tf2.enabled():
        # TODO(yuefengz): we should split this function.
        exit()
    else:
        if api_type == "wrap_into_iterator":
            exit()
        else:
            iterator = iter(dataset)

    test_get_next_as_optional(iterator)

if iteration_type == "for_loop" and context.executing_eagerly():
    self._assert_dataset_values_for_loop(dataset, expected_values,
                                         self.evaluate, devices)
