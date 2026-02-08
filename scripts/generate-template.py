#!/usr/bin/env python3
"""
Daily Template Generator
Helps create or update daily documentation with proper structure
"""

import os
import sys
from datetime import datetime

def create_daily_template(day_number, date_str=None):
    """Create a complete daily template"""
    
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    
    day_formatted = f"day{day_number:02d}"
    day_path = f"journey/{day_formatted}"
    
    # Create directory if it doesn't exist
    os.makedirs(day_path, exist_ok=True)
    os.makedirs(f"{day_path}/resources", exist_ok=True)
    
    # README.md template
    prev_day = max(1, day_number - 1)
    next_day = min(90, day_number + 1)
    
    nav_prev = f"[← Day {prev_day:02d}](../day{prev_day:02d}/)" if day_number > 1 else "[⬅️ Back to Journey](../)"
    nav_next = f"[Day {next_day:02d} →](../day{next_day:02d}/)" if day_number < 90 else "[🏆 Journey Complete!](../)"
    
    readme_content = f"""# 📅 Day {day_number:02d}

> **Date:** {date_str}  
> **Status:** ⬜️ Not Started

---

## 🎯 Today's Focus

_What are you focusing on today?_

---

## ✅ Tasks Completed

- [ ] Task 1
- [ ] Task 2
- [ ] Task 3
- [ ] Task 4
- [ ] Task 5

---

## 🏆 Achievements

- Achievement 1
- Achievement 2
- Achievement 3

---

## 📝 Summary

_Write a brief summary of what you accomplished today..._

---

## 🔗 Related Files

- [Tasks](./tasks.md)
- [Learnings](./learnings.md)
- [Notes](./notes.md)
- [Resources](./resources/)

---

## 💭 Reflection

_What went well? What could be improved?_

---

**Energy Level:** ⭐⭐⭐⭐⭐  
**Productivity:** ⭐⭐⭐⭐⭐  
**Mood:** 😊

---

{nav_prev} | {nav_next}
"""
    
    # Write README.md
    with open(f"{day_path}/README.md", 'w') as f:
        f.write(readme_content)
    
    print(f"✅ Created/Updated {day_path}/README.md")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate-template.py <day_number> [date]")
        print("Example: python3 generate-template.py 1")
        print("Example: python3 generate-template.py 1 2026-02-08")
        sys.exit(1)
    
    day = int(sys.argv[1])
    date = sys.argv[2] if len(sys.argv) > 2 else None
    
    if day < 1 or day > 90:
        print("Error: Day number must be between 1 and 90")
        sys.exit(1)
    
    create_daily_template(day, date)
    print(f"\n🎉 Template for Day {day:02d} is ready!")
