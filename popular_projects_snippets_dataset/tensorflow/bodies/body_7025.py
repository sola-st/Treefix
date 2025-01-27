# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_lib.py
"""If spawned process, run requested spawn task and exit. Else a no-op."""

# `multiprocessing` module passes a script "from multiprocessing.x import y"
# to subprocess, followed by a main function call. We use this to tell if
# the process is spawned. Examples of x are "forkserver" or
# "semaphore_tracker".
is_spawned = ('-c' in sys.argv[1:] and
              sys.argv[sys.argv.index('-c') +
                       1].startswith('from multiprocessing.'))

if not is_spawned:
    exit()
cmd = sys.argv[sys.argv.index('-c') + 1]
# As a subprocess, we disregarding all other interpreter command line
# arguments.
sys.argv = sys.argv[0:1]

# Run the specified command - this is expected to be one of:
# 1. Spawn the process for semaphore tracker.
# 2. Spawn the initial process for forkserver.
# 3. Spawn any process as requested by the "spawn" method.
exec(cmd)  # pylint: disable=exec-used
sys.exit(0)  # Semaphore tracker doesn't explicitly sys.exit.
