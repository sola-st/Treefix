# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "False"

if FLAGS.use_tf2:
    logging.info("Running in TF2 mode. Eager execution is enabled.")
    framework_ops.enable_eager_execution()
else:
    logging.info("Running in TF1 mode. Eager execution is disabled.")
    framework_ops.disable_eager_execution()

if FLAGS.use_int8:
    logging.info("Will try converting with INT8 precision.")
else:
    logging.info("Will not try converting with INT8 precision.")

if FLAGS.gpu_memory_limit_mb:
    set_up_gpu_memory_limit(FLAGS.gpu_memory_limit_mb)

tol = namedtuple("tol", "perf acc")
tolerances = {
    trt.TrtPrecisionMode.FP32:
        tol(perf=float(FLAGS.fp32_speedup_tolerance),
            acc=float(FLAGS.fp32_abs_tolerance)),
    trt.TrtPrecisionMode.FP16:
        tol(perf=float(FLAGS.fp16_speedup_tolerance),
            acc=float(FLAGS.fp16_abs_tolerance)),
    trt.TrtPrecisionMode.INT8:
        tol(perf=float(FLAGS.int8_speedup_tolerance),
            acc=float(FLAGS.int8_abs_tolerance)),
}

analyzer = result_analyzer.ResultAnalyzer(
    use_cpu_latency_baseline=FLAGS.latency_baseline == "CPU",
    use_cpu_numerics_baseline=FLAGS.numerics_baseline == "CPU",
    perf_checkers={
        precision: functools.partial(
            result_analyzer.check_column,
            name="speedup",
            fn=lambda x: x > tol.perf)
        for precision, tol in tolerances.items()
    },
    acc_checkers={
        precision: functools.partial(
            result_analyzer.check_column,
            name="abs_diff_mean",
            fn=lambda x: all(v < tol.acc for v in x.values()))
        for precision, tol in tolerances.items()
    })

runner = SampleRunner(
    saved_model_dir=FLAGS.saved_model_dir,
    saved_model_tags=FLAGS.saved_model_tags,
    saved_model_signature_key=FLAGS.saved_model_signature_key,
    batch_size=FLAGS.batch_size,
    output_dir=FLAGS.output_dir,
    output_format=FLAGS.output_format,
    use_tf2=FLAGS.use_tf2,
    use_int8=FLAGS.use_int8,
    analyzer=analyzer)

runner.run_all_tests()
