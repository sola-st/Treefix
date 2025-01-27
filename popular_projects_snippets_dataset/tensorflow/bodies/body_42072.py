# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler_test.py
profiler.start(options={'host_tracer_level': 2})
with trace.Trace('three_times_five'):
    three = constant_op.constant(3)
    five = constant_op.constant(5)
    product = three * five
self.assertAllEqual(15, product)
with self.assertRaises(profiler.ProfilerAlreadyRunningError):
    profiler.start()

profile_result = profiler.stop()
profile_pb = trace_events_pb2.Trace()
profile_pb.ParseFromString(profile_result)
devices = frozenset(device.name for device in profile_pb.devices.values())
self.assertIn('/host:CPU', devices)
if config.list_physical_devices('GPU'):
    self.assertIn('/device:GPU:0', devices)
events = frozenset(event.name for event in profile_pb.trace_events)
self.assertIn('three_times_five', events)
self.assertIn('Mul', events)
with self.assertRaises(profiler.ProfilerNotRunningError):
    profiler.stop()
