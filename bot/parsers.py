import configparser
from os import path, getcwd


BASE_DIR = path.abspath(getcwd())


class IniParser:

    def __init__(self, file_path=None):
        self._path = file_path or BASE_DIR+'/bot_rules.ini'
        self._parser = configparser.ConfigParser()
        self.settings = {}

    def _validate_path(self):
        if not path.isfile(self._path):
            raise FileNotFoundError(
                'Config File not found: {}'.format(self._path))

    def _parse(self):
        self._parser.read(self._path)
        keys = self._parser.sections()
        for key in keys:
            self.settings[key] = self._config_section_map(key)

    def _config_section_map(self, section):
        _d = {}
        options = self._parser.options(section)
        for option in options:
            try:
                _d[option] = int(self._parser.get(section, option))
            except configparser.NoOptionError:
                _d[option] = None
        return _d

    def parse(self) -> dict:
        self._validate_path()
        self._parse()
        return self.settings
