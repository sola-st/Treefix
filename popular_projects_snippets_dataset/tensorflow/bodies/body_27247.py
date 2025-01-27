# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
# Test that the data service client performs retries instead of failing when
# the dataset is created before the master and worker are started.
try:
    import portpicker  # pylint: disable=g-import-not-at-top
    dispatcher_port = portpicker.pick_unused_port()
except:
    raise self.skipTest("Flakes in portpicker library do not represent "
                        "TensorFlow errors.")
cluster = data_service_test_base.TestCluster(
    num_workers=1, dispatcher_port=dispatcher_port, start=False)

def start_servers():
    time.sleep(0.5)
    cluster.start_dispatcher()
    cluster.start_workers()

start_servers_thread = threading.Thread(target=start_servers, daemon=True)
start_servers_thread.start()

num_elements = 10
ds = self.make_distributed_range_dataset(num_elements, cluster)
results = [elem.numpy() for elem in ds]
self.assertEqual(list(range(num_elements)), results)
start_servers_thread.join()
