# import logging
# logging.basicConfig(level=logging.DEBUG, format="We have next logging message: "
#                                                 "%(asctime)s:%(levelname)s-%(message)s")
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")

# """
# >>> 2+2*2
# 8
# """
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

import unittest
from main import *

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)
    def test_kwargs(self):
        pass

if __name__ == "__main__":
    unittest.main()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result