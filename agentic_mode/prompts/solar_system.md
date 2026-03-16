# Prompt: Solar System Simulation

**Model used:** Claude (via Claude Code + Blender MCP)  
**Task type:** Agentic — full scene generation with animation  
**Blender version:** 4.5

---

## The Goal

Build a complete animated solar system in Blender with all 8 planets orbiting the Sun, realistic relative sizes and distances (simplified), and planetary materials.

---

## Main Prompt

```
Create an animated solar system in Blender with the following requirements:

Planets (in order from the Sun):
Mercury, Venus, Earth, Mars, Jupiter, Saturn (with rings), Uranus, Neptune

For each planet:
- Use a UV Sphere with a size proportional to the real planet (simplified scale)
- Assign a material with the planet's approximate color
- Set up a circular orbit path around the Sun
- Animate the orbit using keyframes — orbital speed should be
  proportional to real orbital periods (Mercury fastest, Neptune slowest)
- Each planet should also rotate on its own axis

For the Sun:
- Large emissive sphere at the origin
- Yellow-orange emission material with strength ~5.0
- Add a point light at the origin to illuminate all planets

Saturn:
- Add a torus around it scaled to represent the ring system
- Ring material should be semi-transparent and light-colored

Background:
- Set the world background to a deep space color (near black, slight blue tint)
- Add a few hundred random star particles

Camera:
- Position above the ecliptic plane at roughly 45 degrees
- Frame the entire solar system in view
- Set focal length to 50mm

Render:
- Output at 1920x1080
- Use Cycles with 128 samples
- Take a screenshot so I can see the result
```

---

## Follow-up Prompts

```
Saturn's rings are rotating incorrectly — they should be locked
to Saturn's equatorial plane and rotate with the planet, not orbit separately.
Can you fix that?
```

```
The Sun looks too flat. Increase the emission strength to 8.0
and add a subtle volumetric glow around it (use a large transparent sphere
with a volume scatter material around the Sun).
```

```
Earth looks too grey. Give it a blue base color with some green patches
to represent land masses, and add a slight atmospheric glow.
```

---

## Results

| Element | Success |
|---|---|
| All 8 planets created | ✅ |
| Orbital animation | ✅ |
| Relative orbital speeds | ✅ (approximate) |
| Saturn rings | ✅ (minor rotation bug, fixed on follow-up) |
| Planet self-rotation | ✅ |
| Emissive Sun with point light | ✅ |
| Star background | ✅ |
| Camera framing | ✅ |
| Cycles render | ✅ |

---

## Limitations Observed

- Saturn's tilt and ring orientation needed a manual correction prompt
- Planet textures are flat colors — Claude cannot load image textures automatically via MCP
- The simplified scale means inner planets are hard to see next to Jupiter/Saturn
- Animation baking (for render output) required an extra follow-up prompt

---

## Tips for Astronomical Scenes

- Ask for **simplified proportional scale** rather than real scale (real scale makes inner planets microscopic)
- Specify orbital period ratios explicitly if accuracy matters
- For textures, use Blender's procedural noise nodes — Claude can set these up programmatically
- Request a "camera tracking" constraint so the camera always looks at the Sun
