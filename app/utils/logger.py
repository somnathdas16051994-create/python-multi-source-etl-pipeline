import logging

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO
)

logger = logging.getLogger(__name__)