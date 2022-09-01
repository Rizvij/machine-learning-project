import logging
from datetime import datetime

LOG_DIR="housing_logs"

CURRENT_TIME_STAMP= f"{datetime.now().strftime('%y-%m-%d_%H-%M-%s')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w" ,
format='[%(sctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO

)