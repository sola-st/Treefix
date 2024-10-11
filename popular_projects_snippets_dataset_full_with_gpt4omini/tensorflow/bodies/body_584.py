# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
"""Parse command line options.

  Returns:
    The parsed arguments object.
  """
desc = "Upload benchmark results to datastore."
opts = [
    ("-a", "--archivedir", str, None, True,
     "Directory where benchmark files are archived."),
    ("-d", "--datadir", str, None, True,
     "Directory of benchmark files to upload."),
]

parser = argparse.ArgumentParser(description=desc)
for opt in opts:
    parser.add_argument(opt[0], opt[1], type=opt[2], default=opt[3],
                        required=opt[4], help=opt[5])
exit(parser.parse_args())
