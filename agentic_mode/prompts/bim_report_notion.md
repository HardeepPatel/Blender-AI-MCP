# Prompt: BIM Report Generation → Notion

**Model used:** Claude (via Claude Code + Blender MCP + Notion MCP)  
**Task type:** Agentic — multi-MCP workflow (Blender + Notion simultaneously)  
**Blender version:** 4.5  
**BIM Tool:** Bonsai extension (IFC import)

---

## The Goal

Extract structured scheduling data (doors and windows) from a BIM model open in Blender and automatically populate a Notion database — replicating a workflow typically done in Revit.

---

## Setup Required

This task requires **two MCP servers active simultaneously**:

1. **Blender MCP** — to read IFC object metadata from the scene
2. **Notion MCP** — to write structured data to a Notion database

Both must be configured in your Claude Code or AnythingLLM MCP settings before running this prompt.

---

## Main Prompt

```
I have a BIM model open in Blender, imported via the Bonsai IFC extension.
The model contains architectural elements including doors and windows
with IFC metadata attached.

Please do the following:

STEP 1 — EXTRACT FROM BLENDER:
- Scan all objects in the Blender scene
- Identify all IFC Door elements (look for objects with IFC class
  "IfcDoor" in their custom properties or name patterns)
- Identify all IFC Window elements ("IfcWindow")
- For each element, extract:
  * Element ID / IFC GUID
  * Type name (e.g. "Single-Flush Door", "Fixed Window")
  * Width and Height dimensions (from IFC properties if available)
  * Level / Storey it belongs to
  * Any fire rating or acoustic rating properties if present

STEP 2 — CREATE NOTION DATABASES:
- In my Notion workspace, create two new databases:
  * "Door Schedule" with columns: ID, Type, Width, Height, Level, Fire Rating, Notes
  * "Window Schedule" with columns: ID, Type, Width, Height, Level, Glazing Type, Notes

STEP 3 — POPULATE THE DATABASES:
- Add each door and window as a row in the respective database
- Format dimensions in millimeters
- Leave Notes column empty for manual entry later

STEP 4 — SUMMARY PAGE:
- Create a Notion page called "BIM Schedules Summary" that includes:
  * Total door count (by type)
  * Total window count (by type)
  * A breakdown by floor/level
  * Link to both schedule databases
```

---

## Results

### Doors Extracted
Claude successfully identified and catalogued **all IFC doors** in the model, including:
- Type classification (single-flush, double, fire door variants)
- Dimensional data pulled from IFC property sets
- Floor level assignment

### Windows Extracted
Windows were similarly extracted with:
- Glazing type metadata where available
- Width/height from bounding box when IFC properties were missing
- Level assignment

### Notion Output
Both databases were created and populated automatically. The summary page included:
- Counts per type (e.g. "12x Single Flush Door, 3x Double Door")
- Floor-by-floor breakdown table
- Direct links to both schedule databases

---

## Comparison: AI vs Revit Scheduling

| Feature | Revit | Blender + Claude MCP |
|---|---|---|
| Schedule generation | Built-in, automated | ✅ Automated via agent |
| Custom columns | Template-based | ✅ Flexible, prompt-driven |
| Export destination | Excel / PDF | ✅ Directly to Notion |
| IFC property reading | Native | ✅ Via Bonsai metadata |
| Non-BIM objects included | No | ⚠️ Agent may include non-IFC objects — add filter prompt |

---

## Tips for BIM Scheduling

1. **Filter explicitly** — prompt Claude to "only include objects whose IFC class is IfcDoor, not all objects with 'door' in the name"
2. **Verify counts** — ask Claude to report the count before writing to Notion so you can cross-check
3. **Dimension fallback** — if IFC property sets are missing, ask Claude to measure bounding box dimensions as a fallback
4. **Multi-storey models** — specify the IFC storey property name ("IfcBuildingStorey") to ensure correct floor assignment

---

## Notion MCP Config

Add to your MCP config alongside the Blender server:

```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    },
    "notion": {
      "command": "uvx",
      "args": ["notion-mcp"],
      "env": {
        "NOTION_API_KEY": "your_notion_integration_token_here"
      }
    }
  }
}
```

Get your Notion integration token at: https://www.notion.so/my-integrations
