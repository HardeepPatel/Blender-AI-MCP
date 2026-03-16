"""
Script: 02_non_overlapping_cubes.py
Description: Generate 5 cubes with random sizes placed so they do NOT
             overlap each other. Uses a simple distance check before placing.

Usage: Open in Blender Text Editor and click Run Script.
Generated with: ChatGPT 5.1 (Assistant Mode)
"""

import bpy
import random
import math


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def cubes_overlap(pos1, size1, pos2, size2, margin=0.2):
    """Return True if two axis-aligned cubes overlap (with an extra margin)."""
    for axis in range(2):  # check X and Y only
        half1 = size1 / 2 + margin
        half2 = size2 / 2 + margin
        if abs(pos1[axis] - pos2[axis]) < (half1 + half2):
            continue
        return False
    return True


def find_valid_position(size, placed, area=8, max_attempts=200):
    """Try random positions until one doesn't overlap existing cubes."""
    for _ in range(max_attempts):
        x = random.uniform(-area, area)
        y = random.uniform(-area, area)
        candidate = (x, y)

        overlap = False
        for pos, s in placed:
            if cubes_overlap(candidate, size, pos, s):
                overlap = True
                break

        if not overlap:
            return candidate

    return None  # failed to find a valid spot


def create_non_overlapping_cubes(count=5):
    placed = []  # list of (position, size) tuples

    created = 0
    for i in range(count):
        size = random.uniform(0.5, 1.5)
        pos = find_valid_position(size, placed)

        if pos is None:
            print(f"⚠️  Could not place cube {i+1} without overlap — skipping.")
            continue

        bpy.ops.mesh.primitive_cube_add(size=size, location=(pos[0], pos[1], size / 2))
        cube = bpy.context.active_object
        cube.name = f"Cube_{i+1}"
        placed.append((pos, size))
        created += 1

    print(f"✅ Placed {created}/{count} non-overlapping cubes.")


# --- MAIN ---
clear_scene()
create_non_overlapping_cubes(count=5)
