import logging
import sys
from pythonjsonlogger import jsonlogger

logger = logging.getLogger("uvicorn.access")
logger.setLevel(logging.INFO)

log_handler = logging.StreamHandler(sys.stdout)
formatter = jsonlogger.JsonFormatter()

log_handler.setFormatter(formatter)
logger.handlers = [log_handler]
