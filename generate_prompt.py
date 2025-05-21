import random
import uuid
import json

def generate_one_piece_prompt(prompt_id):
    """Generates a unique One Piece prompt."""
    characters = [
        "Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe",
        "Shanks", "Blackbeard", "Akainu", "Aokiji", "Kizaru", "Garp", "Sengoku", "Roger", "Whitebeard",
        "Kaido", "Big Mom", "Buggy", "Crocodile", "Doflamingo", "Mihawk", "Boa Hancock", "Law", "Kid",
        "Yamato", "Ace", "Sabo", "Vivi", "Rebecca", "Oden", "Toki", "Momo", "Hiyori"
    ]
    locations = [
        "East Blue", "Grand Line", "New World", "Wano Country", "Whole Cake Island", "Dressrosa",
        "Alabasta", "Water 7", "Enies Lobby", "Marineford", "Fish-Man Island", "Skypiea", "Loguetown",
        "Reverse Mountain", "Red Line", "Mary Geoise", "Impel Down", "Punk Hazard", "Zou"
    ]
    devil_fruits = [
        "Gomu Gomu no Mi", "Mera Mera no Mi", "Hito Hito no Mi (Model: Human)", "Hana Hana no Mi",
        "Suke Suke no Mi", "Tori Tori no Mi (Model: Phoenix)", "Yami Yami no Mi", "Gura Gura no Mi",
        "Uo Uo no Mi (Model: Seiryu)", "Soru Soru no Mi", "Ito Ito no Mi", "Ope Ope no Mi",
        "Mochi Mochi no Mi", "Bara Bara no Mi", "Suna Suna no Mi", "Doku Doku no Mi", "Horo Horo no Mi",
        "Nikyu Nikyu no Mi", "Kage Kage no Mi", "Pika Pika no Mi", "Hie Hie no Mi", "Magu Magu no Mi"
    ]
    themes = [
        "the meaning of freedom", "the power of friendship", "the injustice of the World Government",
        "the legacy of the past", "the pursuit of dreams", "overcoming adversity", "the nature of power",
        "the importance of family", "the cost of war", "the exploration of the unknown"
    ]
    events = [
        "the Summit War of Marineford", "the Ohara incident", "the God Valley incident",
        "Luffy's encounter with Shanks", "the formation of the Straw Hat Pirates",
        "the fall of Dressrosa", "the raid on Onigashima", "the escape from Whole Cake Island"
    ]
    relationships = [
        "Luffy and his crew", "the bond between the Straw Hats", "the rivalry between Luffy and Blackbeard",
        "the connection between Roger and Rayleigh", "the dynamic between siblings (Ace/Sabo/Luffy)",
        "the complex relationship between the World Government and the revolutionaries"
    ]
    what_ifs = [
        f"What if {random.choice(characters)} ate a different Devil Fruit?",
        f"What if {random.choice(characters)} joined a different pirate crew?",
        f"What if a major event like {random.choice(events)} had a different outcome?",
        f"What if {random.choice(characters)} met {random.choice(characters)} much earlier?",
        f"What if {random.choice(locations)} was ruled by a different power?"
    ]
    creative_starters = [
        "Write a scene where",
        "Imagine a new character with",
        "Continue the story after",
        "Describe the daily life of",
        "Explore the history of"
    ]

    prompt_type = random.choice(["character_focus", "plot_point", "world_building", "what_if", "creative_start"])

    if prompt_type == "character_focus":
        char = random.choice(characters)
        focus_area = random.choice(["past", "motivations", "hidden abilities", "a surprising encounter", "their greatest fear"])
        return f"Focus on {char}: Explore their {focus_area} in detail within the world of One Piece."
    elif prompt_type == "plot_point":
        event = random.choice(events)
        angle = random.choice(["a different perspective on", "the long-term consequences of", "a secret leading up to", "an alternative scenario during"])
        return f"Consider the event: {event}. Explore {angle} this pivotal moment in One Piece history."
    elif prompt_type == "world_building":
        location = random.choice(locations)
        aspect = random.choice(["the unique culture of", "the political structure of", "the hidden dangers within", "the history and legends of", "a day in the life of an ordinary citizen in"])
        return f"World-building prompt: Describe {aspect} {location} in the One Piece world."
    elif prompt_type == "what_if":
        return random.choice(what_ifs)
    elif prompt_type == "creative_start":
        starter = random.choice(creative_starters)
        subject = random.choice(characters + locations + devil_fruits + themes)
        detail = ""
        if starter.startswith("Write a scene where"):
            detail = f" {random.choice(characters)} encounters a mysterious object in {random.choice(locations)}."
        elif starter.startswith("Imagine a new character with"):
            detail = f" the {random.choice(devil_fruits)} and a connection to {random.choice(characters)}."
        elif starter.startswith("Continue the story after"):
            detail = f" the events of {random.choice(events)}, focusing on {random.choice(themes)}."
        elif starter.startswith("Describe the daily life of"):
            detail = f" a Marine soldier stationed in {random.choice(locations)}."
        elif starter.startswith("Explore the history of"):
            detail = f" the lost kingdom and its connection to the {random.choice(devil_fruits)}."
        return f"{starter} {subject}{detail}"

def create_jsonl_entry(prompt):
    """Creates a JSONL entry with the specified format."""
    entry = {
        "custom_id": str(uuid.uuid4()),
        "type": "completions",
        "version": "v1",
        "body": {
            "model": "gemini-2.0-flash",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
    }
    return entry

def generate_and_write_prompts(num_prompts=10000, filename="one_piece_prompts.jsonl"):
    """Generates and writes a specified number of unique One Piece prompts to a JSONL file."""
    prompts = set()
    print(f"Generating {num_prompts} unique One Piece prompts...")
    while len(prompts) < num_prompts:
        prompt_id = len(prompts) + 1
        prompts.add(generate_one_piece_prompt(prompt_id))
        if len(prompts) % 1000 == 0:
            print(f"Generated {len(prompts)} prompts...")

    print("Writing prompts to JSONL file...")
    with open(filename, 'w') as f:
        for prompt in prompts:
            entry = create_jsonl_entry(prompt)
            json_record = json.dumps(entry)
            f.write(json_record + '\n')
    print(f"Successfully generated and wrote {len(prompts)} unique One Piece prompts to '{filename}'.")

if __name__ == "__main__":
    generate_and_write_prompts(num_prompts=100000)