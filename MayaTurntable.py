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
        self.frame_start = 1
        self.frame_end = 120
        self.video_lemgth = 5.0
        self.rotation_speed = 1
        self.rotation_amount = "Full"
        self.rotation_axis = "Y"
        self.direction = "Clockwise"
        self.smooth_spin = True
        #Output Settings
        self.video_name = "Turntable"
        self.save_video = False
        self.output_folder = ""
        #Selected model
        self.selected_model = None
        self.model_center = None
        self.model_size = None


    def get_selected_model(self):
        #Find selected model transform
        selection = cmds.ls(selection=True, long=True)
        if not selection:
            cmds.warning("Please select a model first.")
            return None
        
        node = selection[0]
        if cmds.nodeType(node) == "mesh":
            parents = cmds.listRelatives(node, parents=True, fullPath=True)
            node = parents[0] if parents else None
        if not node or cmds.nodeType(node) != "transform":
            cmds.warning("Please select a model transform or mesh.")
            return None

        self.selected_model = node
        return self.selected_model


    def get_model_dimensions(self):
        # Measure model using world bounding box
        model = self.get_selected_model()
        if not model:
            return None

        bounds = cmds.exactWorldBoundingBox(model)
        self.model_center = (
            (bounds[0] + bounds[3]) / 2.0,
            (bounds[1] + bounds[4]) / 2.0,
            (bounds[2] + bounds[5]) / 2.0
        )
        self.model_size = (
            (bounds[3] - bounds[0]),
            (bounds[4] - bounds[1]),
            (bounds[5] - bounds[2]) 
        )
        return self.model_center, self.model_size

    def validate_settings(self):
        # check settings before generating turn table
        

    def create_turntable(self):
        # Take settings and create Turntable
