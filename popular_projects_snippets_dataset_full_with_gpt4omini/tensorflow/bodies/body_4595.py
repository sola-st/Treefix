# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/sleep/sleep_bin.py
del argv  # not used
delay_seconds = 1.0
print("""
Using synchronous sleep op with each of 50 ops sleeping for about %0.2f seconds,
so total time is about %0.2f * ceil(50 / NUMBER_OF_THREADS). 16 is a typical
number of threads, which would be %0.2f seconds. The actual time will be
a little greater.
""" % (delay_seconds, delay_seconds, delay_seconds * math.ceil(50.0 / 16.0)))
stack50(sleep_op.SyncSleep, delay_seconds)

print("""
Using asynchronous sleep op with each of 50 ops sleeping only as much as
necessary so they finish after at least %0.2f seconds. Time that
an op spends blocked waiting to finish counts as all or part of its delay.
The returned values show how long each ops sleeps or 0 if the op does not
need to sleep. The expected total time will be a little greater than
the requested delay of %0.2f seconds.
""" % (delay_seconds, delay_seconds))
stack50(sleep_op.AsyncSleep, delay_seconds)
