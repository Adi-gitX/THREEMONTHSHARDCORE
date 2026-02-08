# Changelog

All notable changes and improvements to this project will be documented in this file.

## [Unreleased]

### Added
- Added badges to main README (Days, Progress, Status)
- Added Table of Contents to main README
- Created QUICKSTART.md guide for easy onboarding
- Created CONTRIBUTING.md with comprehensive guidelines
- Created LICENSE file (MIT License)
- Added `/scripts` directory with automation tools:
  - `validate-structure.sh` - Repository structure validation
  - `progress-stats.sh` - Progress statistics display
  - `generate-template.py` - Daily template generator
- Added `/templates` directory with reusable templates:
  - `day-readme-template.md` - Daily README template
  - `learnings-template.md` - Daily learnings template
  - `tasks-template.md` - Daily tasks template
  - `notes-template.md` - Daily notes template
- Created README files for scripts and templates directories
- Enhanced .gitignore with comprehensive exclusions

### Fixed
- Fixed typo in CompletePlan directory: "Semister6.csv" → "Semester6.csv"
- Removed UTF-8 BOM from CSV file for better compatibility
- Fixed broken navigation link in Day 01 (removed reference to non-existent Day 00)
- Fixed broken navigation link in Day 90 (removed reference to non-existent Day 91)
- Improved navigation with emoji and clearer labels

### Changed
- Enhanced main README with better organization
- Improved documentation structure throughout repository
- Made all scripts executable by default

## [1.0.0] - 2026-02-08

### Initial Release
- Created basic 90-day journey structure
- 90 day folders (day01-day90) with templates
- Journey tracking files (PROGRESS.md, GOALS.md)
- Basic documentation structure
- CompletePlan with semester schedule

---

## Types of Changes
- **Added** - New features
- **Changed** - Changes in existing functionality
- **Deprecated** - Soon-to-be removed features
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security improvements
