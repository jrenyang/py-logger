import os
import datetime
import logging

def get_logger(p_name, log_dir, log_file_name, log_file_append_date=False):
    os.makedirs(log_dir, exist_ok=True)
    
    formatter = logging.Formatter(
        "%(asctime)s  %(levelname)s {:<5} --- {}: %(message)s".format(os.getpid(), p_name)
    )

    file_path = os.path.join(log_dir, log_file_name + ".log")

    if log_file_append_date:
        file_path = os.path.join(log_dir, datetime.datetime.now().strftime("%Y%m%d") + "_" + log_file_name + ".log")
        
    file_handler = logging.FileHandler(filename=file_path, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(p_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

def log(logger):
    def decorator(func):
        def run(*args):
            logger.info("==================== Start ====================")
            func(*args)
            logger.info("====================  END  ====================") 
        return run
    return decorator

def process_log(logger, process_name):
    def decorator(func):
        def run(*args):
            logger.info("Start Process: %s" % process_name)
            func(*args)
            logger.info("Finish Process: %s" % process_name) 
        return run
    return decorator