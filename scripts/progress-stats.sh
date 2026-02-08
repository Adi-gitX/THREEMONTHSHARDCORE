#!/bin/bash

# progress-stats.sh - Display progress statistics
# Shows completion status across all days

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
JOURNEY_DIR="$REPO_ROOT/journey"
PLAN_FILE="$REPO_ROOT/CompletePlan/Semester6.csv"

echo "📊 THREE MONTHS HARDCORE - Progress Statistics"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Count days with content
total_days=90
completed=0
in_progress=0

for i in $(seq -w 1 90); do
    readme="$JOURNEY_DIR/day$i/README.md"
    if [ -f "$readme" ]; then
        # Check if day has been filled in (not template)
        if grep -q "Status.*✅\|Status.*🟢\|Completed" "$readme" 2>/dev/null; then
            ((completed++))
        elif grep -q "Status.*🔄\|In Progress" "$readme" 2>/dev/null; then
            ((in_progress++))
        fi
    fi
done

not_started=$((total_days - completed - in_progress))
percent=$((completed * 100 / total_days))

# Progress bar
bar_size=30
filled=$((percent * bar_size / 100))
empty=$((bar_size - filled))
bar=$(printf "%${filled}s" | tr ' ' '█')$(printf "%${empty}s" | tr ' ' '░')

echo "Progress: [$bar] $percent%"
echo ""
echo "📈 Status Breakdown:"
echo "   ✅ Completed:   $completed / $total_days days"
echo "   🔄 In Progress: $in_progress days"
echo "   ⬜ Not Started: $not_started days"
echo ""

# Subject areas from plan
if [ -f "$PLAN_FILE" ]; then
    echo "📚 Subjects in Plan:"
    echo "   • Operating Systems (1.5 hrs/day)"
    echo "   • DevOps (1.5 hrs/day)"
    echo "   • DL/AML (1.25 hrs/day)"
    echo "   • Advanced Discrete Math (45 min/day)"
    echo "   • DSA (30 min/day)"
    echo "   • Interview Prep (30 min/day)"
    echo ""
fi

echo "🎯 Keep going! Every day counts!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
