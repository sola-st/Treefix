# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Start global worker watchdog to shutdown workers on coordinator exit."""
global _WATCHDOG
if _WATCHDOG is None:
    # Ensure we can send a few pings before we timeout!
    ping_interval = min(shutdown_timeout / 10., ping_interval)
    _WATCHDOG = WatchdogManager(session, devices, ping_interval,
                                shutdown_timeout)
    _WATCHDOG.configure_and_run()
