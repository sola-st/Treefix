# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
cv = threading.Condition()
count = [0]
num_threads = 10

def execution_mode_test(cond, count, num_threads, ctx, mode):
    cond.acquire()
    # Ensure that all threads set their mode simultaneously
    # Note that this is not a simple assignment, as the execution_mode is an
    # @property with a custom setter.
    ctx.execution_mode = mode
    count[0] = count[0] + 1
    if count[0] < num_threads:
        cond.wait()
    else:
        cond.notify_all()
    cond.release()
    self.assertEqual(ctx.execution_mode, mode)

ctx = context.Context()
threads = []
for i in range(num_threads):
    t = threading.Thread(
        target=execution_mode_test,
        args=(cv, count, num_threads, ctx,
              context.SYNC if i % 2 == 0 else context.ASYNC))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
