import os
import logging
from datetime import datetime
import importlib
importlib.reload(logging)

class CustomLogger:
    def __init__(self,logs_dir="logs"):
        #Ensures the logs directory exists
        self.logs_dir = os.path.join(os.getcwd(),logs_dir)
        os.makedirs(self.logs_dir,exist_ok=True)

        LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        LOG_FILE_PATH=os.path.join(self.logs_dir,LOG_FILE)
        
        #Configure Logging
        logging.basicConfig(
            filename = LOG_FILE_PATH,
            format = "[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level = logging.INFO,
            force=True
        )


    def get_logger(self,name=__file__): #gets the file name
        return logging.getLogger(os.path.basename(name))


if __name__ == "__main__":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Custom Logging initialized...")