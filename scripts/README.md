# 🛠️ Automation Scripts

This directory contains automation scripts to help manage and track the 90-day journey.

---

## 📜 Available Scripts

### `update_progress.py`
**Purpose:** Automatically update the progress tracker with current statistics.

**What it does:**
- Scans all 90 day folders
- Counts completed days
- Calculates progress percentages
- Updates weekly and monthly breakdowns
- Tracks streaks (current and longest)
- Counts total tasks and learnings
- Updates `journey/PROGRESS.md` with fresh data

**Usage:**
```bash
python3 scripts/update_progress.py
```

**When to run:**
- After completing a day
- Before reviewing your progress
- At the end of each week
- Anytime you want updated statistics

---

### `validate_repo.py`
**Purpose:** Validate repository consistency and check for issues.

**What it checks:**
- All day folders have required files (README.md, tasks.md, learnings.md, notes.md)
- All day folders have resources directory
- Navigation links are consistent
- Day 01 doesn't link to non-existent Day 00
- Day 90 doesn't link to non-existent Day 91
- Header formatting is consistent across all days

**Usage:**
```bash
python3 scripts/validate_repo.py
```

**When to run:**
- Before committing major changes
- When you suspect navigation issues
- As part of weekly maintenance
- Before creating weekly summaries

**Output:**
- ✅ Success message if everything is valid
- ⚠️ List of issues if problems are found

---

## 🚀 Quick Tips

### Daily Workflow
1. Complete your daily tasks
2. Update day's README with status: `✅ Complete`
3. Run `update_progress.py` to update statistics
4. Commit your changes

### Weekly Workflow
1. Run `validate_repo.py` to check for issues
2. Fix any reported issues
3. Run `update_progress.py` for final stats
4. Create weekly summary using the template
5. Review progress and plan next week

### Making Scripts Executable (Optional)
```bash
chmod +x scripts/update_progress.py
chmod +x scripts/validate_repo.py
```

Then you can run them directly:
```bash
./scripts/update_progress.py
./scripts/validate_repo.py
```

---

## 🔧 Requirements

- Python 3.6+
- No external dependencies (uses standard library only)

---

## 💡 Future Enhancements

Potential scripts to add:
- [ ] Daily task generator from CSV
- [ ] Progress visualization (charts/graphs)
- [ ] Automated weekly summary generator
- [ ] Streak tracker with notifications
- [ ] Study time calculator
- [ ] GitHub integration for automated commits

---

## 🤝 Contributing

Have ideas for new automation scripts? Feel free to contribute! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

*Automation is the key to consistency. Let the scripts do the heavy lifting!* 🚀
