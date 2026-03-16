# Prompt: Minecraft-Style Stonehenge with UFOs

**Model used:** Claude (via Claude Code + Blender MCP)  
**Task type:** Agentic — stylized scene with complex lighting  
**Blender version:** 4.5

---

## The Goal

Create a stylized, Minecraft-inspired Stonehenge scene featuring:
- Voxel/blocky stone monoliths arranged in a circle
- UFOs hovering above
- A central fire casting dynamic light onto the stones
- Dramatic atmospheric rendering

---

## Main Prompt

```
Create a Minecraft-style Stonehenge scene in Blender:

STONEHENGE STRUCTURE:
- Arrange 10 pairs of upright stone pillars in a circle (radius ~6 units)
- Each upright pillar: rectangular box, roughly 0.8 x 0.8 x 2.5 units
- Place a horizontal lintel stone across each pair of uprights
- Lintel: 2.0 x 0.8 x 0.6 units, resting on top of the two pillars
- All stones: grey stone material, high roughness (0.9), slightly varied
  grey tones per stone to avoid uniformity
- Give each stone slightly randomized rotation (±3 degrees) to look weathered

GROUND:
- Large flat plane with a grass-like green material (rough, not shiny)
- Slightly darker circular patch in the center where fire has scorched the earth

FIRE:
- Place a fire/flame in the exact center of the stone circle
- Use an emissive material (orange/red, emission strength ~15)
- Add a Point Light at the fire location: warm orange color (#FF6B1A),
  energy 500W, radius 0.5
- The light should visibly cast on the stone faces nearest to the center

UFOs:
- Add 3 UFOs hovering above the stone circle at different heights (8–14 units)
- Each UFO: flattened sphere (disc shape) with a dome on top
- UFO body material: metallic silver (metallic ~0.9, roughness ~0.15)
- Add subtle green emission on the underside of each UFO (strength ~3)
- Slightly tilt each UFO differently for a dynamic feel

ATMOSPHERE:
- Set world background to a deep dark blue-purple night sky (#0A0A1A)
- Add a single moon-like area light high above for subtle ambient fill
- Light fog/mist: use a low-density volume scatter in the world volume

CAMERA:
- Low angle, outside the stone circle, looking inward and slightly upward
- Frame the fire, 2-3 stones, and at least one UFO in shot
- Focal length: 28mm (wide angle, dramatic)

RENDER:
- Cycles, 256 samples, denoising
- 1920x1080
- Render and show me the result
```

---

## Follow-up Prompts

```
The fire looks like a flat disc. Can you stack 3-4 cone shapes of decreasing
size, each with a slightly more yellow emissive material toward the tip,
to simulate a more 3D flame shape?
```

```
The UFO green underglow is too subtle. Increase emission strength to 8
and also add a small Area Light directly under each UFO (green, 50W)
to cast the glow color onto the stones below.
```

---

## Results

| Element | Result |
|---|---|
| Stone circle geometry | ✅ Correct circular arrangement |
| Lintel placement | ✅ Correctly resting on uprights |
| Stone material variation | ✅ Subtle tone differences |
| Central fire + lighting | ✅ Dynamic orange cast on stones |
| UFO models | ✅ Classic disc + dome shape |
| UFO underglow | ✅ After emission strength fix |
| Night atmosphere | ✅ Deep purple-black sky |
| Camera angle | ✅ Dramatic low wide shot |
| Final render | ✅ Visually striking result |

---

## Lighting Setup Summary

```
World Background: #0A0A1A (near black)
Moon Fill Light: Area, White, 30W, positioned at (0, -20, 30)
Fire Point Light: Orange #FF6B1A, 500W, at (0, 0, 0.5)
UFO Lights (x3): Area, Green #00FF88, 50W, under each UFO
```

---

## Render Notes

- Bloom effect added in Compositor (Glare node, Fog Glow type, threshold 0.8)
- Color grading: slight desaturation + contrast boost in compositor
- Total render time: ~5 minutes on RTX 3070

---

## Takeaway

Stylized/voxel scenes are a sweet spot for AI generation — simple geometries mean fewer errors, and the blocky aesthetic forgives imprecise proportions. Adding atmospheric lighting is where the scene goes from basic to visually impressive.
