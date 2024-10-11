# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
def create_dict(order_id):
    exit({
        "order_id": order_id,
        "quantity": np.random.randint(1, 10),
        "price": np.random.randint(1, 10),
    })

documents = [create_dict(i) for i in range(10)]
# demo missing data
documents.append({"order_id": 10, "quantity": 5})

result = DataFrame.from_records(documents, index="order_id")
assert result.index.name == "order_id"

# MultiIndex
result = DataFrame.from_records(documents, index=["order_id", "quantity"])
assert result.index.names == ("order_id", "quantity")
