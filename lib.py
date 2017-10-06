import importlib
import os
import sys
import time
import traceback


from .exceptions import MisnamedFunctionError, TestingError, \
    TestNotFoundError, SolutionNotFoundError


def timer(func, *args):
    start = time.time()
    try:
        result = func(*args)
    except Exception:
        result = TestingError(
            "Function raised an exception:\n" +
            traceback.format_exc()
        )
    length = time.time() - start
    return length, result


def runner(user_function, test_suite, count=1000):
    total_time = 0.0
    test_results = {
        True: [],
        False: []
    }
    recorded_results = False
    for iteration in range(count):
        for expected_result, args in test_suite:
            length, result = timer(
                user_function, args
            )
            total_time += length

            if not recorded_results:
                if expected_result == result:
                    test_results[True].append(
                        (expected_result, result)
                    )
                else:
                    test_results[False].append(
                        (expected_result, result)
                    )
        recorded_results = True
    return total_time / count, test_results


def _size(user_function):
    return len(
        user_function.func_code.co_code
    )


def test_solution(challenge, user_module):
    weights = challenge.weights

    try:
        user_function = getattr(user_module, challenge.user_function_name)
    except Exception:
        raise MisnamedFunctionError(
            "Was expecting function to be named %s, "
            "but %s could not be found" % (
                challenge.user_function_name,
                challenge.user_function_name
            )
        )

    total_time, test_results = runner(
        user_function=user_function,
        test_suite=challenge.tests
    )

    weights.size = _size(user_function)
    weights.results = test_results
    weights.time = total_time

    weights.print_results()


def __import_challenge(challenge_path, challenge_name):
    print("Adding %s to path" % os.path.dirname(challenge_path))
    sys.path.insert(0, os.path.dirname(challenge_path))

    challenge_module = __import__(challenge_name)
    challenge = getattr(challenge_module, challenge_name, None)
    sys.path.remove(os.path.dirname(challenge_path))
    return challenge


def __import_user_module(module_path):
    if not os.path.exists(module_path):
        raise SolutionNotFoundError(
            "Could not find the solution: %s" % module_path
        )

    directory, module_name = os.path.split(os.path.splitext(module_path)[0])
    sys.path.insert(0, directory)
    try:
        module = __import__(module_name)
    except ImportError as err:
        raise SolutionNotFoundError(
            "Could not import the solution: %s\nError was: %s" % (
                module_path, str(err)
            )
        )
    sys.path.remove(directory)
    return module


def build_testing(challenge_name, module_path):
    print("Building test environemtn for %s" % challenge_name)
    challenge_path = os.path.join(
        os.path.dirname(__file__),
        "challenges",
        challenge_name,
        challenge_name + ".py"
    )
    if not os.path.exists(challenge_path):
        raise TestNotFoundError(
            "Could not find a test with the name %s" % challenge_name
        )

    challenge = __import_challenge(challenge_path, challenge_name)
    if challenge is None:
        raise TestNotFoundError(
            "Could not import a test with the name %s" % challenge_name
        )

    user_module = __import_user_module(module_path)

    test_solution(
        challenge,
        user_module
    )
