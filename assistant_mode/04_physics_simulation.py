"""
Script: 04_physics_simulation.py
Description: Generate 5 colored cubes floating 10 units above ground,
             then apply rigid body physics so they fall and land on a plane.

Usage: Open in Blender Text Editor and click Run Script.
Generated with: ChatGPT 5.1 (Assistant Mode)
"""

import bpy
import random
import math


def clear_scene():
    """Remove all mesh objects from the scene."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_ground_plane():
    """Create a large ground plane with passive rigid body."""
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
    plane = bpy.context.active_object
    plane.name = "Ground"

    # Add passive rigid body (it won't move, but cubes will collide with it)
    bpy.ops.rigidbody.object_add()
    plane.rigid_body.type = 'PASSIVE'
    plane.rigid_body.collision_shape = 'MESH'
    return plane


def random_color_material(name):
    """Create a new material with a random RGB color."""
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        r = random.random()
        g = random.random()
        b = random.random()
        bsdf.inputs["Base Color"].default_value = (r, g, b, 1.0)
        bsdf.inputs["Metallic"].default_value = random.uniform(0.0, 0.5)
        bsdf.inputs["Roughness"].default_value = random.uniform(0.2, 0.8)
    return mat


def create_physics_cubes(count=5):
    """Create cubes with random sizes, positions, and colors floating above the ground."""
    cubes = []

    for i in range(count):
        # Random size between 0.5 and 1.5 units
        size = random.uniform(0.5, 1.5)

        # Random X/Y position, Z fixed at 10 units above ground
        x = random.uniform(-4, 4)
        y = random.uniform(-4, 4)
        z = 10 + random.uniform(0, 5)  # stagger heights slightly

        # Create the cube
        bpy.ops.mesh.primitive_cube_add(size=size, location=(x, y, z))
        cube = bpy.context.active_object
        cube.name = f"PhysicsCube_{i+1}"

        # Random rotation for more natural falling
        cube.rotation_euler = (
            random.uniform(0, math.pi),
            random.uniform(0, math.pi),
            random.uniform(0, math.pi)
        )

        # Assign random color material
        mat = random_color_material(f"CubeMat_{i+1}")
        if cube.data.materials:
            cube.data.materials[0] = mat
        else:
            cube.data.materials.append(mat)

        # Add active rigid body physics
        bpy.ops.rigidbody.object_add()
        cube.rigid_body.type = 'ACTIVE'
        cube.rigid_body.mass = random.uniform(1.0, 5.0)
        cube.rigid_body.collision_shape = 'BOX'
        cube.rigid_body.restitution = random.uniform(0.1, 0.4)  # slight bounce

        cubes.append(cube)

    return cubes


def setup_scene():
    """Configure scene for physics simulation playback."""
    scene = bpy.context.scene

    # Set frame range
    scene.frame_start = 1
    scene.frame_end = 150
    scene.frame_current = 1

    # Enable rigid body world
    if not scene.rigidbody_world:
        bpy.ops.rigidbody.world_add()

    scene.rigidbody_world.steps_per_second = 60
    scene.rigidbody_world.solver_iterations = 20


# --- MAIN ---
clear_scene()
setup_scene()
create_ground_plane()
cubes = create_physics_cubes(count=5)

print(f"✅ Created {len(cubes)} physics cubes above a ground plane.")
print("Press SPACEBAR in Blender to play the physics simulation!")
