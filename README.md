# 🤖 AI for Blender 2026 — Agentic MCP Agents vs Assistant Mode

> Using ChatGPT, Claude, Gemini & Local LLMs to supercharge your Blender workflow with Agentic AI and MCP (Model Context Protocol).

---

## 🧠 Overview

This repository documents experiments connecting **Large Language Models (LLMs)** to **Blender 4.5** using two distinct approaches:

| Approach | Description | Tools Used |
|---|---|---|
| **Assistant Mode** | LLM generates Python scripts; you paste & run manually | ChatGPT 5.1, Blender Text Editor |
| **Agentic Mode (MCP)** | LLM autonomously senses Blender state and makes changes | Claude + Blender MCP + Claude Code |

---

## 🗂️ Repository Structure

```
blender-ai-mcp/
├── assistant_mode/
│   ├── 01_random_cubes.py
│   ├── 02_non_overlapping_cubes.py
│   ├── 03_colored_cubes.py
│   ├── 04_physics_simulation.py
│   └── 05_bulk_material_update.py
├── agentic_mode/
│   ├── prompts/
│   │   ├── wall_e_robot.md
│   │   ├── solar_system.md
│   │   ├── donut_scene.md
│   │   ├── minecraft_stonehenge.md
│   │   ├── bim_shader_fix.md
│   │   ├── bim_report_notion.md
│   │   └── bim_wall_modification.md
│   └── setup/
│       ├── anything_llm_mcp_config.json
│       └── claude_code_mcp_config.json
├── local_llm_setup/
│   ├── ollama_setup.md
│   └── anything_llm_guide.md
└── README.md
```

---

## ⚡ Method 1: AI Assistant Mode (ChatGPT + Blender)

Use any LLM to **generate Python scripts** that run inside Blender's built-in Text Editor.

### How It Works

1. Describe your task to ChatGPT / Claude / Gemini in plain English
2. Copy the generated Python code
3. Open Blender → split screen → set panel to **Text Editor**
4. Paste the script and click **Run Script**

### Example Tasks Demonstrated

```python
# Example: Generate 5 non-overlapping random cubes with physics
# See: assistant_mode/04_physics_simulation.py
```

**Tasks covered in this project:**
- ✅ Generate N random cubes with random scale
- ✅ Prevent cube overlap using spatial checks
- ✅ Assign random materials/colors
- ✅ Set up physics simulation (rigid body fall)
- ✅ Bulk update material properties (e.g. metallic, roughness) across all objects

### Limitations
- You must manually copy-paste each script
- No feedback loop — the LLM cannot "see" what happened in Blender
- Requires clear, precise prompts for best results

---

## 🚀 Method 2: Agentic AI Mode (Blender MCP)

Connect LLMs **directly** to Blender using the **Model Context Protocol (MCP)** for a fully autonomous agent loop.

### What is MCP?

**MCP (Model Context Protocol)** is an open standard developed by **Anthropic** that allows LLMs to connect to external tools and applications via a standardized interface — without writing custom API integrations.

Think of it as a **USB standard for AI models**: plug your LLM into any compatible tool (Blender, Notion, GitHub, web browsers, etc.) and let it operate autonomously.

```
LLM (Claude / ChatGPT / Local)
         │
         ▼ JSON over MCP
    Blender MCP Plugin
         │
         ▼
  Blender Scene (sense + act)
```

### Setup: Claude Code + Blender MCP

**Prerequisites:**
- Blender 4.5+
- [Blender MCP Plugin](https://github.com/ahujasid/blender-mcp) installed
- Claude Code (Desktop) installed

**Steps:**
1. Install the Blender MCP add-on: `Edit → Preferences → Add-ons`
2. Open the MCP panel and click **Start Server**
3. ⚠️ **Critical:** Always open Blender and start the server BEFORE opening Claude Code
4. Open Claude Code — it will auto-detect the running MCP server
5. Start prompting Claude to interact with your Blender scene!

---

## 🎨 Agentic Demo Results

### 1. WALL-E Robot
**Prompt:** Provided a reference image of WALL-E; asked Claude to reconstruct it using primitive geometries.

**Result:** Claude autonomously created a recognizable WALL-E approximation using boxes, cylinders, and spheres — sensing the scene after each step.

### 2. Solar System Simulation
**Prompt:** Create a solar system with accurate planetary orbital movement.

**Result:** All planets created as spheres with materials, Saturn's rings added, animation keyframes set. Camera positioned for a cinematic render.

### 3. Donut Scene (Classic Blender Tutorial)
**Prompt:** Create a photorealistic donut with icing and sprinkles.

**Result:** Donut geometry, icing material, and scattered sprinkles created. Final rendered image produced via Cycles.

### 4. Minecraft-Style Stonehenge with UFOs
**Prompt:** Minecraft-style stone monoliths with UFOs hovering above and fire casting light in the center.

**Result:** Voxel-style monolithic structures, emissive fire material, area lights, and UFO objects assembled automatically.

### 5. BIM Shader Fix ⭐ (Most Practical Use Case)
**Prompt:** Import a BIM model (via Bonsai extension), fix all broken shaders, set up camera and lighting for a photorealistic render.

**Result:** 300+ shaders fixed in seconds. Photorealistic daytime AND nighttime renders produced with proper lighting.

### 6. BIM → Notion Report Generation
**Prompt:** Read all doors and windows from the BIM model in Blender and generate a scheduling report in Notion.

**Result:** Claude read IFC metadata from Blender objects and populated a structured Notion database with door/window counts, types, and dimensions — similar to Revit's scheduling feature.

### 7. BIM Wall Modification
**Prompt:** Raise ceiling height to 4m without deforming doors and windows.

**Result:** Roof slab moved, wall heights adjusted, door/window openings preserved. Minor corrections needed via follow-up prompts.

---

## 🏠 Method 3: Local LLMs via AnythingLLM + Ollama

Run the full agentic Blender workflow **100% locally** — no cloud, no API costs, full privacy.

### Stack

```
Ollama (local model runner)
    + Gemma 3 / Llama / Qwen etc.
         │
    AnythingLLM (UI + MCP bridge)
         │ JSON / MCP
    Blender MCP Plugin
         │
      Blender
```

### Setup Guide

1. Install [Ollama](https://ollama.com) and pull a model:
   ```bash
   ollama pull gemma3
   # Or for better results:
   ollama pull llama3.1:8b
   ```

2. Install [AnythingLLM Desktop](https://anythingllm.com)

3. In AnythingLLM: `Settings → Chat Settings` → select your Ollama model

4. Enable MCP: `Settings → Agent Skills → MCP Servers`

5. Add the Blender MCP config to:
   ```
   Windows: %APPDATA%\AnythingLLM Desktop\storage\plugins\anythingllm-mcp-servers.json
   Mac: ~/Library/Application Support/AnythingLLM Desktop/storage/plugins/
   ```

6. In chat, use `@agent` to activate the agent and communicate with Blender

### Model Recommendations by GPU VRAM

| VRAM | Recommended Model | Notes |
|---|---|---|
| 4 GB | Gemma 3 2B, Phi-3 Mini | Basic tasks, simple scene reading |
| 8 GB | Llama 3.1 8B, Gemma 3 9B | Good balance of speed and capability |
| 16 GB | Llama 3.1 70B (quantized), Qwen2.5 14B | Near GPT-4 quality locally |
| 24 GB+ | Llama 3.3 70B, Qwen2.5 32B | Excellent for complex BIM/modeling tasks |

> ⚠️ Always match your model size to your GPU VRAM. Running oversized models on CPU will be extremely slow.

### Using ChatGPT API via AnythingLLM (Pay-as-you-go)
Instead of local models, you can use OpenAI's API for better results:
1. Get an API key at [platform.openai.com](https://platform.openai.com)
2. In AnythingLLM: `Settings → Chat Settings → OpenAI`
3. Paste your key — you'll be charged per token used

**Estimated cost for Blender tasks:**
- Simple scene queries: ~$0.001–0.01
- Complex BIM analysis: ~$0.05–0.20
- Extended modeling sessions: ~$0.50–2.00

---

## 💡 Key Learnings & Tips

### Prompting Tips for Blender AI
1. **Be specific** — "Place 5 cubes" is worse than "Place 5 cubes at random X/Y positions with no overlap, each with a unique random color material"
2. **Iterate** — Agentic AI works best in a conversation; correct it when it makes mistakes
3. **Use the agent's vision** — Ask it to "take a screenshot and describe what you see" before making changes
4. **Break complex tasks** — Don't ask for a full scene in one prompt; build it step by step

### When to Use Which Approach

| Situation | Recommended Approach |
|---|---|
| Quick one-off automation | Assistant Mode (paste script) |
| Complex iterative modeling | Agentic Mode (Claude Code) |
| Privacy-sensitive projects | Local LLM via AnythingLLM |
| Heavy BIM/architecture work | Claude Code (best context handling) |
| Bulk material/shader updates | Assistant Mode (fast, reliable) |
| Report generation (to Notion, etc.) | Agentic Mode with multi-MCP |

---

## 🔗 Resources

- [Blender MCP Plugin](https://github.com/ahujasid/blender-mcp)
- [AnythingLLM](https://anythingllm.com)
- [Ollama](https://ollama.com)
- [Anthropic MCP Documentation](https://modelcontextprotocol.io)
- [Bonsai BIM Extension for Blender](https://bonsaibim.org)
- [OpenAI API Pricing](https://openai.com/pricing)

---

## 📄 License

MIT License — feel free to use, modify, and share these scripts and prompts.

---

## 🙌 Contributing

Found a cool use case? Improved one of the scripts? PRs are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-blender-experiment`
3. Commit your changes
4. Open a Pull Request with a description and screenshot/render

---

*If this helped you, please ⭐ the repo and share your Blender AI creations in the Issues tab!*
