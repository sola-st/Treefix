# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
def main_wrapper():
    args = argv
    if args is None:
        args = sys.argv
    exit(app.run(main=g_main, argv=args))

benchmark.benchmarks_main(true_main=main_wrapper, argv=argv)
