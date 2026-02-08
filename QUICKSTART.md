# 🚀 Quick Start Guide

Welcome to your 90-day hardcore journey! This guide will help you get started.

## 📋 Initial Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Adi-gitX/THREEMONTHSHARDCORE.git
cd THREEMONTHSHARDCORE
```

### 2. Review the Structure
```bash
# View the main README
cat README.md

# Check the journey folder
ls journey/

# Run validation to ensure everything is set up correctly
./scripts/validate-structure.sh
```

### 3. Set Your Goals
Edit the goals file to define your objectives:
```bash
# Open and customize your goals
nano journey/GOALS.md
# or
code journey/GOALS.md
```

## 📅 Daily Workflow

### Starting a New Day

1. **Navigate to the day's folder:**
   ```bash
   cd journey/day01  # Replace with current day
   ```

2. **Update the README.md:**
   - Add today's date
   - Define your focus for the day
   - List your tasks

3. **Work on your tasks**

4. **Document as you go:**
   - Update `tasks.md` as you complete items
   - Capture learnings in `learnings.md`
   - Add notes to `notes.md`
   - Save resources in the `resources/` folder

5. **End-of-day reflection:**
   - Update README.md with summary
   - Mark tasks as complete
   - Rate your energy, productivity, and mood
   - Write reflection notes

6. **Commit your progress:**
   ```bash
   git add .
   git commit -m "Day XX: [Brief summary]"
   git push
   ```

### Using Scripts

**Check your progress:**
```bash
./scripts/progress-stats.sh
```

**Validate structure:**
```bash
./scripts/validate-structure.sh
```

**Generate a day template:**
```bash
python3 scripts/generate-template.py 1 2026-02-08
```

## 💡 Tips for Success

### 1. **Be Consistent**
- Update daily, even if it's just a quick note
- Small progress is still progress
- Don't break the chain!

### 2. **Be Specific**
- Write clear, actionable tasks
- Document specific learnings with examples
- Include measurable achievements

### 3. **Be Honest**
- Reflect truthfully on your day
- Document challenges and failures
- Learn from mistakes

### 4. **Be Organized**
- Keep files in their proper locations
- Use descriptive names for resources
- Maintain consistent formatting

### 5. **Review Regularly**
- Weekly: Review the past week's progress
- Monthly: Update monthly goals and milestones
- Adjust your approach based on what works

## 📊 Tracking Progress

### Weekly Review
At the end of each week:
1. Review all 7 days
2. Identify patterns (what worked, what didn't)
3. Update goals if needed
4. Plan for the next week

### Monthly Review
At the end of each month:
1. Review the entire month
2. Check off completed goals
3. Celebrate achievements
4. Set new goals for next month
5. Update the PROGRESS.md file

## 🎯 Customization

Feel free to customize:
- Add your own templates
- Create additional scripts
- Modify the structure to fit your needs
- Add new tracking metrics

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 🆘 Troubleshooting

### Missing Files
Run the validation script to identify missing files:
```bash
./scripts/validate-structure.sh
```

### Git Issues
Make sure you're in the repository root:
```bash
cd /path/to/THREEMONTHSHARDCORE
git status
```

### Script Permissions
If scripts won't run, make them executable:
```bash
chmod +x scripts/*.sh scripts/*.py
```

## 📚 Additional Resources

- [Main README](./README.md) - Overview and navigation
- [Contributing Guidelines](./CONTRIBUTING.md) - Best practices
- [Scripts Documentation](./scripts/README.md) - Script usage
- [Templates](./templates/) - Quick reference templates

## 🎉 Ready to Start?

1. Set your goals in `journey/GOALS.md`
2. Navigate to `journey/day01/`
3. Update the README.md with today's date
4. Start working on your first day!

---

**"The journey of a thousand miles begins with a single step."**

*Let's make these 90 days count!* 💪

[← Back to Main](./README.md) | [Start Day 01 →](./journey/day01/)
