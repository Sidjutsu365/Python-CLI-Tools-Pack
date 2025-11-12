import logging
from pathlib import Path
from subprocess import run
from time import sleep


class SystemMonitoring:

    # Initilazing vars
    def __init__(self, logfile, interval):
        self.logfile = Path(logfile).expanduser()
        self.interval = interval
        self.logger = logging.getLogger(f'App.{self.__class__.__name__}')

    # Main function
    def monitoring(self):

        self._set_logging()  # Setting logging

        while True:

            self.logger.info('Getting system parameters...')
            cpu_usage = self._get_cpu_usage()  # Gettting cpu usage
            mem_usage = self._get_mem_usage()  # Gettting memory usage

            # Logging results
            self.logger.info(f'CPU usage is: {cpu_usage}%')
            self.logger.info(f'Memory usage is: {mem_usage}\n')

            # Sleep time
            sleep(self.interval)

    # Function to get CPU usage
    def _get_cpu_usage(self):

        cpu = run(['top', '-bn1'], capture_output=True, text=True).stdout

        # find str with CPU usage in Top command
        for i in cpu.split('\n'):

            if 'Cpu(s)' in i:
                cpu_usage = i.split(',')[0][9:-3]
                return cpu_usage

    # Function to get Memory usage
    def _get_mem_usage(self):

        # Get Memory usage
        mem = run(['free', '-h'], capture_output=True, text=True)
        mem_usage = mem.stdout.splitlines()[1].split()[2]
        return mem_usage

    def _set_logging(self):
        handler = logging.FileHandler(
            filename=f'{Path(self.logfile).expanduser()}',
            mode='a',
            encoding='UTF-8'
        )  # Created File Handler
        handler.setLevel(logging.INFO)  # Set logging level for File Handler

        formatter = logging.Formatter(
            fmt='%(asctime)s - [%(name)s] - [%(levelname)s] - \
                line %(lineno)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )  # Creating custom Formatter

        # Set Formatter for Handlers
        handler.setFormatter(formatter)

        # Set Handlers for logger
        self.logger.addHandler(handler)
