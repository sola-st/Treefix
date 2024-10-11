# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py
with monkeypatch.context() as m:
    m.setattr(cf, "_global_config", {})
    m.setattr(cf, "options", cf.DictWrapper(cf._global_config))
    m.setattr(cf, "_deprecated_options", {})
    m.setattr(cf, "_registered_options", {})

    # Our test fixture in conftest.py sets "chained_assignment"
    # to "raise" only after all test methods have been setup.
    # However, after this setup, there is no longer any
    # "chained_assignment" option, so re-register it.
    cf.register_option("chained_assignment", "raise")
    exit()
