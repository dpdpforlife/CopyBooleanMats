# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#  (c) 2018 Dan Pool (dpdp)

import bpy

bl_info = {
    "name": "CopyBooleanMats",
    "author": "Dan Pool (dpdp)",
    "version": (0,0,1),
    "blender": (2, 80,0),
    "description": "Copies the materials from boolean objects to the main object for continuous material updates",
    "location": "Properties > Material > Specials > CopyBooleanMats",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Materials"}

class CopyBooleanMats(bpy.types.Operator):
    """Copy materials from boolean objects"""
    bl_idname = "object.copy_boolean_mats"
    bl_label = "Copy Boolean Mats"
    bl_options = {'REGISTER', 'UNDO'}
    global converted

    @classmethod
    def poll(cls, context):
        return (	(len(context.selected_objects) > 0)
            and  (context.mode == 'OBJECT')	)	
	
    def execute(self, context):
        
        #Selected object with modifiers
        object = bpy.context.active_object      

        for modifier in object.modifiers:
            #Check if modifier is boolean AND has a boolean object selected  
            if modifier.type == "BOOLEAN" and modifier.object:
                bo = modifier.object
                for mat in bo.data.materials:
                    object.data.materials.append(mat)
	return {'FINISHED'}

def register():
    bpy.utils.register_class(CopyBooleanMats)
    bpy.types.MATERIAL_MT_context_menu.append(menu_func)

def unregister():
    bpy.utils.unregister_class(CopyBooleanMats)
    bpy.types.MATERIAL_MT_context_menu.remove(menu_func)

def menu_func(self, context):
    self.layout.separator()
    self.layout.operator(CopyBooleanMats.bl_idname)
	
if __name__ == "__main__":
    register()
