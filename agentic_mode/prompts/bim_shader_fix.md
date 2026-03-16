# Prompt: BIM Shader Fix + Photorealistic Render

**Model used:** Claude (via Claude Code + Blender MCP)  
**Task type:** Agentic — Claude autonomously inspects and fixes shaders, sets up lighting & camera

---

## The Problem

After importing a BIM model using the **Bonsai** extension for Blender, all materials appear flat/grey in Material Preview mode. The IFC-assigned colors are not rendering correctly.

---

## Prompt Given to Claude

```
I have just imported a BIM (IFC) model into Blender using the Bonsai extension.
When I switch to Material Preview or Rendered view, all objects appear the same grey color —
the IFC material colors are not showing.

Please:
1. Inspect all materials in the current Blender scene
2. Identify why the colors are not visible (likely missing Principled BSDF connections
   or emission-only materials without proper shader nodes)
3. Fix ALL shaders so the IFC colors display correctly in Material Preview
4. Once fixed, set up a camera and 3-point lighting rig for a photorealistic
   architectural visualization of the house model
5. Render the scene using Cycles at 1920x1080 and save the output
```

---

## What Claude Did (Agentic Steps)

1. **Sensed the scene** — queried all objects and their material slots via MCP
2. **Diagnosed the issue** — detected materials using `Emission` nodes without `Principled BSDF`, causing no PBR response in Material Preview
3. **Fixed 300+ shaders** — replaced broken shader trees with correct `Principled BSDF` nodes, connecting IFC color data to `Base Color` input
4. **Set up camera** — positioned at ~45° angle, 15m distance, framing the full building
5. **Added lighting** — HDRI world lighting + one sun lamp at low angle for architectural shadows
6. **Rendered with Cycles** — 128 samples, denoising enabled, saved to `/tmp/bim_render_day.png`

---

## Follow-up Prompt (Night Scene)

```
Excellent work! Now create a night-time version of the same render.
- Dark sky (deep navy/black)
- Soft warm interior light bleeding through the windows
- A subtle ambient fill to show the building silhouette
- Keep the same camera angle
```

---

## Results

| Version | Description |
|---|---|
| Daytime | Clean architectural render, all materials correct, natural sunlight |
| Night | Dark exterior, warm orange glow from windows, moody atmosphere |

---

## Key Takeaway

> **This is the most practical use case for Agentic AI in Blender.**  
> Fixing 300 shaders manually would take 1–2 hours.  
> Claude did it in under 60 seconds.

---

## Tips for BIM Projects

- Always use **Bonsai** for IFC imports (not the built-in IFC importer)
- After import, IFC materials often use `Diffuse BSDF` or bare emission — Claude can detect and fix this automatically
- Prompt Claude to "describe what it sees" before making changes — it will catch issues you haven't noticed
- For night renders, specify a hex color for interior light (e.g. `#FFB347` for warm tungsten)
