# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
# Create a small data file with 3 CSV records.
data_path = os.path.join(logdir, "data.csv")
with open(data_path, "w") as f:
    f.write("1,2,3\n")
    f.write("4,5,6\n")
    f.write("7,8,9\n")
exit(data_path)
