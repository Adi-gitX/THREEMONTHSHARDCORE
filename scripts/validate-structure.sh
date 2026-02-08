#!/bin/bash

# validate-structure.sh - Validate repository structure
# Checks that all 90 day folders exist with required files

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
JOURNEY_DIR="$REPO_ROOT/journey"

echo "🔍 Validating repository structure..."
echo ""

errors=0
warnings=0

# Check journey folder exists
if [ ! -d "$JOURNEY_DIR" ]; then
    echo -e "${RED}✗ Journey folder not found!${NC}"
    exit 1
fi

# Check all 90 days exist
for i in $(seq -w 1 90); do
    day_folder="$JOURNEY_DIR/day$i"
    if [ ! -d "$day_folder" ]; then
        echo -e "${RED}✗ Missing: day$i${NC}"
        ((errors++))
        continue
    fi
    
    # Check required files
    for file in README.md tasks.md learnings.md notes.md; do
        if [ ! -f "$day_folder/$file" ]; then
            echo -e "${YELLOW}⚠ day$i: missing $file${NC}"
            ((warnings++))
        fi
    done
    
    # Check resources folder
    if [ ! -d "$day_folder/resources" ]; then
        echo -e "${YELLOW}⚠ day$i: missing resources folder${NC}"
        ((warnings++))
    fi
done

# Check core files
for file in GOALS.md PROGRESS.md README.md; do
    if [ ! -f "$JOURNEY_DIR/$file" ]; then
        echo -e "${RED}✗ Missing: journey/$file${NC}"
        ((errors++))
    fi
done

# Check root files
for file in README.md LICENSE CONTRIBUTING.md; do
    if [ ! -f "$REPO_ROOT/$file" ]; then
        echo -e "${YELLOW}⚠ Missing: $file${NC}"
        ((warnings++))
    fi
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $errors -eq 0 ] && [ $warnings -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
else
    echo -e "Errors: ${RED}$errors${NC} | Warnings: ${YELLOW}$warnings${NC}"
fi

exit $errors
