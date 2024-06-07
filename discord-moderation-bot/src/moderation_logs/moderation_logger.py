import logging

class ModerationLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_moderation_action(self, action, user, reason):
        logging.info(f'{action} - User: {user} - Reason: {reason}')

    def log_auto_moderation(self, action, user, reason):
        logging.info(f'Auto-{action} - User: {user} - Reason: {reason}')

    def log_custom_command(self, command, user):
        logging.info(f'Custom Command - {command} - User: {user}')

    def log_scheduled_message(self, message):
        logging.info(f'Scheduled Message - {message}')

    def log_report(self, reporter, reported_user, reason):
        logging.info(f'Report - Reporter: {reporter} - Reported User: {reported_user} - Reason: {reason}')

    def log_spam_detection(self, user, message):
        logging.info(f'Spam Detected - User: {user} - Message: {message}')