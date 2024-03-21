import logging
import os


def setup_logger(name) -> logging.Logger:
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    
    directory = fileDir + "/logs"
    if not os.path.exists(directory):
        os.makedirs(directory)

    debug_handler = logging.FileHandler(directory + "/DEBUG.log")
    info_handler = logging.FileHandler(directory + "/INFO.log")
    warning_handler = logging.FileHandler(directory + "/WARNING.log")
    error_handler = logging.FileHandler(directory + "/ERROR.log")
    critical_handler = logging.FileHandler(directory + "/CRITICAL.log")

    # Set the log level for each handler
    debug_handler.setLevel(logging.DEBUG)
    info_handler.setLevel(logging.INFO)
    warning_handler.setLevel(logging.WARNING)
    error_handler.setLevel(logging.ERROR)
    critical_handler.setLevel(logging.CRITICAL)

    TIME_FORMAT = "%d.%m.%Y %I:%M:%S %p"

    # Create formatters for log messages
    formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s : %(lineno)s - %(message)s', datefmt=TIME_FORMAT)
    debug_handler.setFormatter(formatter)
    info_handler.setFormatter(formatter)
    warning_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    critical_handler.setFormatter(formatter)

    # Add the handlers to the logger
    # logging.basicConfig(level=logging.INFO)

    # logger = logging.getLogger(__name__)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set logger level to the lowest level among handlers

    # Remove default handler added by logging.basicConfig()
    if logger.hasHandlers():
        logger.handlers.clear()


    # Add the handlers to the logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)
    logger.addHandler(critical_handler)
    
    return logger
