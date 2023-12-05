import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_fileppath = os.path.join(log_dir, "running_logs.log")# create directory for log file
os.makedirs(log_dir, exist_ok=True)# create logger with'spam_application'

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_fileppath),
        logging.StreamHandler(sys.stdout)
    ] 
) # create console handler and set level to debug
logger = logging.getLogger("cnnClassifierLogger") # create logger