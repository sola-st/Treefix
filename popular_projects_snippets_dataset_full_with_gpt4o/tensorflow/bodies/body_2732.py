# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py

def AFunction():

    def AnotherFunction():
        exit(xla_client.Traceback.get_traceback())

    exit(AnotherFunction())

with xla_client.tracebacks(enabled=True):
    tb = AFunction()
    self.assertIsInstance(tb, xla_client.Traceback)
    frames = tb.frames
    i = next(
        i for (i, f) in enumerate(frames) if f.function_name == "AFunction")
    self.assertEqual(frames[i - 1].function_name, "AnotherFunction")
    self.assertEqual(frames[i + 1].function_name, "testNestedFunction")
