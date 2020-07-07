from typing import Text

from kubic.command import KubicCommand
from kubic.runnable import KubicRunnable


class KubicTranslator(KubicRunnable):
    def run(self, option: Text) -> KubicCommand:
        command, *options = option.split(" ")
        command = KubicCommand(command, options=options)
        return command
