# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/gce_failure_handler_test.py

@def_function.function
def train_step():
    model.v.assign_add(constant_op.constant(1.))

strategy.run(train_step)

if current_step == STEPS_PER_EPOCH - 1:
    logging.info('epoch %d finished', current_epoch)
