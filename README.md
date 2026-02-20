# LLM Battleground: Adversarial Dialogue Simulator

The LLM Battleground is a functional framework designed to eliminate "Passive Opponent Syndrome" in AI interactions. By pitting Llama 3 (via Groq) against Gemini 2.0 (via Google GenAI), the script forces a high-stakes, zero-concession debate where agreement is programmatically prohibited.

## Why This Exists
Most LLMs are fine-tuned for helpfulness, which often leads to "sycophancy"—the tendency to agree with the user or an opponent to avoid conflict. This script breaks that cycle using **Forced Contrarianism**. It creates a "Digital Viva" where every logic gap is exploited, and every bias is exposed. For researchers and power users, this is a stress-test for model reasoning under pressure.

## Turning AI "Flaws" into Features
This tool is built for researchers who want to move past simple error mitigation. Instead of trying to fix bias and hallucination, this script weaponises them as **provocative frictions**. It forces the models to stop being "helpful" and start being difficult, which is essential for studying:

* **Active Resistance:** See how aggressive, biased AI prompts can actually empower users to push back and assert their own agency.
* **Creative Friction:** By programmatically blocking agreement, the script turns hallucinations into a springboard for reflection and new insights rather than just being "wrong".
* **Stress-Testing Assumptions:** The adversarial setup exposes how models default to ageist or systemic biases when they are forced to win an argument at all costs.
* **Hard Evidence:** The automated logging provides a raw, unedited transcript of these interactions, giving you the documentation needed for rigorous qualitative analysis.

## How It Works
The system uses a dual-provider architecture to ensure diverse rhetorical styles. While Llama maintains the primary argument, Gemini is injected with an adversarial prompt that overrides its default polite persona. 

### Key Technical Features:
* **Adversarial Injection:** Gemini is hard-coded to identify flaws and provide conflicting theories regardless of the topic.
* **Context Truncation:** The script manages memory by passing the System prompt and only the last four turns, keeping the focus sharp and preventing "context drift".
* **Dynamic Temperature Scaling:** To prevent repetitive "loops," the temperature (randomness) increases with each round.
* **Automated Logging:** Every exchange is captured in a timestamped `.txt` file, providing a permanent record of the intellectual conflict.

## Requirements
* `pip install google-genai groq`
* API Keys for Groq and Google GenAI.

## Quick Start
1. Add your keys to the `CONFIGURATION` section of the script.
2. Run: `python LLM_Battleground4.py`
3. Enter a controversial topic and watch the models fight for dominance.
4. Check the local directory for the `debate_log_...` file to review the final verdict.
