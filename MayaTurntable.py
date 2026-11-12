import maya.cmds as cmds
import maya.OpenMayaUI as omui

from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

# Turn Table to do week one
# set up your project structure, main functions
# research functions

# Maya Window functions 

def get_main_maya_window():
    pointer = omui.MQtUyil.mainWindow()
    return wrapInstance(int(pointer), QtWidgets.QWidget)

class TurntableGenerator:
    def __init__(self):
        #Animation settings 
        #Output Settings
        #Selected model

    def get_selected_model(self):
        #Find selected model transform 

    def get_model_dimensions(self):
        # Measure model using world bounding box

    def validate_settings(self):
        # check settings before generating turn table

    def create_turntable(self):
        # Take settings and create Turntable


