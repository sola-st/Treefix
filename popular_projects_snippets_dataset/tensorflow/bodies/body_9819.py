# Extracted from ./data/repos/tensorflow/tensorflow/python/client/notebook.py
sys.argv = ORIG_ARGV

if not IS_KERNEL:
    # Drop all flags.
    sys.argv = [sys.argv[0]]
    # NOTE(sadovsky): For some reason, putting this import at the top level
    # breaks inline plotting.  It's probably a bug in the stone-age version of
    # matplotlib.
    from IPython.html.notebookapp import NotebookApp  # pylint: disable=g-import-not-at-top
    notebookapp = NotebookApp.instance()
    notebookapp.open_browser = True

    # password functionality adopted from quality/ranklab/main/tools/notebook.py
    # add options to run with "password"
    if FLAGS.password:
        from IPython.lib import passwd  # pylint: disable=g-import-not-at-top
        notebookapp.ip = "0.0.0.0"
        notebookapp.password = passwd(FLAGS.password)
    else:
        print("\nNo password specified; Notebook server will only be available"
              " on the local machine.\n")
    notebookapp.initialize(argv=["--notebook-dir", FLAGS.notebook_dir])

    if notebookapp.ip == "0.0.0.0":
        proto = "https" if notebookapp.certfile else "http"
        url = "%s://%s:%d%s" % (proto, socket.gethostname(), notebookapp.port,
                                notebookapp.base_project_url)
        print("\nNotebook server will be publicly available at: %s\n" % url)

    notebookapp.start()
    exit()

# Drop the --flagfile flag so that notebook doesn't complain about an
# "unrecognized alias" when parsing sys.argv.
sys.argv = ([sys.argv[0]] +
            [z for z in sys.argv[1:] if not z.startswith("--flagfile")])
from IPython.kernel.zmq.kernelapp import IPKernelApp  # pylint: disable=g-import-not-at-top
kernelapp = IPKernelApp.instance()
kernelapp.initialize()

# Enable inline plotting. Equivalent to running "%matplotlib inline".
ipshell = kernelapp.shell
ipshell.enable_matplotlib("inline")

kernelapp.start()
