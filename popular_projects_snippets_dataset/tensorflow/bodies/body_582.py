# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/upload_test_benchmarks.py
"""Parse benchmark data and use the client to upload it to the datastore.

  Parse the given benchmark data from the serialized JSON-format used to write
  the test results file.  Create the different datastore Entities from that data
  and upload them to the datastore in a batch using the client connection.

  Args:
    client: datastore client connection
    data: JSON-encoded benchmark data
  """
test_result = json.loads(data)

test_name = str(test_result["name"])
start_time = datetime.datetime.utcfromtimestamp(
    float(test_result["startTime"]))
batch = []

# Create the Test Entity containing all the test information as a
# non-indexed JSON blob.
t_key = client.key("Test")
t_val = datastore.Entity(t_key, exclude_from_indexes=["info"])
t_val.update({"test": test_name, "start": start_time, "info": str(data)})
batch.append(t_val)

# Create one Entry Entity for each benchmark entry.  The wall-clock timing is
# the attribute to be fetched and displayed.  The full entry information is
# also stored as a non-indexed JSON blob.
for ent in test_result["entries"].get("entry", []):
    ent_name = str(ent["name"])
    e_key = client.key("Entry")
    e_val = datastore.Entity(e_key, exclude_from_indexes=["info"])
    e_val.update({
        "test": test_name,
        "start": start_time,
        "entry": ent_name,
        "timing": ent["wallTime"],
        "info": str(json.dumps(ent))
    })
    batch.append(e_val)

# Put the whole batch of Entities in the datastore.
client.put_multi(batch)
