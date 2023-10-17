import random

adjectives = ['Silly', 'Goofy', 'Wacky', 'Zany', 'Whimsical', 'Kooky', 'Bizarre', 'Absurd', 'Quirky', 'Crazy']
nouns = ['Banana', 'Penguin', 'Toaster', 'Giraffe', 'Pickle', 'Noodle', 'Walrus', 'Kangaroo', 'Llama', 'Octopus']

def generate_funny_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'{adjective} {noun}'

if __name__ == '__main__':
    print(generate_funny_name())
