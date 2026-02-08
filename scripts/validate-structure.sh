#!/bin/bash
# Script to validate the consistency of all day folders

echo "🔍 Validating repository structure..."

ERRORS=0
WARNINGS=0

# Check if all day folders exist
echo ""
echo "📁 Checking day folders..."
for i in $(seq -f "%02g" 1 90); do
    if [ ! -d "journey/day$i" ]; then
        echo "❌ ERROR: journey/day$i folder missing"
        ERRORS=$((ERRORS + 1))
    fi
done

# Check if all required files exist in each day folder
echo ""
echo "📄 Checking required files in each day folder..."
for i in $(seq -f "%02g" 1 90); do
    DAY_DIR="journey/day$i"
    
    if [ -d "$DAY_DIR" ]; then
        # Check README.md
        if [ ! -f "$DAY_DIR/README.md" ]; then
            echo "❌ ERROR: $DAY_DIR/README.md missing"
            ERRORS=$((ERRORS + 1))
        fi
        
        # Check tasks.md
        if [ ! -f "$DAY_DIR/tasks.md" ]; then
            echo "⚠️  WARNING: $DAY_DIR/tasks.md missing"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check learnings.md
        if [ ! -f "$DAY_DIR/learnings.md" ]; then
            echo "⚠️  WARNING: $DAY_DIR/learnings.md missing"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check notes.md
        if [ ! -f "$DAY_DIR/notes.md" ]; then
            echo "⚠️  WARNING: $DAY_DIR/notes.md missing"
            WARNINGS=$((WARNINGS + 1))
        fi
        
        # Check resources folder
        if [ ! -d "$DAY_DIR/resources" ]; then
            echo "⚠️  WARNING: $DAY_DIR/resources folder missing"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
done

# Summary
echo ""
echo "📊 Validation Summary:"
echo "   Errors: $ERRORS"
echo "   Warnings: $WARNINGS"

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo ""
    echo "✅ All checks passed! Repository structure is valid."
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo ""
    echo "⚠️  Validation completed with warnings."
    exit 0
else
    echo ""
    echo "❌ Validation failed with errors."
    exit 1
fi
