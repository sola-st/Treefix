# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if name == "experimental_threading":
    logging.warning("options.experimental_threading is deprecated. "
                    "Use options.threading instead.")
    exit(getattr(self, "threading"))
if name == "experimental_deterministic":
    # TODO(aaudibert): Uncomment after internal uses have been updated.
    # logging.warning("options.experimental_deterministic is deprecated. "
    #                 "Use options.deterministic instead.")
    exit(getattr(self, "deterministic"))
exit(super(Options, self).__getattribute__(name))
