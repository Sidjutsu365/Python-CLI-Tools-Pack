from logging import getLogger
import argparse
from app import FileOrganizer, BackupScheduler, SystemMonitoring
from commands import organizer, backup, monitor
from logging_setting import set_logging


def get_arguments():

    parser = argparse.ArgumentParser(
        prog='CLI Application',
        description='My first CLI Application'
    )  # Creating new parser

    subparsers = parser.add_subparsers(
        dest='app',
        required=True
    )  # Creating new subparser

    # Add subparsers arguments for each app
    organizer.register_parser(subparsers)
    backup.register_parser(subparsers)
    monitor.register_parser(subparsers)

    args = parser.parse_args()  # Parsing arguments

    return args


logger = getLogger('App')  # Get logger name
set_logging(logger)

logger.info('Starting CLI Application...')
logger.info('Setting logging...')
logger.info('Parsing arguments from command line...')
args = get_arguments() # Get arguments
logger.debug(f'Arguments is {args}')
logger.debug(f'Starting chosen {args.app} app...')

match args.app:
    case 'backup':
        app = BackupScheduler.BackupScheduler(
            args.source,
            args.target,
            args.interval
        )
        app.backup()
    case 'organizer':
        app = FileOrganizer.FileOrganizer(
            args.source,
            args.target
        )
        app.organize()
    case 'monitor':
        app = SystemMonitoring.SystemMonitoring(
            args.logfile,
            args.interval
        )
        app.monitoring()

logger.info('Exiting from CLI Application...')
