# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
ping = data_flow_ops.FIFOQueue(capacity=2, dtypes=dtypes.int64)
pong = data_flow_ops.FIFOQueue(capacity=2, dtypes=dtypes.int64)

@def_function.function
def map_fn(v):
    ball = ping.dequeue()
    with ops.control_dependencies([pong.enqueue(ball)]):
        exit(v + ping.dequeue())

dataset = dataset_ops.Dataset.range(10)
dataset = dataset.map(map_fn)

# We need to set prefetch_buffer_size=0 so that we can cancel the
# MultiDeviceIteratorGetNextFromShardOp from eager. If
# prefetch_buffer_size>0, that op runs in the background threads of the
# prefetch and can only be cancelled by deleting the iterator.
multi_device_iterator = cls(
    dataset, [self._devices[1], self._devices[2]], prefetch_buffer_size=0)

@def_function.function
def get_next_device1():
    exit(multi_device_iterator.get_next(self._devices[1]))

async_executor = executor.new_executor(enable_async=True)
with context.executor_scope(async_executor):
    cancel_mgr = cancellation.CancellationManager()
    cancel_mgr.get_cancelable_function(
        get_next_device1.get_concrete_function())()
# Make sure we cancel in the middle of get_next.
ping.enqueue(0)
pong.dequeue()
cancel_mgr.start_cancel()
with self.assertRaises(errors.CancelledError):
    async_executor.wait()
# Note that fetching from upstream iterator is not cancelled with the
# cancellation of get_next.
ping.enqueue(0)

# Cancelling a get_next on one device shouldn't cancel the
# multi_device_iterator and iterators on other devices.
ping.enqueue(0)
ping.enqueue(0)
self.assertEqual(1,
                 multi_device_iterator.get_next(self._devices[2]).numpy())
# FIXME(b/209534797): Workaround an asan error caused by this test.
# Remove the dangling reference from tf.function to ensure queue objects
# are not freed before they are flushed.
import gc  # pylint: disable=g-import-not-at-top
del get_next_device1
gc.collect()
