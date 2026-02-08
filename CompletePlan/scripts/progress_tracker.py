#!/usr/bin/env python3
"""
Progress Tracker - Visual progress display for the 91-day journey
"""

import csv
from pathlib import Path
from datetime import datetime, timedelta


def create_progress_bar(completed, total, length=40):
    """Create a visual progress bar"""
    filled = int(length * completed / total)
    empty = length - filled
    bar = '█' * filled + '░' * empty
    percentage = int(100 * completed / total)
    return f"[{bar}] {percentage}% ({completed}/{total})"


def calculate_days_completed(csv_path):
    """Calculate how many days have been completed"""
    # This would check the 'Done' columns in the CSV
    # For now, returns 0 as placeholder
    completed = 0
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Check if all main tasks are done
            all_done = row.get('ALL COMPLETE', '').lower() == 'yes'
            if all_done:
                completed += 1
    
    return completed


def generate_weekly_breakdown(total_days=91):
    """Generate weekly breakdown"""
    weeks = []
    day = 1
    for week_num in range(1, 14):
        if week_num <= 12:
            days_in_week = 7
        else:
            days_in_week = 7  # Week 13 has 7 days (Days 85-91)
        
        week_end = min(day + days_in_week - 1, total_days)
        weeks.append({
            'week': week_num,
            'start': day,
            'end': week_end,
            'total': week_end - day + 1
        })
        day = week_end + 1
        
        if day > total_days:
            break
    
    return weeks


def generate_progress_report(csv_path, output_path):
    """Generate a markdown progress report"""
    
    # Calculate stats
    total_days = 91
    completed_days = calculate_days_completed(csv_path)
    remaining_days = total_days - completed_days
    
    # Calculate phase progress
    foundation_days = 21
    midsem_days = 28  # Days 22-49
    advanced_days = 28  # Days 50-77
    final_days = 14    # Days 78-91
    
    # Generate report
    report = f"""# 📊 Progress Report

> **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 🎯 Overall Progress

{create_progress_bar(completed_days, total_days, 50)}

**Days Completed:** {completed_days} / {total_days}  
**Days Remaining:** {remaining_days}  
**Completion Rate:** {int(100 * completed_days / total_days)}%

---

## 📅 Phase Breakdown

### Phase 1: Foundation (Days 1-21)
{create_progress_bar(min(completed_days, foundation_days), foundation_days)}

### Phase 2: Midsem Domination (Days 22-49)
{create_progress_bar(max(0, min(completed_days - foundation_days, midsem_days)), midsem_days)}

### Phase 3: Advanced + Projects (Days 50-77)
{create_progress_bar(max(0, min(completed_days - foundation_days - midsem_days, advanced_days)), advanced_days)}

### Phase 4: Final Lock-in (Days 78-91)
{create_progress_bar(max(0, min(completed_days - foundation_days - midsem_days - advanced_days, final_days)), final_days)}

---

## 📊 Weekly Breakdown

"""
    
    weeks = generate_weekly_breakdown()
    for week in weeks:
        completed_in_week = max(0, min(completed_days - week['start'] + 1, week['total']))
        status = '✅ Complete' if completed_in_week == week['total'] else \
                 '⏳ In Progress' if completed_in_week > 0 else \
                 '⬜️ Not Started'
        
        report += f"**Week {week['week']}** (Days {week['start']}-{week['end']}) - {status}\n"
        report += f"{create_progress_bar(completed_in_week, week['total'], 30)}\n\n"
    
    report += f"""---

## 🎯 Milestones

- {'✅' if completed_days >= 7 else '⬜️'} **Day 7** - First Week Complete
- {'✅' if completed_days >= 14 else '⬜️'} **Day 14** - Two Weeks Strong
- {'✅' if completed_days >= 21 else '⬜️'} **Day 21** - Foundation Complete
- {'✅' if completed_days >= 30 else '⬜️'} **Day 30** - Month 1 Complete
- {'✅' if completed_days >= 45 else '⬜️'} **Day 45** - Halfway Point
- {'✅' if completed_days >= 60 else '⬜️'} **Day 60** - Month 2 Complete
- {'✅' if completed_days >= 75 else '⬜️'} **Day 75** - 75% Complete
- {'✅' if completed_days >= 84 else '⬜️'} **Day 84** - Projects Complete
- {'✅' if completed_days >= 90 else '⬜️'} **Day 90** - Final Exams Complete
- {'✅' if completed_days >= 91 else '⬜️'} **Day 91** - 🎉 JOURNEY COMPLETE!

---

## 📈 Study Time Tracking

**Expected Total:** ~600 hours (6.6 hrs/day × 91 days)  
**Completed:** ~{int(completed_days * 6.6)} hours  
**Remaining:** ~{int(remaining_days * 6.6)} hours

---

## 💡 Insights

### Pace Analysis
"""
    
    if completed_days > 0:
        days_per_week = completed_days / max(1, completed_days // 7 + 1)
        report += f"- Average: {days_per_week:.1f} days per week\n"
        
        if completed_days >= 7:
            projected_completion = int(91 * 7 / days_per_week)
            report += f"- Projected completion: Day {projected_completion}\n"
            
            if projected_completion <= 91:
                report += f"- Status: ✅ On track!\n"
            else:
                report += f"- Status: ⚠️ Behind schedule by ~{projected_completion - 91} days\n"
    else:
        report += "- No data yet. Start your journey!\n"
    
    report += f"""

### Next Milestone
"""
    
    next_milestone = None
    milestones = [
        (7, "First Week Complete"),
        (14, "Two Weeks Strong"),
        (21, "Foundation Complete"),
        (30, "Month 1 Complete"),
        (45, "Halfway Point"),
        (60, "Month 2 Complete"),
        (75, "75% Complete"),
        (84, "Projects Complete"),
        (90, "Final Exams"),
        (91, "Journey Complete")
    ]
    
    for day, name in milestones:
        if completed_days < day:
            next_milestone = (day, name)
            break
    
    if next_milestone:
        days_until = next_milestone[0] - completed_days
        report += f"**Day {next_milestone[0]}:** {next_milestone[1]}\n"
        report += f"- {days_until} days remaining\n"
    else:
        report += "🎉 All milestones completed!\n"
    
    report += """

---

## 🔥 Motivation

**Remember:**
- Progress over perfection
- Consistency compounds
- Every day counts
- You've got this! 💪

---

*To update this report, run: `python scripts/progress_tracker.py`*
"""
    
    # Write report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Progress report generated: {output_path}")
    print(f"\n📊 Current Status:")
    print(f"   Completed: {completed_days}/{total_days} days")
    print(f"   {create_progress_bar(completed_days, total_days)}")


if __name__ == "__main__":
    script_dir = Path(__file__).parent.parent
    csv_path = script_dir / "Semister6.csv"
    output_path = script_dir.parent / "journey" / "PROGRESS.md"
    
    if not csv_path.exists():
        print(f"❌ Error: CSV file not found at {csv_path}")
        exit(1)
    
    generate_progress_report(csv_path, output_path)
    print(f"\n💡 Tip: Update your CSV 'ALL COMPLETE' column to track progress!")
