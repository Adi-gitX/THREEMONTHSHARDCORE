#!/usr/bin/env python3
"""
generate-template.py - Generate day templates or weekly summaries
Usage:
    python3 generate-template.py --day 15
    python3 generate-template.py --week 3
    python3 generate-template.py --help
"""

import argparse
import os
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
TEMPLATES_DIR = os.path.join(REPO_ROOT, "templates")

def generate_day_template(day_num: int) -> str:
    """Generate a daily template with pre-filled content."""
    template = f"""# 📅 Day {day_num:02d}

> **Date:** {datetime.now().strftime("%Y-%m-%d")}  
> **Status:** 🔄 In Progress

---

## 🎯 Today's Focus

_What are you focusing on today?_

---

## ✅ Tasks Completed

- [ ] OS: 
- [ ] DevOps: 
- [ ] DL/AML: 
- [ ] ADM: 
- [ ] DSA: 
- [ ] Interview: 

---

## 🏆 Achievements

- Achievement 1
- Achievement 2

---

## 📝 Summary

_Write a brief summary of what you accomplished today..._

---

## 💭 Reflection

_What went well? What could be improved?_

---

**Energy Level:** ⭐⭐⭐⭐⭐  
**Productivity:** ⭐⭐⭐⭐⭐
"""
    return template


def generate_weekly_summary(week_num: int) -> str:
    """Generate a weekly summary template."""
    start_day = (week_num - 1) * 7 + 1
    end_day = min(week_num * 7, 90)
    
    template = f"""# 📊 Week {week_num} Summary

> **Days Covered:** Day {start_day:02d} - Day {end_day:02d}  
> **Date Range:** _[Add dates]_

---

## 🎯 Weekly Goals

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

---

## ✅ Completed Tasks

### Operating Systems
- Task 1
- Task 2

### DevOps
- Task 1
- Task 2

### DL/AML
- Task 1

### DSA
- Problems solved: X

---

## 📈 Progress Metrics

| Subject | Planned | Completed | % |
|---------|---------|-----------|---|
| OS | X hrs | Y hrs | Z% |
| DevOps | X hrs | Y hrs | Z% |
| DL/AML | X hrs | Y hrs | Z% |
| ADM | X hrs | Y hrs | Z% |
| DSA | X problems | Y problems | Z% |

---

## 🏆 Key Achievements

1. Achievement 1
2. Achievement 2
3. Achievement 3

---

## 💭 Weekly Reflection

**What went well:**
- 

**What to improve:**
- 

**Next week focus:**
- 

---

## 🔗 Day Links

"""
    for d in range(start_day, end_day + 1):
        template += f"- [Day {d:02d}](../day{d:02d}/)\n"
    
    return template


def main():
    parser = argparse.ArgumentParser(
        description="Generate templates for THREE MONTHS HARDCORE"
    )
    parser.add_argument("--day", type=int, help="Generate day template (1-90)")
    parser.add_argument("--week", type=int, help="Generate weekly summary (1-13)")
    parser.add_argument("--output", "-o", help="Output file path (optional)")
    
    args = parser.parse_args()
    
    if args.day:
        if not 1 <= args.day <= 90:
            print("Error: Day must be between 1 and 90")
            return 1
        content = generate_day_template(args.day)
        filename = f"day{args.day:02d}_template.md"
    elif args.week:
        if not 1 <= args.week <= 13:
            print("Error: Week must be between 1 and 13")
            return 1
        content = generate_weekly_summary(args.week)
        filename = f"week{args.week:02d}_summary.md"
    else:
        parser.print_help()
        return 0
    
    if args.output:
        output_path = args.output
    else:
        output_path = os.path.join(TEMPLATES_DIR, filename)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"✅ Generated: {output_path}")
    return 0


if __name__ == "__main__":
    exit(main())
