"""
Script: 05_bulk_material_update.py
Description: Bulk-update material properties (metallic, roughness, base color tint)
             across ALL objects in the current Blender scene.

             This is extremely useful for BIM models or scenes with hundreds of
             objects where manual shader editing would take hours.

Usage: Open in Blender Text Editor, adjust CONFIG values below, then Run Script.
Generated with: ChatGPT 5.1 (Assistant Mode)
"""

import bpy


# ─── CONFIGURATION ───────────────────────────────────────────────────────────
# Set to None to skip updating that property
CONFIG = {
    "metallic":   0.512,   # 0.0 = fully non-metallic, 1.0 = fully metallic
    "roughness":  None,    # None = don't change roughness
    "specular":   None,    # None = don't change specular
    "emission_strength": None,  # Set to a float to add emissive glow
    # Set to a tuple (R, G, B) to tint all materials, or None to skip
    "color_tint": None,    # e.g. (0.8, 0.9, 1.0) for a cool blue tint
}
# ─────────────────────────────────────────────────────────────────────────────


def update_material(mat):
    """Update a single material's Principled BSDF node properties."""
    if not mat or not mat.use_nodes:
        return False

    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if not bsdf:
        return False

    updated = []

    if CONFIG["metallic"] is not None:
        bsdf.inputs["Metallic"].default_value = CONFIG["metallic"]
        updated.append(f"Metallic={CONFIG['metallic']}")

    if CONFIG["roughness"] is not None:
        bsdf.inputs["Roughness"].default_value = CONFIG["roughness"]
        updated.append(f"Roughness={CONFIG['roughness']}")

    if CONFIG["specular"] is not None:
        # Specular IOR Level in Blender 4.x
        if "Specular IOR Level" in bsdf.inputs:
            bsdf.inputs["Specular IOR Level"].default_value = CONFIG["specular"]
        elif "Specular" in bsdf.inputs:
            bsdf.inputs["Specular"].default_value = CONFIG["specular"]
        updated.append(f"Specular={CONFIG['specular']}")

    if CONFIG["emission_strength"] is not None:
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = CONFIG["emission_strength"]
            updated.append(f"EmissionStrength={CONFIG['emission_strength']}")

    if CONFIG["color_tint"] is not None:
        r, g, b = CONFIG["color_tint"]
        current = bsdf.inputs["Base Color"].default_value
        # Multiply existing color by tint
        bsdf.inputs["Base Color"].default_value = (
            current[0] * r,
            current[1] * g,
            current[2] * b,
            1.0
        )
        updated.append(f"ColorTint={CONFIG['color_tint']}")

    return len(updated) > 0


def bulk_update_all_materials():
    """Iterate every material in the blend file and apply CONFIG updates."""
    total = 0
    skipped = 0

    for mat in bpy.data.materials:
        if update_material(mat):
            total += 1
        else:
            skipped += 1

    return total, skipped


# --- MAIN ---
print("🔄 Starting bulk material update...")
updated, skipped = bulk_update_all_materials()

print(f"✅ Updated {updated} materials successfully.")
print(f"⏭️  Skipped {skipped} materials (no Principled BSDF or no nodes).")
print(f"\nSettings applied:")
for key, val in CONFIG.items():
    if val is not None:
        print(f"  {key}: {val}")
