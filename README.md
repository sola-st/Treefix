# Treefix: Enabling Execution with a Tree of Prefixes

This repository contains the implementation of Treefix and supplementary material for the paper "Treefix: Enabling Execution with a Tree of Prefixes" (ICSE'25).

Paper: https://arxiv.org/pdf/2501.12339

## Getting Started Guide

1. Follow the installation instructions in [INSTALL.md](INSTALL.md).
2. Follow the usage instructions in [USE.md](USE.md).

## Replication Guide

To reproduce the results from the paper, follow these instructions. The results of the following instructions are provided in the `Available Data` section bellow, i.e., you can also inspect them there to skip some of the below steps.

First, install Treefix using the instructions above.

### Effectiveness at Covering Code Overall and per Step (RQ1 and RQ2)

We evaluate Treefix on two datasets containing Python code snippets. These datasets are available at `./so_snippets` and `./popular_projects_snippets_dataset`. 
The used files are listed at `./so_snippets_dataset.txt` and `./popular_projects_snippets_dataset.txt`. 

1. Create a folder to store the metrics for each code snippet:
```
mkdir metrics
```

2. Run Treefix on the chosen dataset:

For the Stack Overflow snippets, run:
```
python -m l3.Run --files ./so_snippets_dataset.txt --openai_api_key $OPENAI_API_KEY
```
For the Open-source functions, run:
```
python -m l3.Run --files ./popular_projects_snippets_dataset.txt --openai_api_key $OPENAI_API_KEY
```

The coverage achieved by Treefix on each snippet will be available on a `raw` folder.

3. Get the average coverage achieved by Treefix on the snippets on each step:
```
python -m l3.evaluation.CombineData
```

The average results, such as the ones presented at Tables II and III of the paper, will be available on a `*_grouped.csv` file, where the coverage achieved by the set of prefixes P is in column `coverage_percentage` and the coverage achieved by p_best is in column `max_coverage_prediction_value`.

### Diversity of Values (RQ4)

1. Get the list of `.csv` files generated on the same folder of the original code snippets, i.e. at `./so_snippets` and `./popular_projects_snippets_dataset`. Write the path of the `.csv` files to a `.txt` file, e.g.  `model_predictions.txt`

2. Calculate the predictions diversity:
```
python -m l3.evaluation.CalculatePredictionsDiversity --files model_predictions.txt
```

The output of this is a raw JSON file: `treefix_types_and_values.json`.

3. Summarize the values, similarly to Table IV in the paper:
```
python -m l3.evaluation.SummarizePredictionsDiversity
```

### Efficiency and Costs (RQ5)

1. Get the list of `.csv` files generated on the same folder of the original code snippets, i.e. at `./so_snippets` and `./popular_projects_snippets_dataset`. Write the path of the `.csv` files to a `.txt` file, e.g.  `model_predictions.txt`

2. Calculate the price:
```
python -m l3.evaluation.CalculatePrice --files model_predictions.txt
```

## Available Data

The data from our experiments can be found in the following folders:

1. The prompts and model responses for each snippet are available in .csv files at:
```
./so_snippets_full_with_gpt4o
```
```
./so_snippets_full_with_gpt4omini
```
```
popular_projects_snippets_dataset_full_with_gpt4o
```
```
popular_projects_snippets_dataset_full_with_gpt4omini
```

2. The overall metrics and metrics for each snippet and model are available at:
```
./metrics_full_datasets_with_GPT4o
```
```
./metrics_full_datasets_with_GPT4o_mini
```

3. The case studies are available at:
```
./case_studies
```

