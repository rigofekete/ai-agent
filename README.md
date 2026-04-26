# ai_agent

ai_agent is an agentic Python tool with a Textual-based TUI that uses Google’s Gemini API and function calling to analyze Python repositories, detect bugs, and propose or apply fixes.

## Tools and Dependencies

- Google Gemini API
- Textual (TUI framework)

## Requirements

- Linux
- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Google Gemini API key

## Install

```bash
git clone https://github.com/rigofekete/ai_agent
cd ai_agent
uv sync
```

## Environment Setup

### Get a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your environment

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the TUI using uv:

```bash
uv run python tui.py
```

Or use the CLI directly:

```bash
uv run python main.py "fix the bug in main.py" [--verbose]
```

### Alternative: Using Virtual Environment

If you prefer not to use `uv run`, you can activate the virtual environment directly:

```bash
source .venv/bin/activate
python tui.py
```

Or for the CLI:

```bash
source .venv/bin/activate
python main.py "fix the bug in main.py" [--verbose]
```

## Example

The project includes a sandbox "calculator" app to test the agent:

```bash
cd calculator
python ../tui.py
```

Then ask the agent to fix bugs or add features to the calculator app.

## Demo

<video src="https://github.com/user-attachments/assets/42ea0662-f31b-4863-8337-b34abf6afd05" width="600" controls></video>

## Screenshots

<img width="1921" height="1022" alt="Image" src="https://github.com/user-attachments/assets/38d43bd4-b5ee-43b1-8248-336b30a24dfd" />

## Architecture

The agent uses a modular tool interface:

- `call_function.py` – dispatches function calls to the appropriate handler
- `functions/` – directory containing tool implementations
- `prompt.py` – system prompt that defines the agent's behavior
- `tui.py` – Textual-based terminal user interface

## Customizing the Agent Behavior

The `prompt.py` file contains the system prompt that defines how the agent thinks and behaves. It comes pre-configured with instructions for:

- Reading and writing files
- Running Python code
- Analyzing project structure
- Iterating until errors are resolved

You can tweak the prompt to change the agent's behavior, priorities, or add new instructions. For example, you might want the agent to:

- Prioritize certain coding style conventions
- Always run tests before finishing
- Use specific error handling patterns
- Follow your project's conventions

Edit `prompt.py` to customize the agent to your needs.

## Extensible Design

The agent uses a modular tool interface with these built-in functions available via Gemini function calling:

- `get_files_info` – List files in working directory
- `get_file_content` – Read file contents
- `write_file` – Write/overwrite a file
- `run_python_file` – Run a Python file

Add new tools by:

1. Creating a new function in `functions/` (e.g., `functions/new_tool.py`)
2. Exporting `schema_new_tool` and `new_tool`
3. Registering in `call_function.py`
4. Updating `available_functions` and `functions_dict`
