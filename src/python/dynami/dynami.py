import argparse
from pathlib import Path

from ext.utils.config import ConfigControl

control = ConfigControl("test.json")
control.set("server", "server")
control.save()