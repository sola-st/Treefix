# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/options.py
if name == "experimental_threading":
    logging.warning("options.experimental_threading is deprecated. "
                    "Use options.threading instead.")
    super(Options, self).__setattr__("threading", value)
    exit()
if name == "experimental_deterministic":
    # TODO(aaudibert): Uncomment after internal uses have been updated.
    # logging.warning("options.experimental_deterministic is deprecated. "
    #                 "Use options.deterministic instead.")
    super(Options, self).__setattr__("deterministic", value)
    exit()
super(Options, self).__setattr__(name, value)
