import bpy

bl_info = {
    "name": "Orbit method switch",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Header",
    "description": "Convenient orbit method toggle switch.",
    "category": "Interface",
}

def toggle_orbit_method(self, context):
    layout = self.layout
    inputs = bpy.context.preferences.inputs
    
    row = layout.row(align=True)
    row.prop_enum(inputs, "view_rotate_method", "TURNTABLE", text="", icon="ORIENTATION_GLOBAL")
    row.prop_enum(inputs, "view_rotate_method", "TRACKBALL", text="", icon="ORIENTATION_GIMBAL")

def register():
    bpy.types.VIEW3D_HT_header.append(toggle_orbit_method)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(toggle_orbit_method)
