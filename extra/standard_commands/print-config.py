"""Print the full configuration."""

import yaml
from . import DodoCommand


class Command(DodoCommand):  # noqa
    def handle_imp(self, **kwargs):  # noqa
        print(yaml.dump(self.config))
