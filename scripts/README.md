# 🛠️ Scripts

This directory contains helpful automation scripts for managing your 90-day journey.

## Available Scripts

### 1. `validate-structure.sh`
**Purpose:** Validates the repository structure to ensure consistency

**Usage:**
```bash
./scripts/validate-structure.sh
```

**Features:**
- Checks if all 90 day folders exist
- Verifies required files in each day folder
- Reports errors and warnings

### 2. `progress-stats.sh`
**Purpose:** Displays progress statistics and completion status

**Usage:**
```bash
./scripts/progress-stats.sh
```

**Features:**
- Shows overall progress percentage
- Displays visual progress bar
- Shows monthly breakdown
- Highlights next milestone

### 3. `generate-template.py`
**Purpose:** Generates or updates daily templates with proper structure

**Usage:**
```bash
# Generate template for a specific day
python3 scripts/generate-template.py <day_number>

# Generate template with specific date
python3 scripts/generate-template.py <day_number> <date>
```

**Examples:**
```bash
# Create template for Day 1
python3 scripts/generate-template.py 1

# Create template for Day 15 with custom date
python3 scripts/generate-template.py 15 2026-02-22
```

## Running Scripts

All scripts should be run from the repository root directory:

```bash
cd /path/to/THREEMONTHSHARDCORE
./scripts/validate-structure.sh
./scripts/progress-stats.sh
python3 scripts/generate-template.py 1
```

## Requirements

- **Bash Scripts:** Require bash shell (available on Linux, macOS, and Windows with WSL/Git Bash)
- **Python Scripts:** Require Python 3.6 or higher

## Contributing

Feel free to add more automation scripts to improve the workflow! See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

*Automation makes consistency easier!* 🚀
