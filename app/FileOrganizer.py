from logging import getLogger
from pathlib import Path
from shutil import move
from app.config import FILE_TYPES


class FileOrganizer:

    # Initialazing vars
    def __init__(self, source, target):
        self.source = Path(source).expanduser()
        self.target = Path(target).expanduser()
        self.file_types = FILE_TYPES
        self.logger = getLogger(f'App.{self.__class__.__name__}')

    # Main function
    def organize(self):
        self.logger.info('Starting File Organizer App...')

        self.logger.debug(f'Creating "{self.target}" if not exist...')
        self.target.mkdir(exist_ok=True)

        self.logger.info('Creating directories...')
        self._make_dirs()  # Making dirs

        self.logger.info('Moving files into directories...')
        self._get_types_files()  # Moving files

    # Function to make directories if not exist
    def _make_dirs(self):
        self.logger.debug('Starting "_make_dirs" function...')

        for dir in self.file_types:
            self.logger.debug(f'Value of "dir": {dir}')

            try:
                self.logger.debug('Cretaing new full path')
                (self.target / Path(dir)).mkdir(exist_ok=True)  # Make path

            except BaseException:
                self.logger.exception(BaseException)
                continue

            self.logger.debug(f'Created dir: {self.target / Path(dir)}')

        self.logger.info('Directories is created')

    # Function to define types of files in directory
    def _get_types_files(self):

        self.logger.debug('Starting "_get_types_files" function...')

        for key, value in self.file_types.items():
            self.logger.debug(f'Key: {key}, Value: {value}')

            for file in self.source.iterdir():

                if file.is_dir():
                    self.logger.debug('Skip the file. Its directory...')
                    continue

                file_suffix = file.suffix.lower()  # Get suffix of file

                self.logger.debug(f'File: {file}')
                self.logger.debug(f'Suffix: {file_suffix}, Value: {value}')

                if file_suffix in value:
                    self._move_files(file, (self.target / Path(key)))

    # Function to move files nito dirs
    def _move_files(self, file, src):

        self.logger.debug('Starting "_move_files" function...')
        self.logger.debug(f'Moving File: {file} into Dir: {src}')

        try:
            # Moving file into dir
            move(file, src)
        except BaseException:
            self.logger.exception(BaseException)
        else:
            self.logger.info('Files moved successfully')
