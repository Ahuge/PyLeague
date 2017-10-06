from PyLeague.logger import log


class BaseWeights(object):
    RESULTS_KEY = 0
    SIZE_KEY = 1
    TIME_KEY = 2

    def __init__(self):
        super(BaseWeights, self).__init__()
        self._size = None
        self._results = None
        self._time = None

    def calculate_results(self, results):
        points = 0
        for expected_result, result in results[True]:
            if expected_result == result:
                log.success(
                    "In expected: \"%s\", got \"%s\"..." % (
                        expected_result, result
                    )
                )
                points = min([points, points-1])
            else:
                log.error(
                    "In expected: \"%s\", got \"%s\"..." % (
                        expected_result, result
                    )
                )
                points += 1
        for expected_result, result in results[False]:
            log.error(
                "In expected: \"%s\", got \"%s\"..." % (
                    expected_result, result
                )
            )
            points += 1
        return points

    def calculate_size(self, size):
        points = len(size)
        return points

    def calculate_time(self, time):
        points = time * 1000  # ms to s
        return points

    def get_results(self, key):
        if key == self.RESULTS_KEY:
            return self.calculate_results(self.results)
        elif key == self.SIZE_KEY:
            return self.calculate_size(self.size)
        elif key == self.TIME_KEY:
            return self.calculate_size(self.time)
        else:
            log.warning("Unknown key: %s" % key)

    def print_results(self):
        for name, key in [("RESULTS", self.RESULTS_KEY), ("SIZE", self.SIZE_KEY), ("TIME", self.TIME_KEY)]:
            points = self.get_results(key)
            log.header()
            log.info(
                "Score for %s:" % name
            )
            log.line()
            log.info(
                "Points: %d:" % points
            )
            log.line()


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def results(self):
        return self._results

    @results.setter
    def results(self, value):
        self._results = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


class BaseTest(object):
    def __init__(self, args=(), result=None):
        super(BaseTest, self).__init__()
        self.args = args
        self.result = result

    def __iter__(self):
        yield self.args
        yield self.result


class BaseChallenge(object):
    TESTS = []
    user_function_name = "function"

    def __init__(self, weights):
        super(BaseChallenge, self).__init__()
        self.weights = weights

    @property
    def tests(self):
        return self.TESTS

    @tests.setter
    def tests(self, value):
        raise NotImplementedError
