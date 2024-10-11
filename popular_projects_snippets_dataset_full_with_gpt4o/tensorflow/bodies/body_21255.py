# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
# Tests that the supervisor correctly raises a main loop
# error even when using multiple queues for input.
logdir = self._test_dir("managed_main_error_two_queues")
os.makedirs(logdir)
data_path = self._csv_data(logdir)
with self.assertRaisesRegex(RuntimeError, "fail at step 3"):
    with ops.Graph().as_default():
        # Create an input pipeline that reads the file 3 times.
        filename_queue = input_lib.string_input_producer(
            [data_path], num_epochs=3)
        reader = io_ops.TextLineReader()
        _, csv = reader.read(filename_queue)
        rec = parsing_ops.decode_csv(csv, record_defaults=[[1], [1], [1]])
        shuff_rec = input_lib.shuffle_batch(rec, 1, 6, 4)
        sv = supervisor.Supervisor(logdir=logdir)
        with sv.managed_session("") as sess:
            for step in range(9):
                if sv.should_stop():
                    break
                elif step == 3:
                    raise RuntimeError("fail at step 3")
                else:
                    sess.run(shuff_rec)
