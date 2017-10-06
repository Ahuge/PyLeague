class TestingError(BaseException): pass


class MisnamedFunctionError(TestingError): pass


class TestNotFoundError(TestingError): pass


class SolutionNotFoundError(TestingError): pass
