#!/usr/bin/env python3
"""
Motivational Quotes Generator
Displays random motivational quotes for daily inspiration
"""

import random

QUOTES = [
    ("The secret of getting ahead is getting started.", "Mark Twain"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("The future depends on what you do today.", "Mahatma Gandhi"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Everything you've ever wanted is on the other side of fear.", "George Addair"),
    ("Success is the sum of small efforts repeated day in and day out.", "Robert Collier"),
    ("The expert in anything was once a beginner.", "Helen Hayes"),
    ("Don't let yesterday take up too much of today.", "Will Rogers"),
    ("You learn more from failure than from success. Don't let it stop you.", "Unknown"),
    ("It's not whether you get knocked down, it's whether you get up.", "Vince Lombardi"),
    ("Your limitation—it's only your imagination.", "Unknown"),
    ("Great things never come from comfort zones.", "Unknown"),
    ("Dream it. Wish it. Do it.", "Unknown"),
    ("Success doesn't just find you. You have to go out and get it.", "Unknown"),
    ("The harder you work for something, the greater you'll feel when you achieve it.", "Unknown"),
    ("Dream bigger. Do bigger.", "Unknown"),
    ("Don't stop when you're tired. Stop when you're done.", "Unknown"),
    ("Wake up with determination. Go to bed with satisfaction.", "Unknown"),
    ("Do something today that your future self will thank you for.", "Unknown"),
    ("Little things make big days.", "Unknown"),
    ("It's going to be hard, but hard does not mean impossible.", "Unknown"),
    ("Don't wait for opportunity. Create it.", "Unknown"),
    ("Sometimes we're tested not to show our weaknesses, but to discover our strengths.", "Unknown"),
    ("The key to success is to focus on goals, not obstacles.", "Unknown"),
    ("Dream it. Believe it. Build it.", "Unknown"),
    ("Consistency is the key to success.", "Unknown"),
    ("Small progress is still progress.", "Unknown"),
    ("The only impossible journey is the one you never begin.", "Tony Robbins"),
    ("Strive for progress, not perfection.", "Unknown"),
    ("Fall seven times, stand up eight.", "Japanese Proverb"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Learning to write programs stretches your mind.", "Donald Knuth"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
]

def get_random_quote():
    """Return a random motivational quote"""
    quote, author = random.choice(QUOTES)
    return f'"{quote}"\n   — {author}'

def main():
    print("💡 Daily Motivation")
    print("=" * 70)
    print()
    print(get_random_quote())
    print()
    print("=" * 70)
    print("💪 You've got this! Keep pushing forward!")

if __name__ == "__main__":
    main()
