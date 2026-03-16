"""
Script: 03_colored_cubes.py
Description: Generate 5 non-overlapping cubes each assigned a unique
             random color material (Principled BSDF).

Usage: Open in Blender Text Editor and click Run Script.
       Switch to Material Preview (Z key) to see colors.
Generated with: ChatGPT 5.1 (Assistant Mode)
"""

import bpy
import random
import math


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    # Also remove all existing materials to keep the file clean
    for mat in bpy.data.materials:
        bpy.data.materials.remove(mat)


def make_color_material(name, r, g, b):
    """Create a Principled BSDF material with the given RGB color."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)
        bsdf.inputs["Roughness"].default_value = 0.4
    return mat


def cubes_overlap(pos1, s1, pos2, s2, margin=0.2):
    for axis in range(2):
        if abs(pos1[axis] - pos2[axis]) < (s1 / 2 + s2 / 2 + margin):
            continue
        return False
    return True


def find_valid_position(size, placed, area=8, max_attempts=300):
    for _ in range(max_attempts):
        x = random.uniform(-area, area)
        y = random.uniform(-area, area)
        if all(not cubes_overlap((x, y), size, p, s) for p, s in placed):
            return (x, y)
    return None


def create_colored_cubes(count=5):
    placed = []
    colors = [
        (0.9, 0.2, 0.2),   # red
        (0.2, 0.7, 0.3),   # green
        (0.2, 0.4, 0.9),   # blue
        (0.9, 0.7, 0.1),   # yellow
        (0.7, 0.2, 0.9),   # purple
        (0.1, 0.8, 0.8),   # cyan
        (0.9, 0.5, 0.1),   # orange
    ]
    random.shuffle(colors)

    for i in range(count):
        size = random.uniform(0.6, 1.6)
        pos = find_valid_position(size, placed)
        if pos is None:
            print(f"⚠️  Skipping cube {i+1} — no valid position found.")
            continue

        bpy.ops.mesh.primitive_cube_add(size=size, location=(pos[0], pos[1], size / 2))
        cube = bpy.context.active_object
        cube.name = f"ColorCube_{i+1}"

        r, g, b = colors[i % len(colors)]
        mat = make_color_material(f"Mat_{i+1}", r, g, b)
        if cube.data.materials:
            cube.data.materials[0] = mat
        else:
            cube.data.materials.append(mat)

        placed.append((pos, size))

    print(f"✅ Created {len(placed)} colored cubes. Switch to Material Preview to see colors!")


# --- MAIN ---
clear_scene()
create_colored_cubes(count=5)
