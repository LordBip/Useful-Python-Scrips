import csv
import random
import string

# Define the elements
elements = ['wind', 'water', 'ice', 'fire', 'earth', 'dark', 'light', 'mystic']

# Function to calculate the percentage difference between two numbers
def percentage_difference(a, b):
    return abs((a - b) / ((a + b) / 2)) * 100

# Function to generate a card
def generate_card():
    cost = random.randint(1, 10)
    total_points = cost * 1000
    health = random.randint(0, total_points // 10) * 10
    power = total_points - health
    element = random.choice(elements)

    # Calculate the percentage difference between health and power
    diff = percentage_difference(health, power)

    # Assign rarity based on the percentage difference
    if diff <= 20:
        rarity = 'Common'
    elif diff <= 60:
        rarity = 'Rare'
    elif diff <= 85:
        rarity = 'Super Rare'
    else:
        rarity = 'Legend'

    # Generate a unique name for the card
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(1)) + str(power) + str(cost) + str(health)

    return [name, cost, health, power, element, rarity]

# Generate 100 unique cards and write them to a CSV file
cards = set()
while len(cards) < 100:
    card = tuple(generate_card())
    cards.add(card)

with open('cards.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Cost', 'Health', 'Power', 'Element', 'Rarity'])  # Header row
    for card in cards:
        writer.writerow(card)