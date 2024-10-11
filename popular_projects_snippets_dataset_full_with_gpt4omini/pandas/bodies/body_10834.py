# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH 29037
df = DataFrame(
    {
        "package_id": [1, 1, 1, 2, 2, 3],
        "status": [
            "Waiting",
            "OnTheWay",
            "Delivered",
            "Waiting",
            "OnTheWay",
            "Waiting",
        ],
    }
)

delivery_status_type = pd.CategoricalDtype(
    categories=["Waiting", "OnTheWay", "Delivered"], ordered=True
)
df["status"] = df["status"].astype(delivery_status_type)
df["last_status"] = df.groupby("package_id")["status"].transform(max)
result = df.copy()

expected = DataFrame(
    {
        "package_id": [1, 1, 1, 2, 2, 3],
        "status": [
            "Waiting",
            "OnTheWay",
            "Delivered",
            "Waiting",
            "OnTheWay",
            "Waiting",
        ],
        "last_status": [
            "Delivered",
            "Delivered",
            "Delivered",
            "OnTheWay",
            "OnTheWay",
            "Waiting",
        ],
    }
)

expected["status"] = expected["status"].astype(delivery_status_type)

# .transform(max) should preserve ordered categoricals
expected["last_status"] = expected["last_status"].astype(delivery_status_type)

tm.assert_frame_equal(result, expected)
