# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/run_and_gather_logs.py
name = FLAGS.name
test_name = FLAGS.test_name
test_args = " ".join(FLAGS.test_args)
benchmark_type = FLAGS.benchmark_type
test_results, _ = run_and_gather_logs_lib.run_and_gather_logs(
    name,
    test_name=test_name,
    test_args=test_args,
    benchmark_type=benchmark_type,
    skip_processing_logs=FLAGS.skip_export)
if FLAGS.skip_export:
    exit()

# Additional bits we receive from bazel
test_results.build_configuration.CopyFrom(gather_build_configuration())
# Add os.environ data to test_results.
test_results.run_configuration.env_vars.update(os.environ)

if not FLAGS.test_log_output_dir:
    print(text_format.MessageToString(test_results))
    exit()

if FLAGS.test_log_output_filename:
    file_name = FLAGS.test_log_output_filename
else:
    file_name = (
        name.strip("/").translate(str.maketrans("/:", "__")) +
        time.strftime("%Y%m%d%H%M%S", time.gmtime()))
if FLAGS.test_log_output_use_tmpdir:
    tmpdir = test.get_temp_dir()
    output_path = os.path.join(tmpdir, FLAGS.test_log_output_dir, file_name)
else:
    output_path = os.path.join(
        os.path.abspath(FLAGS.test_log_output_dir), file_name)
json_test_results = json_format.MessageToJson(test_results)
gfile.GFile(output_path + ".json", "w").write(json_test_results)
tf_logging.info("Test results written to: %s" % output_path)
