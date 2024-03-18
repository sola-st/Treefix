import os
import re
import time
import argparse
import subprocess
from tempfile import NamedTemporaryFile

from .LLMs.GPT import GPTValuePredictor
from .Logging import logger
from .Prompt import Prompt
from .RuntimeStats import RuntimeStats
from .Util import execute_and_capture_error, count_lines, gather_files, get_undefined_variables, get_undefined_attributes_methods, add_comment_to_uncovered_lines


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
        predictions = predictor.predict(initial_prompt, 1, code_file)

        for prediction in predictions:
            if runtime_stats.coverage_percentage < 1:
                imports = prediction['imports']
                imports = imports + '\n\n' if imports else imports

                updated_code = f'{imports}{code}'

                # Code with predicted imports only is not executable
                if execute_and_capture_error(updated_code) is not None:
                    initialization = prediction['initialization']
                    initialization = initialization + '\n\n' if initialization else initialization

                    imports = imports + initialization

                    updated_code = f'{imports}{code}'

                updated_file_path = code_file.replace('.py', f'_initial_{prediction_index}.py')
                with open(updated_file_path, "w") as f:
                    f.write(f'{imports}{instrumented_code}')
                runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__, 1)

                if execute_and_capture_error(updated_code) is not None:
                    predictions_with_unsuccessful_execution[prediction_index] = prediction
                else:
                    runtime_stats.initial_predictions_indexes.append(prediction_index)

                prediction_index += 1
            else:
                break
    else:
        updated_code = instrumented_code
        updated_file_path = code_file.replace('.py', f'_initial.py')
        with open(updated_file_path, "w") as f:
            f.write(updated_code)
        runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__, 1)

    runtime_stats.save(code_file, predictor.__class__.__name__, start_time, prediction_index, 'initial')

    return predictions_with_unsuccessful_execution

def refine_predictions(code, instrumented_code, code_file, predictor, predictions, runtime_stats):
    start_time = time.time()
    num_executions = 0

    for index, prediction in predictions.items():
        if runtime_stats.coverage_percentage < 1:
            runtime_stats.refined_predictions_indexes[index] = []

            imports = prediction['imports']
            imports = imports + '\n\n' if imports else imports

            initialization = prediction['initialization']
            initialization = initialization + '\n\n' if initialization else initialization

            imports = imports + initialization
                
            # Refine predictions
            execution_result = execute_and_capture_error(f'{imports}{code}')
            if execution_result is not None:
                exception, line_number, error_msg = execution_result
                if not isinstance(exception, subprocess.TimeoutExpired):
                    cleaned_error_msg = f'Execution error at line {line_number}:\n{error_msg}'
                    refine_prompt = prompt.refine(cleaned_error_msg)
                    refined_predictions = predictor.predict(refine_prompt, 2, code_file, index)

                    refined_prediction_index = 0

                    for refined_prediction in refined_predictions:
                        if runtime_stats.coverage_percentage < 1:
                            refined_imports = refined_prediction['imports']
                            refined_imports = refined_imports + '\n\n' if refined_imports else refined_imports

                            refined_imports = imports + refined_imports

                            updated_code = f'{refined_imports}{code}'

                            # Code with predicted imports only is not executable
                            if execute_and_capture_error(updated_code) is not None:
                                refined_initialization = refined_prediction['initialization']
                                refined_initialization = refined_initialization + '\n\n' if refined_initialization else refined_initialization

                                refined_imports = refined_imports + refined_initialization

                                updated_code = f'{refined_imports}{code}'

                            updated_file_path = code_file.replace('.py', f'_refine_{index}_{refined_prediction_index}.py')
                            with open(updated_file_path, "w") as f:
                                f.write(f'{refined_imports}{instrumented_code}')
                            runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__, 2, index, refined_prediction_index)

                            refined_prediction_index += 1
                            num_executions += 1
                        else:
                            break
        else:
            break

    runtime_stats.save(code_file, predictor.__class__.__name__, start_time, num_executions, 'refine')

def guide_predictions(code, instrumented_code, code_file, predictor, runtime_stats):
    start_time = time.time()
    num_executions = 0

    predictor.conversation_history = [predictor.conversation_history[0]]
    predictor.conversation_history_size = predictor.count_tokens(predictor.conversation_history)

    code_with_uncovered_comment = code

    while runtime_stats.coverage_percentage < 1 and runtime_stats.guide_attempt < 10:
        runtime_stats.guided_predictions_indexes[runtime_stats.guide_attempt] = []

        code_with_uncovered_comment = add_comment_to_uncovered_lines(instrumented_code, runtime_stats.executed_lines)

        guide_prompt = prompt.guide(code_with_uncovered_comment)
        guided_predictions = predictor.predict(guide_prompt, 3, code_file)

        guided_prediction_index = 0

        for prediction in guided_predictions:
            if runtime_stats.coverage_percentage < 1:
                imports = prediction['imports']
                imports = imports + '\n\n' if imports else imports

                updated_code = f'{imports}{code}'

                # Code with predicted imports only is not executable
                if execute_and_capture_error(updated_code) is not None:
                    initialization = prediction['initialization']
                    initialization = initialization + '\n\n' if initialization else initialization

                    updated_code = f'{imports}{initialization}{code}'

                    imports = imports + initialization

                updated_file_path = code_file.replace('.py', f'_guide_{runtime_stats.guide_attempt}_{guided_prediction_index}.py')
                with open(updated_file_path, "w") as f:
                    f.write(f'{imports}{instrumented_code}')
                runtime_stats.measure_coverage(updated_file_path, predictor.__class__.__name__, 3, runtime_stats.guide_attempt, guided_prediction_index)

                guided_prediction_index += 1
                num_executions += 1
            else:
                break

        runtime_stats.guide_attempt += 1

    runtime_stats.save(code_file, predictor.__class__.__name__, start_time, num_executions, 'guide')

if __name__ == "__main__":
    # import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()

    args = parser.parse_args()

    files = gather_files(args.files)

    for file in files:
        # Restore file in case is already instrument
        subprocess.run(["python", "-m", "l3.Instrument", "--files", file, "--restore"])

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

        print(f"\n=============== Initial predictions for {file} ==================\n")
        predictions_with_unsuccessful_execution = initiate_predictions(code, instrumented_code, file, predictor, runtime_stats)
        print(f"\n=============== Refined predictions for {file} ==================\n")
        refine_predictions(code, instrumented_code, file, predictor, predictions_with_unsuccessful_execution, runtime_stats)
        print(f"\n=============== Guided predictions for {file} ==================\n")
        guide_predictions(code, instrumented_code, file, predictor, runtime_stats)

    
    logger.info("Logging ends")

    # profiler.disable()
    # stats = pstats.Stats(profiler).sort_stats('cumtime')
    # stats.print_stats()

