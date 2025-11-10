import logging
from app.config import LOG_FILE
from pathlib import Path

def set_logging(logger):

    logger.setLevel(logging.DEBUG) # Set basic logging level DEBUG

    # Creating custom logger Handlers
    handler_file = logging.FileHandler(
        filename    =   f'{Path(LOG_FILE).expanduser()}',
        mode        =   'a',
        encoding    =   'UTF-8'
    ) # Created File Handler
    handler_file.setLevel(logging.INFO) # Set logging level for File Handler

    handler_console = logging.StreamHandler() # Console Handler
    handler_console.setLevel(logging.ERROR) # Set logging level for Console Handler

    formatter = logging.Formatter(
        fmt     =   '%(asctime)s - [%(name)s] - [%(levelname)s] - line %(lineno)s - %(message)s',
        datefmt =   '%Y-%m-%d %H:%M:%S'
    ) # Creating custom Formatter

    # Set Formatter for Handlers
    handler_file.setFormatter(formatter)
    handler_console.setFormatter(formatter)

    # Set Handlers for logger
    logger.addHandler(handler_file)
    logger.addHandler(handler_console)