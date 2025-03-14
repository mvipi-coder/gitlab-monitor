# tests/test_rptodo.py

from gitlab_monitor import __app_name__, __version__
from gitlab_monitor.commandes import commands
from typer.testing import CliRunner

runner = CliRunner()


def test_version():
    result = runner.invoke(commands.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout
