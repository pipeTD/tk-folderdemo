# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
App that launches applications.

"""

import sgtk
import os

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtGui
from sgtk.platform import Application

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


class SetDVSRootApp(Application):
    """
    Multi App to launch applications.
    """

    # documentation explaining how to reconfigure app paths

    def init_app(self):
        """
        Called as app is being initialized
        """
        self.engine.register_command("Folder Picker", self.run_app)

    def run_app(self):
        self.export_path = QtGui.QFileDialog.getExistingDirectory(QtGui.QApplication.activeWindow(), "Folder Picker", os.getcwd(), QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.DontResolveSymlinks)
        if self.export_path:
            logger.debug("export_path: {}".format(self.export_path))
