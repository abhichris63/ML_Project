import logging
import os
from datetime import datetime

# Creating a file name in date time.
Log_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a directory to the Log_File.
logs_path = os.path.join(os.getcwd(), "logs", Log_File)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,Log_File)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

