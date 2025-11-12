from logging import getLogger
from pathlib import Path
from datetime import datetime
from shutil import copytree
from time import sleep
import schedule


class BackupScheduler:

    # Initialazing vars
    def __init__(self, source, target, interval=10):
        self.source = Path(source).expanduser()
        self.target = Path(target).expanduser()
        self.interval = interval
        self.logger = getLogger(f'App.{self.__class__.__name__}')

    # Main function
    def backup(self):
        self.logger.info('Starting Backup Scheduler App...')

        self.logger.info('Starting schedule and create dirs...')
        self._start_schedule()  # Start schedule and create dir

    # Function creating new dir named current timestamp and copy files into it
    def _make_dir(self):

        self.logger.debug('Starting "_create_dir" function....')
        self.logger.info('Creating backup of directory...')

        now = datetime.now().strftime('%Y-%m-%d_%H-%M')  # Set time format
        self.logger.debug(f'Current timestamp - {now}')

        new_dir = (self.target / Path(now))  # Creating new path
        self.logger.debug(f'Creating new path: {new_dir}')

        self.logger.debug(f'Copying files from {self.source} to {new_dir}...')

        try:
            copytree(self.source, new_dir, dirs_exist_ok=True)  # Copy files
        except BaseException:
            self.logger.exception(BaseException)
        else:
            self.logger.info('Directory copy successfully')

    # Function starting scheduler
    def _start_schedule(self):

        self.logger.debug('Starting "_start_schedule" function....')

        self.logger.info('Setting scheduler...')
        schedule.every(self.interval).minutes.do(
            lambda: self._make_dir())  # Set schedule every * minutes

        self.logger.info('Scheduler is ready')
        self._make_dir()  # Create first backup

        while True:
            schedule.run_pending()  # Checking queue of schedule
            sleep(1)
