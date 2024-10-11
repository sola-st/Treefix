# Extracted from ./data/repos/tensorflow/tensorflow/cc/experimental/libtf/tests/generate_testdata.py

model = get_model(MODEL_NAME.value)
path = os.path.join(TESTDATA_PATH.value, MODEL_NAME.value)
saved_model.save(model, path)
