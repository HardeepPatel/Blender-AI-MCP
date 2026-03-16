# AnythingLLM Complete Guide for Blender MCP

A step-by-step guide to connecting **AnythingLLM** with Blender via MCP, supporting both local Ollama models and cloud APIs (OpenAI, Anthropic, Gemini).

---

## What is AnythingLLM?

AnythingLLM is an open-source desktop application that provides a unified interface for running and chatting with LLMs. It supports:
- **Local models** via Ollama (private, free, runs on your GPU)
- **Cloud APIs** (OpenAI, Anthropic Claude, Google Gemini, and more)
- **MCP (Model Context Protocol)** — connect your LLM to external tools like Blender
- **RAG (Retrieval-Augmented Generation)** — chat with your own documents

Download: [anythingllm.com/desktop](https://anythingllm.com/desktop)

---

## Installation

### Windows
1. Download the `.exe` installer from the website
2. Run and install (no admin required)
3. Launch from Start Menu or Desktop shortcut

### Mac
1. Download the `.dmg` file
2. Drag to Applications
3. On first launch, right-click → Open (bypass Gatekeeper)

### Linux
1. Download the `.AppImage`
2. `chmod +x AnythingLLM-*.AppImage`
3. `./AnythingLLM-*.AppImage`

---

## Connecting a Language Model

### Option A: Local Model via Ollama (Recommended for Privacy)

Prerequisites: [Ollama installed](ollama_setup.md) with at least one model pulled.

1. Open AnythingLLM → click the **Settings** gear icon
2. Go to **AI Providers → LLM**
3. Select **Ollama** from the provider dropdown
4. Base URL: `http://localhost:11434` (default)
5. Select your model from the dropdown
6. Click **Save**

### Option B: OpenAI API (GPT-4o, GPT-4.1, etc.)

1. Get your API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Open AnythingLLM → Settings → AI Providers → LLM
3. Select **OpenAI**
4. Paste your API key
5. Select model (e.g. `gpt-4o` or `gpt-4.1-nano` for cheaper usage)
6. Click **Save**

> **Cost tip:** `gpt-4.1-nano` is the most affordable option and works well for Blender tasks. Use `gpt-4o` for complex BIM or multi-step modeling work.

### Option C: Anthropic Claude API

1. Get your API key from [console.anthropic.com](https://console.anthropic.com)
2. Select **Anthropic** in AnythingLLM LLM settings
3. Paste key, select `claude-sonnet-4-6` for best balance of speed/quality
4. Click **Save**

### Option D: Google Gemini

1. Get your API key from [aistudio.google.com](https://aistudio.google.com)
2. Select **Google Gemini** in LLM settings
3. Paste key, select model
4. Click **Save**

---

## Configuring MCP for Blender

### Step 1: Find the MCP config file

**Windows:**
```
C:\Users\<YourName>\AppData\Roaming\AnythingLLM Desktop\storage\plugins\anythingllm-mcp-servers.json
```

Tip: Press `Win + R`, type `%APPDATA%\AnythingLLM Desktop\storage\plugins\` and press Enter.

**Mac:**
```
~/Library/Application Support/AnythingLLM Desktop/storage/plugins/anythingllm-mcp-servers.json
```

**Linux:**
```
~/.config/AnythingLLM Desktop/storage/plugins/anythingllm-mcp-servers.json
```

### Step 2: Edit the config

Open the file in any text editor (Notepad, VS Code, etc.) and replace the contents with:

```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

Save the file.

### Step 3: Verify in AnythingLLM

1. Restart AnythingLLM
2. Go to **Settings → Agent Skills → MCP Servers**
3. Wait a few seconds for detection
4. You should see `blender` listed — toggle it ON

---

## Using the Agent with Blender

### Critical: Startup Order

```
1. Open Blender
2. Install Blender MCP add-on (if not already done)
3. In Blender: Edit → Preferences → Add-ons → find "Blender MCP" → enable
4. Open the MCP panel (N key in 3D Viewport → MCP tab)
5. Click "Start MCP Server"
6. THEN open AnythingLLM
```

⚠️ If you open AnythingLLM before starting the Blender MCP server, the connection will fail. Always start Blender first.

### Activating Agent Mode in Chat

In the chat input, type `@agent` at the start of your message to activate the agent:

```
@agent What objects are currently in the Blender scene?

@agent Create 5 colored cubes arranged in a circle

@agent Fix all broken materials in the scene and set up a render
```

### Without @agent

Regular messages (without `@agent`) will just chat with the LLM — no Blender connection. Always use `@agent` for Blender tasks.

---

## Model-Specific Tips

### Ollama / Small Local Models (Gemma, Phi, smaller Llama)
- Keep prompts shorter and more explicit
- Break complex tasks into individual steps
- Use `@agent what did you just do?` to verify actions before continuing
- Avoid asking for too many things in one prompt

### GPT-4o / Claude Sonnet / Larger Models
- Handle complex multi-step instructions well
- Can reason about scene state and plan approaches
- Better for BIM work, shader analysis, and architecture tasks

### For Blender-Specific Tasks
- Always specify object names when possible
- Ask the agent to "report what it sees" before making changes
- Request confirmation before destructive operations (deleting objects, clearing scenes)

---

## Troubleshooting

| Problem | Solution |
|---|---|
| MCP server not detected | Restart AnythingLLM after saving config file |
| "Connection refused" to Blender | Start Blender MCP server first, then reopen AnythingLLM |
| Agent not responding to Blender commands | Ensure you typed `@agent` at start of message |
| Model too slow | Switch to a smaller model or use API instead of local |
| Ollama model not in dropdown | Run `ollama pull <modelname>` in terminal first |
| JSON config not loading | Validate your JSON at jsonlint.com — syntax errors prevent loading |

---

## Adding Multiple MCP Servers

You can connect Blender AND other services simultaneously:

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
        "NOTION_API_KEY": "your_token_here"
      }
    },
    "filesystem": {
      "command": "uvx",
      "args": ["mcp-server-filesystem", "--root", "C:/Users/YourName/Documents"]
    }
  }
}
```

This enables the agent to work with Blender, write to Notion, and access local files all in one session.

---

## Privacy Considerations

| Setup | Data leaves your computer? |
|---|---|
| Ollama local model | ❌ No — fully private |
| AnythingLLM + Ollama | ❌ No — fully private |
| OpenAI API | ✅ Yes — sent to OpenAI servers |
| Anthropic API | ✅ Yes — sent to Anthropic servers |
| Cloud APIs via AnythingLLM | ✅ Yes — prompt + context sent to provider |

For client work or sensitive BIM files, use the local Ollama setup.
