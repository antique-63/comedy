import random

class ComedyScriptGenerator:
    def __init__(self):
        self.setup_lines = [
            "Why did the chicken cross the road?",
            "I told my wife she was drawing her eyebrows too high...",
            "I’m on a whiskey diet. I’ve lost three days already.",
            "I used to play piano by ear, but now I just use my fingers.",
            "I asked the gym instructor if he could teach me to do the splits. He replied, 'How flexible are you?'"
        ]

        self.punchlines = [
            "To get to the other side.",
            "She looked surprised.",
            "But I’ve been sober ever since.",
            "I just can't find the key.",
            "I can’t even touch my toes."
        ]
    
    def generate_joke(self):
        setup = random.choice(self.setup_lines)
        punchline = random.choice(self.punchlines)
        joke = f"{setup} {punchline}"
        return joke
    
    def generate_script(self):
        num_jokes = random.randint(3, 5)
        script = []
        for _ in range(num_jokes):
            script.append(self.generate_joke())
        return "\n".join(script)

    def run(self):
        print("Welcome to the Stand-Up Comedy Script Generator!")
        print("\nGenerating a random comedy script...\n")
        print(self.generate_script())

# Run the Comedy Script Generator
if __name__ == "__main__":
    generator = ComedyScriptGenerator()
    generator.run()
