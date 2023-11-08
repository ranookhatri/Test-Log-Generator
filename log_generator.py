import logging
import time

# Create loggers for each file
logger1 = logging.getLogger('project1')
logger2 = logging.getLogger('project2')
logger3 = logging.getLogger('project3')

# Set logging levels for each logger
logger1.setLevel(logging.INFO)
logger2.setLevel(logging.DEBUG)
logger3.setLevel(logging.WARNING)

# Create file handlers for each logger
handler1 = logging.FileHandler('project1/p1_log1.log')
handler2 = logging.FileHandler('project2/p2_log1.log')
handler3 = logging.FileHandler('project3/p3_log1.log')

# Set logging levels for each handler
handler1.setLevel(logging.INFO)
handler2.setLevel(logging.DEBUG)
handler3.setLevel(logging.WARNING)

# Create formatters for each handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)
handler3.setFormatter(formatter)

# Add handlers to each logger
logger1.addHandler(handler1)
logger2.addHandler(handler2)
logger3.addHandler(handler3)

# Generate continuous logs with different records
while True:
    # Create log records with random messages
    log_message1 = f'This is a log message for project1 at {time.time()}'
    logger1.info(log_message1)
    log_message2 = f'This is a log message for project2 at {time.time()}'
    logger2.debug(log_message2)
    log_message3 = f'This is a log message for project3 at {time.time()}'
    logger3.warning(log_message3)
    # Sleep for a random amount of time before generating the next log
    time.sleep(20)