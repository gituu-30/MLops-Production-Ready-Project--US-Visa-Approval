import sys
from us_visa.logger import logging
from us_visa.exception import USVisaException

#logging.info("welcome to our custom log")

try:

    a=1/0
except Exception as e:
    raise USVisaException(e,sys)