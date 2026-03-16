# Prompt: Donut Scene (Classic Blender Tutorial Recreation)

**Model used:** Claude (via Claude Code + Blender MCP)  
**Task type:** Agentic — recreating the iconic Blender beginner tutorial scene  
**Blender version:** 4.5

---

## Background

The Blender Donut Tutorial by Andrew Price (Blender Guru) is the first project almost every Blender user makes. This experiment tests whether an AI agent can recreate it autonomously.

---

## Main Prompt

```
Create the classic Blender donut scene with the following components:

1. DONUT BODY
   - Use a Torus primitive as the base
   - Major radius: 1.0, Minor radius: 0.35
   - Apply a Subdivision Surface modifier (level 3)
   - Material: warm dough color (hex ~#C68642), high roughness (~0.85),
     slightly subsurface scattered to look like baked bread

2. ICING
   - Duplicate the torus and scale it slightly larger (1.05x)
   - Keep only the top half (delete bottom vertices)
   - Give it an irregular, droopy edge using proportional editing OR
     by displacing vertices with a noise modifier
   - Material: pastel pink (#F4A7B9), glossy, roughness ~0.2

3. SPRINKLES
   - Add 20-30 small elongated cylinders (height ~0.15, radius ~0.025)
   - Scatter them randomly across the surface of the icing
   - Each sprinkle gets a different random bright color material
   - Make sure they sit ON the icing surface (no floating)

4. SCENE SETUP
   - Add a simple plane as a table surface beneath the donut
   - 3-point lighting: key light (warm), fill light (cool, lower intensity), rim light
   - Camera: close-up, slightly low angle (~20 degrees), 85mm focal length
   - Depth of field: focus on donut, f-stop 2.8

5. RENDER
   - Cycles renderer
   - 256 samples with denoising
   - 1920x1080
   - Save render and show me the result
```

---

## Challenges Encountered

### Sprinkle Placement
The main challenge was getting sprinkles to sit correctly on the curved icing surface. Claude initially placed them at fixed Z coordinates, causing many to float above or clip through the icing.

**Fix prompt used:**
```
Several sprinkles are floating above the icing. Please use a Shrinkwrap modifier
on each sprinkle object targeting the icing mesh so they conform to the surface.
After applying the Shrinkwrap, rotate each sprinkle to align with the surface normal.
```

After 2 iterations this was resolved.

### Icing Edge Shape
The first attempt produced perfectly flat icing edges. Real donut icing droops slightly.

**Fix prompt used:**
```
The icing edge is too uniform and geometric. Can you add a Displace modifier
to the icing mesh using a Cloud Texture at small scale (~0.3) and low strength (~0.08)
to give the edge a more organic, hand-applied look?
```

---

## Final Results

- **Donut shape:** ✅ Convincing torus with subdivision
- **Dough material:** ✅ Warm brown, slightly subsurface scattered
- **Icing:** ✅ Pink gloss, droopy edge after fix
- **Sprinkles:** ✅ Correctly placed after Shrinkwrap iteration
- **Lighting:** ✅ 3-point setup, warm/cool contrast
- **Render:** ✅ Final Cycles render looked professional at 256 samples

---

## Render Time

~3 minutes on GPU (RTX 3070) at 1920x1080, 256 samples with denoising.

---

## Comparison: AI vs Manual Tutorial

| Aspect | Manual (Beginner) | AI Agent |
|---|---|---|
| Time to complete | 4-6 hours | ~8 minutes |
| Learning value | High | Low |
| Result quality | High (with practice) | Good (80% quality) |
| Iteration speed | Slow | Very fast |
| Fine control | Full | Limited |

---

## Takeaway

For **prototyping and previsualization**, AI is excellent. For learning Blender fundamentals, nothing beats doing it manually. Use AI to quickly test a concept, then refine manually.
