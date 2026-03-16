# Prompt: WALL-E Robot Recreation

**Model used:** Claude (via Claude Code + Blender MCP)  
**Task type:** Agentic — Claude receives a reference image and autonomously builds the robot  
**Blender version:** 4.5

---

## The Goal

Recreate the WALL-E robot from Pixar using only primitive geometries (cubes, cylinders, spheres) inside Blender — guided by a reference image fed to Claude.

---

## Reference Image Prompt

```
I'm attaching an image of the WALL-E robot from Pixar.
Using only Blender primitive objects (cubes, cylinders, spheres, torus),
please reconstruct this robot as closely as possible.

Guidelines:
- Start with the main body (boxy torso)
- Add treads/tracks at the bottom
- Add the two large binocular eyes on top
- Add articulated arms on the sides
- Assign appropriate materials (dirty metal, rubber tracks, glass lenses)
- Once assembled, position a camera to frame the robot nicely
  and render it using Cycles
```

---

## What Claude Did (Step by Step)

1. **Analyzed the reference** — identified key shapes: rectangular torso, cylindrical eyes on a neck, box-like treads, thin arms
2. **Built the torso** — scaled cube, slightly flattened, with a dark metallic material
3. **Created treads** — two elongated boxes with a rubber-like material, positioned at the base
4. **Built the eye assembly** — two cylinders (binoculars) on a short neck cylinder, glass material with slight emission for the lens
5. **Added arms** — thin rectangular extrusions on each side with hinge-like joints
6. **Applied materials** — dirty metal (high roughness, slight metallic), rubber (non-metallic, high roughness), glass lens (transmission = 1.0)
7. **Set up camera** — 3/4 front view, slight low angle looking up at WALL-E
8. **Rendered** — Cycles, 256 samples, denoising on

---

## Prompt Refinements Used

```
The eyes look too perfect — can you tilt them slightly inward
to give WALL-E his characteristic curious expression?
```

```
The treads are too clean. Add a slightly darker, worn material
with roughness around 0.85 to make them look used.
```

---

## Results

- **Accuracy:** ~70% resemblance to the original character
- **Time:** ~4 minutes of agent execution
- **Manual corrections needed:** Eye tilt angle, arm proportions

---

## Key Observations

- Claude is excellent at **spatial planning** — it correctly reasoned about relative object sizes and positions
- **Material assignment** was surprisingly good on the first attempt
- Complex organic shapes (like WALL-E's expressive eye movements) are still beyond primitive geometry
- Best results come from providing a **reference image + clear part-by-part instructions**

---

## Tips for Character Recreation

1. Break the character into named parts in your prompt ("torso", "left arm", "right eye")
2. Give approximate dimensions: "the torso should be roughly 2x wider than it is tall"
3. Ask Claude to "pause and describe what it has built so far" before adding the next part
4. Use follow-up prompts to refine — don't try to get it perfect in one shot
