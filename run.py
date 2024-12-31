# Project entry point
import logging
import os
from app import create_app

app = create_app()

logger = logging.getLogger("run")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 9900)) # Default port is 9900
    logger.info(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)