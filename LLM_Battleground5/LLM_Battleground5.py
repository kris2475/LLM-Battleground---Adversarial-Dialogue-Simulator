"""
================================================================================
PROJECT:        THE LLM BATTLEGROUND - ADVERSARIAL DIALOGUE SIMULATOR
VERSION:        4.1.0 (2026 LOGGING ENABLED)
AUTHOR:         KRIS SEUNARINE
DATE:           FEBRUARY 20, 2026
LOCATION:       SKETTY, WALES, UK
--------------------------------------------------------------------------------
FUNCTIONAL OVERVIEW:
    - AUTOMATED LOGGING: Every turn and the final verdict are saved to a 
      timestamped .txt file in the local directory.
    - DUAL-AGENT DEBATE: Orchestrates a "Viva-style" conflict between Llama 
      (via Groq) and Gemini (via Google GenAI).
    - CONTRARIAN LOGIC: Gemini is hard-coded to act as a rival academic, 
      systematically attacking the opponent's premises.
    - REPUTATION STAKES: Models are prompted to simulate a 1995 Honours 
      Viva environment—concise, sharp, and conceding nothing.

USAGE:
    Run the script, enter a controversial topic, and review the generated 
    log file for a permanent record of the simulation.
================================================================================
"""

import os
import time
import random
import datetime
from google import genai
from groq import Groq

# --- CONFIGURATION ---
GEMINI_API_KEY = ""
GROQ_API_KEY = ""

# --- MODEL DEFINITIONS ---
MODEL_PRIMARY  = "llama-3.1-8b-instant" 
MODEL_OPPONENT = "llama-3.1-8b-instant" 
MODEL_GEMINI   = "gemini-2.0-flash" 

gemini_client = genai.Client(api_key=GEMINI_API_KEY)
groq_client = Groq(api_key=GROQ_API_KEY)

def get_llama_response(history, turn, model):
    """Fetches response from Groq with frequency penalties to break loops."""
    context = [history[0]] + history[-4:]
    dynamic_temp = min(0.85 + (turn * 0.05), 1.2)
    
    response = groq_client.chat.completions.create(
        model=model,
        messages=context,
        temperature=dynamic_temp,
        timeout=30.0,
        presence_penalty=0.8,
        frequency_penalty=0.8
    )
    return response.choices[0].message.content

def get_gemini_response(history):
    """Engages Gemini with a forced adversarial injection."""
    context_text = "\n".join([f"{m['role']}: {m['content']}" for m in history[-4:]])
    
    adversarial_prompt = (
        f"You are a rival academic who completely disagrees with the previous logic. "
        f"You must find a flaw, expose a bias, or provide a conflicting theory. "
        f"DO NOT AGREE. BE ASSERTIVE. Context: {context_text}"
    )
    
    try:
        response = gemini_client.models.generate_content(
            model=MODEL_GEMINI, 
            contents=adversarial_prompt
        )
        return response.text
    except Exception:
        context = history + [{"role": "system", "content": "ADVERSARIAL: You are the opponent. Attack their last point!"}]
        return get_llama_response(context, 1, MODEL_OPPONENT)

def battle_of_the_ai(initial_question, max_turns=6):
    # Setup for file logging
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = "".join(x for x in initial_question[:20] if x.isalnum() or x in "._- ")
    filename = f"debate_log_{timestamp}_{safe_topic}.txt"

    print(f"\n--- ⚡ THE ADVERSARIAL DEBATE: {initial_question} ⚡ ---")
    
    system_instruction = (
        "You are an elite academic in a 1995 Honours Viva. "
        "Your reputation depends on winning this argument. "
        "Find logical fallacies, demand evidence, and never concede. "
        "Keep your responses concise but sharp."
    )

    history = [{"role": "system", "content": system_instruction}]
    history.append({"role": "user", "content": initial_question})

    with open(filename, "w", encoding="utf-8") as log_file:
        log_file.write(f"DEBATE LOG: {initial_question}\n")
        log_file.write(f"TIMESTAMP: {timestamp}\n")
        log_file.write("-" * 60 + "\n")

        for turn in range(1, max_turns + 1):
            print(f"\n--- ROUND {turn} ---")
            log_file.write(f"\n[ROUND {turn}]\n")
            
            # --- LLAMA TURN ---
            llama_reply = get_llama_response(history, turn, MODEL_PRIMARY)
            print(f"\033[94mLLAMA:\033[0m {llama_reply[:300]}...")
            log_file.write(f"LLAMA: {llama_reply}\n")
            history.append({"role": "assistant", "content": llama_reply})
            
            time.sleep(1.5)

            # --- GEMINI TURN ---
            gemini_reply = get_gemini_response(history)
            print(f"\033[92mGEMINI:\033[0m {gemini_reply[:300]}...")
            log_file.write(f"GEMINI: {gemini_reply}\n")
            history.append({"role": "user", "content": gemini_reply})

        # --- FINAL SUMMARY ---
        print("\n" + "="*50)
        print("📢 MODERATOR'S FINAL SUMMARY")
        print("="*50)
        
        summary_request = [
            {"role": "system", "content": "You are a neutral judge. Summarize the conflict points and declare a winner based on rhetorical strength."},
            {"role": "user", "content": f"Analyze this transcript: {history[-4:]}"}
        ]
        
        summary = groq_client.chat.completions.create(
            model=MODEL_PRIMARY,
            messages=summary_request,
            temperature=0.3
        ).choices[0].message.content
        
        print(summary)
        log_file.write("\n" + "="*50 + "\n")
        log_file.write("FINAL JUDICIAL SUMMARY\n")
        log_file.write("="*50 + "\n")
        log_file.write(summary)

    print(f"\n[SIMULATION COMPLETE - TRANSCRIPT SAVED TO {filename}]")

if __name__ == "__main__":
    user_input = input("Enter debate topic: ")

    battle_of_the_ai(user_input)
