import os
import re
import time
import argparse
import subprocess

from .LLMs.GPT import GPTValuePredictor
from .Prompt import Prompt
from .RuntimeStats import RuntimeStats
from .Util import code_executes, count_lines, gather_files, get_undefined_variables, get_undefined_attributes_methods, add_comment_to_uncovered_lines


parser = argparse.ArgumentParser()
parser.add_argument(
    "--files", help="Python files or .txt file with all file paths", nargs="+")
parser.add_argument(
    "--openai_api_key", help="API Key from OpenAI", default="")

prompt = Prompt()

def initiate_predictions(code, instrumented_code, code_file, predictor, runtime_stats):
    start_time = time.time()
    
    undefined_variables = get_undefined_variables(code)
    undefined_attributes_methods = get_undefined_attributes_methods(code)

    predictions_with_unsuccessful_execution = {}
    prediction_index = 0

    if undefined_variables or undefined_attributes_methods:
        # Predict undefined variables and attributes
        initial_prompt = prompt.initial(code, undefined_variables, undefined_attributes_methods)
        predictions = predictor.predict(initial_prompt, code_file)

        for prediction in predictions:
            imports = prediction['imports']
            imports = imports + '\n\n' if imports else imports

            updated_code = f'{imports}{code}'

            # Code with predicted imports only is not executable
            if not code_executes(updated_code):
                initialization = prediction['initialization']
                initialization = initialization + '\n\n' if initialization else initialization

                imports = imports + initialization

                updated_code = f'{imports}{code}'

            updated_file_path = code_file.replace('.py', f'_initial_{prediction_index}.py')
            with open(updated_file_path, "w") as f:
                f.write(f'{imports}{instrumented_code}')
            runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__)

            if not code_executes(updated_code):
                predictions_with_unsuccessful_execution[prediction_index] = prediction
            else:
                runtime_stats.initial_predictions_indexes.append(prediction_index)

            prediction_index += 1
    else:
        updated_code = instrumented_code
        updated_file_path = code_file.replace('.py', f'_initial.py')
        with open(updated_file_path, "w") as f:
            f.write(updated_code)
        runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__)

    runtime_stats.save(code_file, predictor.__class__.__name__, start_time, 'initial')

    return predictions_with_unsuccessful_execution

def refine_predictions(code, instrumented_code, code_file, predictor, predictions, runtime_stats):
    start_time = time.time()

    for index, prediction in predictions.items():
        runtime_stats.refined_predictions_indexes[index] = []

        imports = prediction['imports']
        imports = imports + '\n\n' if imports else imports

        initialization = prediction['initialization']
        initialization = initialization + '\n\n' if initialization else initialization

        imports = imports + initialization
        initialization = ""
            
        # Refine predictions
        with open("temp.py", "w") as f:
            f.write(f'{imports}{initialization}{code}')
        try:
            process = subprocess.run(["python3", "temp.py"], capture_output=True, text=True, check=True, timeout=30)
        except subprocess.CalledProcessError as e:
            lines = e.stderr.splitlines()
            line_number = ""
            for line in lines:
                match = re.search(r'temp.py\", line (\d+)', line)
                if match:
                    line_number = int(match.group(1))

            line_code_and_error_msg = '\n'.join(lines[-2:])
            cleaned_error_msg = f'Execution error at line {line_number}:\n{line_code_and_error_msg}'
        
            refine_prompt = prompt.refine(cleaned_error_msg)
            refined_predictions = predictor.predict(refine_prompt, code_file)

            refined_prediction_index = 0

            for refined_prediction in refined_predictions:
                refined_imports = refined_prediction['imports']
                refined_imports = refined_imports + '\n\n' if refined_imports else refined_imports

                imports = imports + refined_imports

                updated_code = f'{imports}{code}'

                # Code with predicted imports only is not executable
                if not code_executes(updated_code):
                    refined_initialization = refined_prediction['initialization']
                    refined_initialization = refined_initialization + '\n\n' if refined_initialization else refined_initialization

                    imports = imports + refined_initialization

                    updated_code = f'{imports}{code}'

                updated_file_path = code_file.replace('.py', f'_refine_{index}_{refined_prediction_index}.py')
                with open(updated_file_path, "w") as f:
                    f.write(f'{imports}{instrumented_code}')
                runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__)

                if code_executes(updated_code):
                    runtime_stats.refined_predictions_indexes[index].append(refined_prediction_index)

                refined_prediction_index += 1

        except subprocess.TimeoutExpired:
            pass

    runtime_stats.save(code_file, predictor.__class__.__name__, start_time, 'refine')

def guide_predictions(code, instrumented_code, code_file, predictor, runtime_stats):
    start_time = time.time()

    code_with_uncovered_comment = code

    while runtime_stats.coverage_percentage < 1 and runtime_stats.guide_attempt < 10:
        runtime_stats.guided_predictions_indexes[runtime_stats.guide_attempt] = []

        code_with_uncovered_comment = add_comment_to_uncovered_lines(instrumented_code, runtime_stats.executed_lines)

        guide_prompt = prompt.guide(code_with_uncovered_comment)
        guided_predictions = predictor.predict(guide_prompt, code_file)

        guided_prediction_index = 0

        for prediction in guided_predictions:
            imports = prediction['imports']
            imports = imports + '\n\n' if imports else imports

            updated_code = f'{imports}{code}'

            # Code with predicted imports only is not executable
            if not code_executes(updated_code):
                initialization = prediction['initialization']
                initialization = initialization + '\n\n' if initialization else initialization

                updated_code = f'{imports}{initialization}{code}'

                imports = imports + initialization

            updated_file_path = code_file.replace('.py', f'_guide_{runtime_stats.guide_attempt}_{guided_prediction_index}.py')
            with open(updated_file_path, "w") as f:
                f.write(f'{imports}{instrumented_code}')
            runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__)

            if code_executes(updated_code):
                runtime_stats.guided_predictions_indexes[runtime_stats.guide_attempt].append(guided_prediction_index)

            guided_prediction_index += 1

        runtime_stats.guide_attempt += 1

    runtime_stats.save(code_file, predictor.__class__.__name__, start_time, 'guide')

if __name__ == "__main__":
    args = parser.parse_args()

    files = gather_files(args.files)

    for file in files:
        with open(file, "r") as f:
            code = ''.join(f.readlines())

        # Instrument
        subprocess.run(["python", "-m", "l3.Instrument", "--files", file, "--line_coverage_instrumentation"])

        with open(file, "r") as f:
            instrumented_code = ''.join(f.readlines())

        dependencies_dir_path = os.path.dirname(os.path.realpath(file))
        if not os.path.exists(f"{dependencies_dir_path}/temp"):
            os.makedirs(f"{dependencies_dir_path}/temp")

        predictor = GPTValuePredictor(args.openai_api_key)
        runtime_stats = RuntimeStats(predictor)
        runtime_stats.total_lines = count_lines(file)

        predictions_with_unsuccessful_execution = initiate_predictions(code, instrumented_code, file, predictor, runtime_stats)
        refine_predictions(code, instrumented_code, file, predictor, predictions_with_unsuccessful_execution, runtime_stats)
        guide_predictions(code, instrumented_code, file, predictor, runtime_stats)