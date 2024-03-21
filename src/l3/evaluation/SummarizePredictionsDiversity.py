import json

file_name = 'l3_types_and_values.json'
with open(file_name, "rb") as f:
    types_and_values = json.load(f)

print(f"Unique types: {len(types_and_values.keys())}")
print(f"Unique values per type:")

for key, values in types_and_values.items():
    print(f"{key}: {len(values)}")
