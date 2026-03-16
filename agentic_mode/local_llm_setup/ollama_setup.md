# Setting Up Ollama for Local Blender AI

Run powerful LLMs **locally on your own machine** — no cloud, no API costs, complete privacy.

---

## Prerequisites

- Windows 10/11, macOS 12+, or Linux
- NVIDIA or AMD GPU with 4 GB+ VRAM (recommended) OR Apple Silicon Mac
- 16 GB+ system RAM recommended

---

## Step 1: Install Ollama

Download from [ollama.com](https://ollama.com) and install.

Verify the installation:
```bash
ollama --version
```

---

## Step 2: Download a Model

```bash
# Fast, good for basic tasks (4 GB VRAM)
ollama pull gemma3:4b

# Better quality, recommended (8 GB VRAM)
ollama pull llama3.1:8b

# High quality, needs 16 GB VRAM
ollama pull llama3.1:70b-instruct-q4_K_M
```

Test it works:
```bash
ollama run llama3.1:8b "Describe a Blender scene with 3 cubes"
```

---

## Step 3: Install AnythingLLM Desktop

Download from [anythingllm.com](https://anythingllm.com/desktop)

---

## Step 4: Connect AnythingLLM to Ollama

1. Open AnythingLLM
2. Go to **Settings → Chat Settings**
3. Set LLM Provider to **Ollama**
4. Base URL: `http://localhost:11434`
5. Select your downloaded model
6. Click Save

---

## Step 5: Configure MCP for Blender

Find the AnythingLLM MCP config file:

**Windows:**
```
%APPDATA%\AnythingLLM Desktop\storage\plugins\anythingllm-mcp-servers.json
```

**Mac:**
```
~/Library/Application Support/AnythingLLM Desktop/storage/plugins/anythingllm-mcp-servers.json
```

Paste the contents of `../agentic_mode/setup/anything_llm_mcp_config.json` into this file.

---

## Step 6: Enable MCP in AnythingLLM

1. Go to **Settings → Agent Skills**
2. Scroll to **MCP Servers**
3. Wait for it to load — you should see `blender` listed
4. Toggle it ON

---

## Step 7: Use the Agent

1. **Start Blender first** and enable the MCP server from the add-on panel
2. Open AnythingLLM
3. In the chat, type `@agent` to activate agent mode
4. Try: `@agent What objects are in the current Blender scene?`

---

## Model Performance Guide

| GPU VRAM | Model | Blender Tasks | Speed |
|---|---|---|---|
| 4 GB | gemma3:4b | Scene reading, simple scripts | Fast |
| 8 GB | llama3.1:8b | Most tasks, good reasoning | Good |
| 12 GB | llama3.2:11b-vision | + image understanding | Good |
| 16 GB | llama3.1:70b (Q4) | Complex BIM, detailed prompts | Moderate |
| 24 GB | qwen2.5:32b | Near GPT-4 quality | Moderate |

> **Rule of thumb:** Model size in GB ≈ VRAM needed. A 8B model at Q4 quantization needs ~5 GB VRAM.

---

## Troubleshooting

**Ollama not responding:**
```bash
# Restart the Ollama service
ollama serve
```

**Model too slow:**
- Check GPU usage with `nvidia-smi` (NVIDIA) or Activity Monitor (Mac)
- If CPU usage is high, the model is too large for your VRAM — try a smaller model

**MCP not connecting to Blender:**
- Ensure Blender MCP server is started BEFORE AnythingLLM loads
- Check Blender's system console for error messages
- Verify the MCP config JSON is valid (use a JSON validator)

**AnythingLLM can't find Blender MCP:**
- Restart AnythingLLM after editing the config file
- Make sure you saved the JSON with valid syntax
