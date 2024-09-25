from dotenv import load_dotenv
from pathlib import Path
import logging
import os

load_dotenv()

path = Path(__file__).resolve()

logger = logging
logger.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename=path.parent.parent / 'logs/reports.log'
)

bot_config = {
    'bot_token': os.environ.get('BOT_TOKEN'),
}