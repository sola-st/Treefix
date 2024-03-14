import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument(
    "--file", help=".csv file with the model communication log", required=True)
args = parser.parse_args()

# read .csv file and print its content
with open(args.file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    round = 1
    for row in reader:
        prompt = row[0]
        raw_predictions = row[1]
        predictions = row[2]
        print(f"\n================= Round {round} ==================")
        print(f"\nPrompt:\n-------\n{prompt}")
        print(f"\nRaw Predictions:\n----------------\n{raw_predictions}")
        print(f"\nPredictions:\n------------\n{predictions}")
        round += 1
