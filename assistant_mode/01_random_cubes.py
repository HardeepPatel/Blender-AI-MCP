"""
Script: 01_random_cubes.py
Description: Clear the scene and generate 5 cubes with random sizes
             and random positions along the X-axis.

Usage: Open in Blender Text Editor and click Run Script.
Generated with: ChatGPT 5.1 (Assistant Mode)
"""

import bpy
import random


def clear_scene():
    """Remove all mesh objects from the scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_random_cubes(count=5):
    """Create cubes with random scale and X position."""
    for i in range(count):
        scale_x = random.uniform(0.3, 2.0)
        scale_y = random.uniform(0.3, 2.0)
        scale_z = random.uniform(0.3, 2.0)
        x = random.uniform(-5, 5)

        bpy.ops.mesh.primitive_cube_add(location=(x, 0, 0))
        cube = bpy.context.active_object
        cube.name = f"RandomCube_{i+1}"
        cube.scale = (scale_x, scale_y, scale_z)

    print(f"✅ Created {count} random cubes.")


# --- MAIN ---
clear_scene()
create_random_cubes(count=5)
