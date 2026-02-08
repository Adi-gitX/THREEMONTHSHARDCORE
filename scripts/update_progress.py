#!/usr/bin/env python3
"""
Progress Tracker Script
Automatically tracks and updates progress across the 90-day journey
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Configuration
JOURNEY_DIR = Path(__file__).parent.parent / "journey"
PROGRESS_FILE = JOURNEY_DIR / "PROGRESS.md"
TOTAL_DAYS = 90


def count_completed_days():
    """Count how many days have been marked as completed."""
    completed = 0
    
    for day in range(1, TOTAL_DAYS + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        readme_file = day_dir / "README.md"
        
        if readme_file.exists():
            content = readme_file.read_text()
            # Check if status is completed
            if "✅ Complete" in content or "🟢 Complete" in content:
                completed += 1
    
    return completed


def calculate_progress(completed):
    """Calculate progress percentage and create progress bar."""
    percentage = int((completed / TOTAL_DAYS) * 100)
    filled = int((completed / TOTAL_DAYS) * 20)
    empty = 20 - filled
    progress_bar = "█" * filled + "░" * empty
    
    return percentage, progress_bar


def get_month_progress(start_day, end_day):
    """Get progress for a specific month."""
    completed = 0
    total = end_day - start_day + 1
    
    for day in range(start_day, end_day + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        readme_file = day_dir / "README.md"
        
        if readme_file.exists():
            content = readme_file.read_text()
            if "✅ Complete" in content or "🟢 Complete" in content:
                completed += 1
    
    percentage = int((completed / total) * 100) if total > 0 else 0
    filled = int((completed / total) * 10) if total > 0 else 0
    empty = 10 - filled
    progress_bar = "█" * filled + "░" * empty
    
    return completed, total, percentage, progress_bar


def get_week_status(start_day, end_day):
    """Get status for a specific week."""
    completed = 0
    total = end_day - start_day + 1
    
    for day in range(start_day, end_day + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        readme_file = day_dir / "README.md"
        
        if readme_file.exists():
            content = readme_file.read_text()
            if "✅ Complete" in content or "🟢 Complete" in content:
                completed += 1
    
    if completed == total:
        return completed, total, "✅ Complete"
    elif completed > 0:
        return completed, total, "🟡 In Progress"
    else:
        return completed, total, "⬜️ Not Started"


def count_tasks_and_learnings():
    """Count total tasks completed and learnings documented."""
    total_tasks = 0
    total_learnings = 0
    
    for day in range(1, TOTAL_DAYS + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        
        # Count tasks
        tasks_file = day_dir / "tasks.md"
        if tasks_file.exists():
            content = tasks_file.read_text()
            total_tasks += content.count("- [x]")
        
        # Count learnings
        learnings_file = day_dir / "learnings.md"
        if learnings_file.exists():
            content = learnings_file.read_text()
            # Count non-empty learning entries (lines starting with - or *)
            total_learnings += len([line for line in content.split('\n') 
                                   if line.strip().startswith(('-', '*')) 
                                   and len(line.strip()) > 5])
    
    return total_tasks, total_learnings


def calculate_streak():
    """Calculate current and longest streak."""
    current_streak = 0
    longest_streak = 0
    temp_streak = 0
    
    for day in range(1, TOTAL_DAYS + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        readme_file = day_dir / "README.md"
        
        if readme_file.exists():
            content = readme_file.read_text()
            if "✅ Complete" in content or "🟢 Complete" in content:
                temp_streak += 1
                longest_streak = max(longest_streak, temp_streak)
            else:
                if current_streak == 0:
                    current_streak = temp_streak
                temp_streak = 0
        else:
            if current_streak == 0:
                current_streak = temp_streak
            temp_streak = 0
    
    # If we reached the end while on a streak, that's the current streak
    if temp_streak > 0:
        current_streak = temp_streak
    
    return current_streak, longest_streak


def update_progress_file():
    """Update the PROGRESS.md file with current statistics."""
    completed_days = count_completed_days()
    percentage, progress_bar = calculate_progress(completed_days)
    
    # Month breakdowns
    m1_comp, m1_total, m1_pct, m1_bar = get_month_progress(1, 30)
    m2_comp, m2_total, m2_pct, m2_bar = get_month_progress(31, 60)
    m3_comp, m3_total, m3_pct, m3_bar = get_month_progress(61, 90)
    
    # Week statuses
    weeks = [
        (1, 1, 7), (2, 8, 14), (3, 15, 21), (4, 22, 30),
        (5, 31, 37), (6, 38, 44), (7, 45, 51), (8, 52, 60),
        (9, 61, 67), (10, 68, 74), (11, 75, 81), (12, 82, 90)
    ]
    
    week_data = []
    for week_num, start, end in weeks:
        comp, total, status = get_week_status(start, end)
        week_data.append((week_num, start, end, comp, total, status))
    
    # Statistics
    total_tasks, total_learnings = count_tasks_and_learnings()
    current_streak, longest_streak = calculate_streak()
    
    # Generate new content
    content = f"""# 📈 Progress Tracker

Track your journey through 90 days of hardcore commitment!

---

## 🎯 Overall Progress

```
Days Completed: {completed_days} / {TOTAL_DAYS}
Completion: {percentage}%

[{progress_bar}] {percentage}%
```

---

## 📅 Monthly Breakdown

### Month 1 (Days 1-30)
```
Progress: [{m1_bar}] {m1_comp}/{m1_total} days ({m1_pct}%)
```

| Week | Days | Completed | Status |
|------|------|-----------|--------|
"""
    
    for week_num, start, end, comp, total, status in week_data[:4]:
        content += f"| Week {week_num} | {start:02d}-{end:02d} | {comp}/{total} | {status} |\n"
    
    content += f"""
### Month 2 (Days 31-60)
```
Progress: [{m2_bar}] {m2_comp}/{m2_total} days ({m2_pct}%)
```

| Week | Days | Completed | Status |
|------|------|-----------|--------|
"""
    
    for week_num, start, end, comp, total, status in week_data[4:8]:
        content += f"| Week {week_num} | {start:02d}-{end:02d} | {comp}/{total} | {status} |\n"
    
    content += f"""
### Month 3 (Days 61-90)
```
Progress: [{m3_bar}] {m3_comp}/{m3_total} days ({m3_pct}%)
```

| Week | Days | Completed | Status |
|------|------|-----------|--------|
"""
    
    for week_num, start, end, comp, total, status in week_data[8:]:
        content += f"| Week {week_num} | {start:02d}-{end:02d} | {comp}/{total} | {status} |\n"
    
    content += f"""
---

## 🏆 Milestones

- {"[x]" if completed_days >= 7 else "[ ]"} **Day 7** - First Week Complete! 🎉
- {"[x]" if completed_days >= 14 else "[ ]"} **Day 14** - Two Weeks Strong! 💪
- {"[x]" if completed_days >= 21 else "[ ]"} **Day 21** - Three Weeks Unstoppable! 🔥
- {"[x]" if completed_days >= 30 else "[ ]"} **Day 30** - Month 1 Complete! 🎊
- {"[x]" if completed_days >= 45 else "[ ]"} **Day 45** - Halfway Point! 🚀
- {"[x]" if completed_days >= 60 else "[ ]"} **Day 60** - Month 2 Complete! 🌟
- {"[x]" if completed_days >= 75 else "[ ]"} **Day 75** - 75% There! ⚡
- {"[x]" if completed_days >= 90 else "[ ]"} **Day 90** - JOURNEY COMPLETE! 🏆🎆

---

## 💡 Quick Stats

- **Longest Streak:** {longest_streak} days
- **Current Streak:** {current_streak} days
- **Total Tasks Completed:** {total_tasks}
- **Total Learnings Documented:** {total_learnings}

---

*Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
*Auto-generated by scripts/update_progress.py*
"""
    
    # Write the updated content
    PROGRESS_FILE.write_text(content)
    print(f"✅ Progress file updated!")
    print(f"   Days completed: {completed_days}/{TOTAL_DAYS} ({percentage}%)")
    print(f"   Current streak: {current_streak} days")
    print(f"   Longest streak: {longest_streak} days")


def main():
    """Main function."""
    print("🔄 Updating progress tracker...")
    update_progress_file()
    print("✨ Done!")


if __name__ == "__main__":
    main()
