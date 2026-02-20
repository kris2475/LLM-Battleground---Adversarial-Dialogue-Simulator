# LLM Battleground: Adversarial Dialogue Simulator

A functional framework designed to eliminate "Passive Opponent" syndrome in Large Language Models. This tool forces two AI agents into a high-stakes, zero-concession debate, ensuring a continuous back-and-forth where agreement is programmatically prohibited.

## Evolution: Breaking the "Digital Hall of Mirrors"

Early versions of this script faced a significant technical hurdle: the **Repetition Attractor**. By round 6 or 7, the models would hit a "rhetorical cul-de-sac," repeating identical arguments and sentence structures until the logic stalled entirely. In an academic environment, this would be failed for "circular reasoning".

To solve this, the script evolved to include several "Noise Injection" strategies:

* **Forced Contrarianism:** The opponent agent is injected with a specific adversarial prompt that requires it to find flaws or conflicting theories in every turn.
* **Memory Management:** The script uses **Context Truncation**, providing only the system instructions and the last few turns to the AI to prevent it from mimicking old sentence structures.
* **Entropy (Randomness):** We implemented **Temperature Jitter**, which increases the randomness of word choices as the rounds progress to keep the AI from picking the same predictable rebuttals.
* **Penalties:** The framework uses **Frequency and Presence Penalties** to mathematically forbid the AI from repeating words it has already used, forcing the introduction of new topics.

## How LLMs Work: A Layman’s Guide

Large Language Models (LLMs) are essentially highly advanced statistical guessing machines. To understand why they get "stuck" without adversarial controls, you have to look at the underlying mechanics.

### 1. The Statistical Guessing Game
LLMs generate text one word (or "token") at a time. For every new word, the model calculates a probability distribution across its entire vocabulary.

* **The Path:** The model calculates probabilities for the next word and generally picks the highest-weighted option.
* **Self-Conditioning:** Once a model uses a specific phrase, those words are weighted heavily in its immediate memory.
* **Self-Attention:** The model's **Self-Attention mechanism** looks back at its own successful prose and concludes that the most "optimal" way to continue is to repeat that same structural template.

### 2. The Mirroring Effect
Without external intervention, models suffer from a loss of "Semantic Drift". In a standard setting, LLMs have no internal drive other than to satisfy the prompt.

* **Synchronization:** If Model A is aggressive, Model B "attends" to that style and mimics it. Model A then mimics that mimicry.
* **The Result:** They effectively synchronise their internal logic, becoming like two mirrors reflecting the same beam of light back and forth until the signal becomes a single, unchanging frequency.

### 3. The Resolution Problem (Quantisation)
To run faster, many modern models use **Quantisation** (8-bit or 4-bit weights), which reduces the "resolution" of the model's vocabulary. This makes them even more likely to choose the "safest," most common tokens rather than searching for creative words that might break a loop.

This script acts as a "microphone mover" in a PA system. By injecting noise and forcing contrarianism, it breaks the feedback loop before the logic "screeches" to a halt.

## Technical Overview

* **Primary Agent:** Llama 3.1 (via Groq).
* **Opponent Agent:** Gemini 2.0 Flash (via Google).
* **Logging:** Automated timestamped transcripts saved to local .txt files.
* **Safety Bypass:** Uses adversarial roleplay prompting to ensure models engage in difficult topics.
