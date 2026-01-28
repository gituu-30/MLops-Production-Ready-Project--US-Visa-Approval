import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')}.log"
)

# 🔐 CRITICAL FIX: avoid re-configuring logging if already configured
if not logging.getLogger().handlers:
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s %(name)s - %(message)s",
    )
