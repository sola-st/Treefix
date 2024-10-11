# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
# Tests that the supervisor finishes without an error when using
# a fixed number of epochs, reading from a single queue.
logdir = self._test_dir("managed_end_of_input_one_queue")
os.makedirs(logdir)
data_path = self._csv_data(logdir)
with ops.Graph().as_default():
    # Create an input pipeline that reads the file 3 times.
    filename_queue = input_lib.string_input_producer(
        [data_path], num_epochs=3)
    reader = io_ops.TextLineReader()
    _, csv = reader.read(filename_queue)
    rec = parsing_ops.decode_csv(csv, record_defaults=[[1], [1], [1]])
    sv = supervisor.Supervisor(logdir=logdir)
    with sv.managed_session("") as sess:
        while not sv.should_stop():
            sess.run(rec)
