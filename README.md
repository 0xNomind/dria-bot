# HOW TO RUN

1. Clone repository
```
git clone git@github.com:0xNomind/dria-bot.git
cd dria-bot
```

2. Permission
```
chmod +x run.sh
```

3. Edit Model on function **create_jsonl_entry**
```
nano generate_prompt.py
```

Select One Model From This List Model 
```
Claude 3.7 Sonnet: 'claude-3.7-sonnet'
Claude 3.5 Sonnet: 'claude-3.5-sonnet'
Gemini 2.5 Pro Experimental: 'gemini-2.5-pro-exp'
Gemini 2.0 Flash: 'gemini-2.0-flash'
gemma3 4b: 'gemma3:4b'
gemma3 12b: 'gemma3:12b'
gemma3 27b: 'gemma3:27b'
GPT-4o-mini: 'gpt-4o-mini'
GPT-4o: 'gpt-4o'
Llama 3.3 70B Instruct: 'llama3.3:70b-instruct-q4_K_M'
Llama 3.1 8B Instruct: 'llama3.1:8b-instruct-q4_K_M'
Llama 3.2 1B Instruct: 'llama3.2:1b-instruct-q4_K_M'
Mistral Nemo 12B: 'mixtral-nemo:12b'
```

3. Edit API KEY
```
nano send_dria.py
```

find your api key here : https://dria.co/batch-inference

4. Run
```
screen -r dria-bot
./run.sh
```
