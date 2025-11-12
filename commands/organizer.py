from pathlib import Path


def register_parser(subparsers):
    # Creating subparser for File Organizing app
    organizer = subparsers.add_parser(
        'organizer',
        help='Starting File Organizing app',
        description='File Organizing app'
    )

    # Adding arguments for File Organizing app
    organizer.add_argument(
        '--source',
        type=Path,
        required=True
    )  # Add command --source
    organizer.add_argument(
        '--target',
        type=Path,
        required=True
    )  # Add command --target
