import json
import random
from datetime import datetime

# Load reminders from a JSON file
def load_reminders():
    try:
        with open("reminders.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save reminders back to file
def save_reminders(reminders):
    with open("reminders.json", "w", encoding="utf-8") as file:
        json.dump(reminders, file, indent=4, ensure_ascii=False)

# Display a random reminder
def show_random(reminders):
    if not reminders:
        print("No reminders found. Please add one first.")
        return
    reminder = random.choice(reminders)
    print("\n🌙 DAILY REMINDER 🌙")
    print(f"“{reminder['text']}”")
    print(f"— {reminder['source']}")
    print(f"⏰ {datetime.now().strftime('%A, %B %d, %Y')}\n")

# Add a new reminder
def add_reminder(reminders):
    text = input("Enter your reminder or verse: ").strip()
    source = input("Enter the source (e.g., Qur'an 2:286 or Hadith): ").strip()
    reminders.append({"text": text, "source": source})
    save_reminders(reminders)
    print("✅ Reminder added successfully!\n")

# Main menu
def main():
    reminders = load_reminders()

    while True:
        print("=== DAILY DIVINE REMINDER ===")
        print("1. Show a random reminder")
        print("2. Add a new reminder")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_random(reminders)
        elif choice == "2":
            add_reminder(reminders)
        elif choice == "3":
            print("Goodbye! 🤍")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
