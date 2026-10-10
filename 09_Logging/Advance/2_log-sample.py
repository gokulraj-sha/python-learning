import logging
import employee

# Logger → identifies where the log message comes from
logger = logging.getLogger(__name__)

# Logging level → DEBUG allows DEBUG and all higher-level messages
logger.setLevel(logging.DEBUG)

# Formatter → defines the format/structure of each log message
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# FileHandler → sends log messages to a file
file_handler = logging.FileHandler('Logging/Advance/sample.log')

# Handler level → only ERROR and CRITICAL messages are written to this file
file_handler.setLevel(logging.ERROR)

# Apply the formatter to the file handler
file_handler.setFormatter(formatter)

# StreamHandler → sends log messages to the console/terminal
stream_handler = logging.StreamHandler()

# Apply the formatter to the console handler
stream_handler.setFormatter(formatter) 

# Add handlers → connect the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(a,b): 
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def devision(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        logger.exception("Tried to divede by zero") #.exception, displays detailed error information
        #instead of .exception, if we write error(it just displays the error)
    else:
        return result

num1 =10
num2 = 0


add_result = add(num1, num2)
logger.debug("Add : {} - {} = {}".format(num1, num2, add_result))

sub_result = sub(num1, num2)
logger.debug("Sub : {} - {} = {}".format(num1, num2, sub_result))


multi_result = multi(num1, num2)
logger.debug("Multipication : {} - {} = {}".format(num1, num2, multi_result))


division_result = devision(num1, num2)
logger.debug("Divison : {} - {} = {}".format(num1, num2, division_result))