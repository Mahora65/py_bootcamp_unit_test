from io import StringIO
import unittest

def call_unit_test(MyTestCase):
    stream = StringIO()
    runner = unittest.TextTestRunner(stream= stream)
    result = runner.run(unittest.makeSuite(MyTestCase))
    test_run = result.testsRun
    errors = result.errors
    failures = result.failures
    stream.seek(0)
    test_output = stream.read()
    return test_run, errors, failures, test_output

