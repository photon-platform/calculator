"""The main application class for the viewer."""

#  from argparse import ArgumentParser, Namespace
#  from webbrowser import open as open_url

#  from textual import __version__ as textual_version  # pylint: disable=no-name-in-module
#  from textual.app import App

#  from .. import __version__
#  from ..data import load_config
#  from ..screens import Main
#  from ..utility.advertising import APPLICATION_TITLE, PACKAGE_NAME

from .calculator import CalculatorApp


def run() -> None:
    """Run the application."""
    CalculatorApp().run()
