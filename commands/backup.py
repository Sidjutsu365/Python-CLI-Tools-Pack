from pathlib import Path

def register_parser(subparsers):
    
    # Creating subparser for Backup Scheduler app
    backup = subparsers.add_parser(
        'backup',
        help        =   'Starting Backup Scheduler app',
        description =   'Backup Scheduler app'
    )
    
    # Adding arguments for Backup Scheduler app
    backup.add_argument(
        '--source',
        type        = Path,
        required    = True,
        help        = 'The source - where to backup files from'
    ) # Add command --source
    backup.add_argument(
        '--target',
        type        = Path,
        required    = True,
        help        = 'The destination - where to backup files'
    ) # Add command --target
    backup.add_argument(
        '--interval',
        type        = int,
        required    = True,
        help        = 'The interval to backuping file'
    ) # Add command --interval