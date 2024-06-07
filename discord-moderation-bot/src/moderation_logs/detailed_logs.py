import logging

class DetailedLogs:
    def __init__(self):
        self.log_file = 'detailed_logs.txt'
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

    def log_action(self, action, user_id, timestamp):
        log_message = f'{timestamp}: User with ID {user_id} performed action: {action}'
        logging.info(log_message)

    def get_logs(self):
        try:
            with open(self.log_file, 'r') as file:
                logs = file.readlines()
                return logs
        except FileNotFoundError:
            return []

    def clear_logs(self):
        open(self.log_file, 'w').close()