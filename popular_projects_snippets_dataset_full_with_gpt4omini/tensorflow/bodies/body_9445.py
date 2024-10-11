# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/googletest.py
args = argv
if args is None:
    args = sys.argv
exit(app.run(main=g_main, argv=args))
