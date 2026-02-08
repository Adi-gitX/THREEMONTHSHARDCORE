#!/usr/bin/env python3
"""
Validation Script
Checks repository consistency and reports any issues
"""

import os
from pathlib import Path

# Configuration
JOURNEY_DIR = Path(__file__).parent.parent / "journey"
TOTAL_DAYS = 90

def validate_structure():
    """Validate that all day folders have the correct structure."""
    issues = []
    
    required_files = ["README.md", "tasks.md", "learnings.md", "notes.md"]
    required_dirs = ["resources"]
    
    for day in range(1, TOTAL_DAYS + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        
        # Check if day directory exists
        if not day_dir.exists():
            issues.append(f"❌ Day {day:02d}: Directory missing")
            continue
        
        # Check required files
        for file_name in required_files:
            file_path = day_dir / file_name
            if not file_path.exists():
                issues.append(f"❌ Day {day:02d}: Missing {file_name}")
        
        # Check required directories
        for dir_name in required_dirs:
            dir_path = day_dir / dir_name
            if not dir_path.exists():
                issues.append(f"⚠️  Day {day:02d}: Missing {dir_name}/ directory")
    
    return issues


def validate_navigation():
    """Validate that navigation links are consistent."""
    issues = []
    
    for day in range(1, TOTAL_DAYS + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        readme_file = day_dir / "README.md"
        
        if not readme_file.exists():
            continue
        
        content = readme_file.read_text()
        
        # Check Day 01 - should link to Home and Day 02
        if day == 1:
            if "day00" in content.lower():
                issues.append(f"❌ Day 01: Invalid link to Day 00 (doesn't exist)")
            if "Home" not in content and "🏠" not in content:
                issues.append(f"⚠️  Day 01: Missing Home link")
        
        # Check Day 90 - should link to Day 89 and Home
        elif day == 90:
            if "day91" in content.lower():
                issues.append(f"❌ Day 90: Invalid link to Day 91 (doesn't exist)")
            if "Home" not in content and "🏠" not in content:
                issues.append(f"⚠️  Day 90: Missing Home link")
        
        # Check other days - should have prev and next links
        else:
            prev_day = f"day{day-1:02d}"
            next_day = f"day{day+1:02d}"
            
            if prev_day not in content.lower():
                issues.append(f"⚠️  Day {day:02d}: Missing link to {prev_day}")
            if next_day not in content.lower():
                issues.append(f"⚠️  Day {day:02d}: Missing link to {next_day}")
    
    return issues


def validate_headers():
    """Validate that day headers are consistent."""
    issues = []
    
    for day in range(1, TOTAL_DAYS + 1):
        day_dir = JOURNEY_DIR / f"day{day:02d}"
        readme_file = day_dir / "README.md"
        
        if not readme_file.exists():
            continue
        
        content = readme_file.read_text()
        lines = content.split('\n')
        
        if len(lines) == 0:
            issues.append(f"❌ Day {day:02d}: README is empty")
            continue
        
        # Check if first line has proper format
        expected_header = f"# 📅 Day {day:02d}"
        if expected_header not in lines[0]:
            issues.append(f"⚠️  Day {day:02d}: Header format inconsistent (expected '{expected_header}')")
    
    return issues


def main():
    """Run all validation checks."""
    print("🔍 Running validation checks...\n")
    
    all_issues = []
    
    # Run structure validation
    print("📁 Checking folder structure...")
    structure_issues = validate_structure()
    all_issues.extend(structure_issues)
    if structure_issues:
        print(f"   Found {len(structure_issues)} structure issues")
    else:
        print("   ✅ All folders have correct structure")
    
    # Run navigation validation
    print("\n🔗 Checking navigation links...")
    nav_issues = validate_navigation()
    all_issues.extend(nav_issues)
    if nav_issues:
        print(f"   Found {len(nav_issues)} navigation issues")
    else:
        print("   ✅ All navigation links are valid")
    
    # Run header validation
    print("\n📝 Checking header formatting...")
    header_issues = validate_headers()
    all_issues.extend(header_issues)
    if header_issues:
        print(f"   Found {len(header_issues)} header issues")
    else:
        print("   ✅ All headers are properly formatted")
    
    # Summary
    print("\n" + "="*60)
    if all_issues:
        print(f"\n⚠️  Found {len(all_issues)} total issues:\n")
        for issue in all_issues:
            print(f"   {issue}")
        print(f"\n⚠️  Total: {len(all_issues)} issues")
        return 1
    else:
        print("\n✅ All validation checks passed! Repository is consistent.")
        return 0


if __name__ == "__main__":
    exit(main())
