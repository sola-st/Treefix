# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/inspect_checkpoint.py
if not FLAGS.file_name:
    print("Usage: inspect_checkpoint --file_name=checkpoint_file_name "
          "[--tensor_name=tensor_to_print] "
          "[--all_tensors] "
          "[--all_tensor_names] "
          "[--printoptions]")
    sys.exit(1)
else:
    print_tensors_in_checkpoint_file(
        FLAGS.file_name, FLAGS.tensor_name,
        FLAGS.all_tensors, FLAGS.all_tensor_names,
        count_exclude_pattern=FLAGS.count_exclude_pattern)
