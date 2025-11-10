from pathlib import Path

def register_parser(subparsers):
    
    # Creating subparser for System Montoring app
    monitor = subparsers.add_parser(
        'monitor',
        help        =   'Starting System Montoring app',
        description =   'System Montoring app'
    )
    
    # Adding arguments for System Montoring app
    monitor.add_argument(
        '--logfile',
        type        = Path,
        required    = True,
        help        = 'The destination - where to logging resourses'
    ) # Add command --logfile
    monitor.add_argument(
        '--interval',
        type        = int,
        required    = True,
        help        = 'The interval to logging monitoring'
    ) # Add command --monitor