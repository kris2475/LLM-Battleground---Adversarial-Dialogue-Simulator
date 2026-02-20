# LLM Battleground: Adversarial Dialogue Simulator

A functional framework designed to eliminate passive AI behavior through forced contrarianism. The script orchestrates a high-stakes, zero-concession debate between Llama 3 and Gemini 2.0, archiving every round and the final judicial verdict into a local text log for a permanent record of the conflict.

## Core Features
* **Forced Contrarianism:** Prevents agreement bugs by injecting adversarial prompts into the opponent agent.
* **Automated Logging:** Saves timestamped transcripts of every debate to `.txt` files.
* **Dual-Provider Architecture:** Leverages Groq (Llama) and Google (Gemini) for diverse rhetorical styles.
* **Dynamic Temperature:** Increases randomness over turns to break repetitive loops.

## Requirements
* `pip install google-genai groq`
* Valid API keys for both Google GenAI and Groq.

## Usage
1. Configure your API keys in the `CONFIGURATION` section.
2. Run the script: `python LLM_Battleground4.py`
3. Enter a debate topic when prompted.
4. Review the generated `.txt` log for the full transcript and winner summary.
