# chatgpt-conversation
Have a conversation with ChatGPT using your voice, and have it talk back.

## Requirements (Linux)

- `espeak`
- `ffmpeg`

## Installation

Copy `config.json.example` to `config.json` and fill in the `session_token` value following the guide [here](https://github.com/acheong08/ChatGPT).

Also, install requirements:

`pip install -r requirements.txt`

## Usage

Run `chatgpt.py`, and wait 2 seconds before starting the conversation (this is to normalise ambient noise). You can keep responding to ChatGPT, it's all 1 "conversation". 

## Next steps

- [ ] Cut-off ChatGPT as it's speaking if you decide to interrupt.
- [ ] Silence PyAudio errors.
- [ ] Remove common, useless end phrases from ChatGPT ("I am an online LLM...", etc.).
- [ ] Make this as a web-app (better text-to-speech, universal):
  - [ ] Create interface
  - [ ] Create backend
  - [ ] Hook-up to a GPU so it's faster (in the speech->text bit). 
