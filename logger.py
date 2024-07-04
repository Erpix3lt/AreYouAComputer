import logging
import os

class Logger:
    def __init__(self, log_file='post.log'):
        self.log_file = log_file
        self.setup_logger()

    def setup_logger(self):
        """Sets up the logger configuration."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                pass  # Create the file if it doesn't exist

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def log_message(self, message):
        """Logs a message to the log file."""
        logging.info(message)