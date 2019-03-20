# Set the path
import unittest
import sys
import pathlib
sys.path.append(pathlib.Path(__file__).parents[0])

loader = unittest.TestLoader()
tests = loader.discover('.')
testRunner = unittest.runner.TextTestRunner()

if __name__ == '__main__':
    testRunner.run(tests)
