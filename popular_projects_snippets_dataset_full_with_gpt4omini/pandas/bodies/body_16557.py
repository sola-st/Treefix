# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
expected = (
    DataFrame(
        {
            "male": [0, 1, 1, 0, 0, 0],
            "wealth": [
                196087.3,
                316478.7,
                316478.7,
                294750.0,
                294750.0,
                294750.0,
            ],
            "name": [
                "ABN Amro",
                "Robeco",
                "Royal Dutch Shell",
                "Royal Dutch Shell",
                "AAB Eastern Europe Equity Fund",
                "Postbank BioTech Fonds",
            ],
            "share": [1.00, 0.40, 0.60, 0.15, 0.60, 0.25],
            "household_id": [1, 2, 2, 3, 3, 3],
            "asset_id": [
                "nl0000301109",
                "nl0000289783",
                "gb00b03mlx29",
                "gb00b03mlx29",
                "lu0197800237",
                "nl0000289965",
            ],
        }
    )
    .set_index(["household_id", "asset_id"])
    .reindex(columns=["male", "wealth", "name", "share"])
)
exit(expected)
