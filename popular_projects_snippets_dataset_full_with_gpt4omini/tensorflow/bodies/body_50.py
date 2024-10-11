# Extracted from ./data/repos/tensorflow/tensorflow/tools/gcs_test/python/gcs_smoke.py
del argv  # Unused.

# Sanity check on the GCS bucket URL.
if not FLAGS.gcs_bucket_url or not FLAGS.gcs_bucket_url.startswith("gs://"):
    print("ERROR: Invalid GCS bucket URL: \"%s\"" % FLAGS.gcs_bucket_url)
    sys.exit(1)

# Generate random tfrecord path name.
input_path = FLAGS.gcs_bucket_url + "/"
input_path += "".join(random.choice("0123456789ABCDEF") for i in range(8))
input_path += ".tfrecord"
print("Using input path: %s" % input_path)

# Verify that writing to the records file in GCS works.
print("\n=== Testing writing and reading of GCS record file... ===")
example_data = create_examples(FLAGS.num_examples, 5)
with tf.io.TFRecordWriter(input_path) as hf:
    for e in example_data:
        hf.write(e.SerializeToString())

    print("Data written to: %s" % input_path)

# Verify that reading from the tfrecord file works and that
# tf_record_iterator works.
record_iter = tf.compat.v1.python_io.tf_record_iterator(input_path)
read_count = 0
for _ in record_iter:
    read_count += 1
print("Read %d records using tf_record_iterator" % read_count)

if read_count != FLAGS.num_examples:
    print("FAIL: The number of records read from tf_record_iterator (%d) "
          "differs from the expected number (%d)" % (read_count,
                                                     FLAGS.num_examples))
    sys.exit(1)

# Verify that running the read op in a session works.
print("\n=== Testing TFRecordReader.read op in a session... ===")
with tf.Graph().as_default():
    filename_queue = tf.compat.v1.train.string_input_producer([input_path],
                                                              num_epochs=1)
    reader = tf.compat.v1.TFRecordReader()
    _, serialized_example = reader.read(filename_queue)

    with tf.compat.v1.Session() as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        sess.run(tf.compat.v1.local_variables_initializer())
        tf.compat.v1.train.start_queue_runners()
        index = 0
        for _ in range(FLAGS.num_examples):
            print("Read record: %d" % index)
            sess.run(serialized_example)
            index += 1

        # Reading one more record should trigger an exception.
        try:
            sess.run(serialized_example)
            print("FAIL: Failed to catch the expected OutOfRangeError while "
                  "reading one more record than is available")
            sys.exit(1)
        except tf.errors.OutOfRangeError:
            print("Successfully caught the expected OutOfRangeError while "
                  "reading one more record than is available")

create_dir_test()
create_object_test()
