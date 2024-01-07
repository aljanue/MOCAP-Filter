# Authors: Alberto Jativa
# version ='1.0'
# ----------------------------------------------------------------------------------------------
""" 
Script that implements an interface to apply a curvature filter to motion capture data
"""
# ----------------------------------------------------------------------------------------------
# Addon information
# ----------------------------------------------------------------------------------------------
bl_info = {
    "name": "Curvature Filter for MOCAP",
    "author": "aljanue",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Animation > Filter",
    "description": "Apply a curvature filter to motion capture data",
    "category": "Animation",
}
# ----------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------
import bpy
import os
import sys

dir = os.path.dirname(os.path.realpath(__file__))
if not dir in sys.path:
    sys.path.append(dir)
    
from .addon import FilterByCurvature


class CurvatureFilterPanel(bpy.types.Panel):
    bl_label = "Curvature Filter"
    bl_idname = "OBJECT_PT_curvature_filter_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    @classmethod
    def poll(cls, context):
        return context.object and context.object.type == 'ARMATURE'

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.label(text="Filter value")
        row.prop(obj, "value")

        row = layout.row()
        row.operator("object.filter")

class FilterOperator(bpy.types.Operator):
    bl_idname = "object.filter"
    bl_label = "Filter values"

    def execute(self, context):
        obj = bpy.context.active_object
        threshold = obj.value
        FilterByCurvature(obj, threshold)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(CurvatureFilterPanel)
    bpy.utils.register_class(FilterOperator)
    bpy.types.Object.value = bpy.props.FloatProperty(name = "Value",
                                                     description="Filter value for animation curves",
                                                     min = 0, 
                                                     default = 0.0001,
                                                     precision = 5)

def unregister():
    bpy.utils.unregister_class(CurvatureFilterPanel)
    bpy.utils.unregister_class(FilterOperator)
    del bpy.types.Object.value
if __name__ == "__main__":
    register()