# Prompt: BIM Wall Modification (Raise Ceiling Height)

**Model used:** Claude (via Claude Code + Blender MCP)  
**Task type:** Agentic — parametric BIM geometry modification  
**Blender version:** 4.5  
**BIM Tool:** Bonsai extension (IFC import)

---

## The Goal

Modify the ceiling height of an imported BIM model from 3.0m to 4.0m, while preserving door and window openings — simulating a design change workflow.

---

## Main Prompt

```
I have a BIM house model open in Blender (imported via Bonsai IFC).
The current floor-to-ceiling height is 3.0 meters.

I want to raise it to 4.0 meters (add 1.0m to the ceiling height).

Please modify the model with these constraints:

1. WALLS — raise all vertical wall objects by 1.0m (extend their height)
   Do NOT move the wall base — only stretch upward from the top

2. ROOF SLAB — move the entire roof/ceiling slab up by exactly 1.0m
   The roof slab should translate on Z by +1.0, not scale

3. DOORS — preserve door openings:
   - Door heights should remain unchanged (standard door height ~2.1m)
   - The wall above each door should be extended to fill the new gap
     between the door top and the raised ceiling

4. WINDOWS — preserve window openings:
   - Window positions and sizes should remain unchanged
   - The wall above/below each window should adjust to the new wall height

5. SANITY CHECK — after making changes:
   - Report the new height of a representative wall element
   - Confirm the roof slab Z position has changed by exactly 1.0m
   - Flag any objects that could not be modified

Please proceed step by step and report after each major change.
```

---

## Agent Execution Log (Summary)

### Step 1: Wall Height Extension
Claude identified all wall objects (IFC class `IfcWall`) and extended their Z scale to match the new 4.0m target. Correctly calculated the scale factor relative to each wall's current height.

### Step 2: Roof Slab Translation
The roof slab (IFC class `IfcSlab` with PredefinedType `ROOF`) was translated +1.0m on the Z axis. ✅

### Step 3: Door Opening Preservation
**First attempt:** Claude scaled the walls uniformly — this caused door openings to scale up with the wall, making door frames taller than 2.1m.

**Fix prompt used:**
```
The door openings have stretched with the wall scaling.
The actual door frame objects are now too tall.
Please restore door heights to their original values
and adjust the surrounding wall geometry instead.
```

After correction, door proportions were restored correctly. ✅

### Step 4: Window Opening Preservation
Windows retained their dimensions correctly since Claude translated (not scaled) the wall top vertices. Minor gaps appeared above some windows, flagged by the agent automatically.

**Fix prompt used:**
```
You mentioned gaps appeared above 3 window openings.
Please fill those gaps with additional wall mesh geometry
matching the wall material.
```

Gaps filled. ✅

---

## Final Verification

Claude reported:
- Wall height confirmed at 4.0m (measured from a representative IfcWall bounding box)
- Roof slab Z-position increased by exactly 1.0 units
- 12 doors preserved at original heights
- 8 windows preserved at original sizes
- 3 window gaps filled

---

## Known Limitations

| Issue | Status |
|---|---|
| Non-IFC mesh objects not identified | ⚠️ Manual check needed |
| Complex curved walls | ⚠️ Agent may scale incorrectly — verify manually |
| Staircase height adjustment | ❌ Not handled — requires manual update |
| Interior partition walls | ✅ Handled correctly if tagged as IfcWall |

---

## Workflow Recommendation

Use this prompt as a **first pass** for simple rectangular building forms. For complex or curved geometry, verify the result visually and use manual corrections for any elements the agent could not handle.

**Always save a backup `.blend` file before running modification prompts.**

---

## Practical Use Cases

- Quick design iteration: "What if we raised the ceilings by 50cm?"
- Code compliance checking: ensure minimum ceiling heights are met
- Repurposing models: adapting residential models for commercial use (higher ceilings required)
- Client presentations: rapidly showing alternative spatial proportions
