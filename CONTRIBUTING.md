# Contributing to THREE MONTHS HARDCORE

Thank you for your interest in contributing! This guide will help you maintain consistency.

## 📁 Folder Structure

```
THREEMONTHSHARDCORE/
├── journey/
│   ├── day01/ - day90/     # Daily progress folders
│   ├── GOALS.md            # Goals & milestones
│   ├── PROGRESS.md         # Progress tracker
│   └── README.md           # Journey overview
├── CompletePlan/           # Study plans
├── scripts/                # Automation scripts
├── templates/              # Reusable templates
└── README.md               # Main readme
```

## 📝 Daily Entry Guidelines

Each day folder (`day01` - `day90`) should contain:
- `README.md` - Daily summary
- `tasks.md` - Task checklist
- `learnings.md` - Key learnings
- `notes.md` - Additional notes
- `resources/` - Supporting files

## ✅ Naming Conventions

- Folders: lowercase with numbers (`day01`, `day02`)
- Files: lowercase with hyphens (`weekly-summary.md`)
- No spaces in filenames

## 🔧 Before Committing

1. Run validation: `./scripts/validate-structure.sh`
2. Update progress in daily README
3. Use descriptive commit messages

## 📊 Progress Tracking

Mark task completion status:
- `[ ]` - Not started
- `[/]` - In progress  
- `[x]` - Completed

## 🎯 Commit Message Format

```
type: brief description

Examples:
- day: complete day 15 tasks
- fix: update broken navigation
- docs: add weekly summary
```
