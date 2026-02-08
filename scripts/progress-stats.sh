#!/bin/bash
# Script to calculate and display progress statistics

echo "📈 THREE MONTHS HARDCORE - Progress Statistics"
echo "=============================================="
echo ""

TOTAL_DAYS=90
COMPLETED_DAYS=0

# Count completed days (days with status ✅)
for i in $(seq -f "%02g" 1 90); do
    DAY_FILE="journey/day$i/README.md"
    if [ -f "$DAY_FILE" ]; then
        if grep -q "Status.*✅.*Completed" "$DAY_FILE"; then
            COMPLETED_DAYS=$((COMPLETED_DAYS + 1))
        fi
    fi
done

# Calculate percentage
PERCENTAGE=$((COMPLETED_DAYS * 100 / TOTAL_DAYS))

# Display progress
echo "📅 Days Completed: $COMPLETED_DAYS / $TOTAL_DAYS"
echo "📊 Progress: $PERCENTAGE%"
echo ""

# Progress bar
FILLED=$((PERCENTAGE / 5))
EMPTY=$((20 - FILLED))

printf "["
for ((i=0; i<$FILLED; i++)); do printf "█"; done
for ((i=0; i<$EMPTY; i++)); do printf "░"; done
printf "] $PERCENTAGE%%\n"

echo ""

# Monthly breakdown
echo "📆 Monthly Breakdown:"
echo ""

# Month 1
MONTH1_COMPLETED=0
for i in $(seq -f "%02g" 1 30); do
    if [ -f "journey/day$i/README.md" ] && grep -q "Status.*✅.*Completed" "journey/day$i/README.md"; then
        MONTH1_COMPLETED=$((MONTH1_COMPLETED + 1))
    fi
done
MONTH1_PERCENT=$((MONTH1_COMPLETED * 100 / 30))
echo "   Month 1 (Days 1-30):  $MONTH1_COMPLETED/30 ($MONTH1_PERCENT%)"

# Month 2
MONTH2_COMPLETED=0
for i in $(seq -f "%02g" 31 60); do
    if [ -f "journey/day$i/README.md" ] && grep -q "Status.*✅.*Completed" "journey/day$i/README.md"; then
        MONTH2_COMPLETED=$((MONTH2_COMPLETED + 1))
    fi
done
MONTH2_PERCENT=$((MONTH2_COMPLETED * 100 / 30))
echo "   Month 2 (Days 31-60): $MONTH2_COMPLETED/30 ($MONTH2_PERCENT%)"

# Month 3
MONTH3_COMPLETED=0
for i in $(seq -f "%02g" 61 90); do
    if [ -f "journey/day$i/README.md" ] && grep -q "Status.*✅.*Completed" "journey/day$i/README.md"; then
        MONTH3_COMPLETED=$((MONTH3_COMPLETED + 1))
    fi
done
MONTH3_PERCENT=$((MONTH3_COMPLETED * 100 / 30))
echo "   Month 3 (Days 61-90): $MONTH3_COMPLETED/30 ($MONTH3_PERCENT%)"

echo ""
echo "=============================================="

# Show next milestone
if [ $COMPLETED_DAYS -lt 7 ]; then
    echo "🎯 Next Milestone: Day 7 - First Week Complete!"
elif [ $COMPLETED_DAYS -lt 14 ]; then
    echo "🎯 Next Milestone: Day 14 - Two Weeks Strong!"
elif [ $COMPLETED_DAYS -lt 21 ]; then
    echo "🎯 Next Milestone: Day 21 - Three Weeks!"
elif [ $COMPLETED_DAYS -lt 30 ]; then
    echo "🎯 Next Milestone: Day 30 - Month 1 Complete!"
elif [ $COMPLETED_DAYS -lt 45 ]; then
    echo "🎯 Next Milestone: Day 45 - Halfway Point!"
elif [ $COMPLETED_DAYS -lt 60 ]; then
    echo "🎯 Next Milestone: Day 60 - Month 2 Complete!"
elif [ $COMPLETED_DAYS -lt 75 ]; then
    echo "🎯 Next Milestone: Day 75 - 75% There!"
elif [ $COMPLETED_DAYS -lt 90 ]; then
    echo "🎯 Next Milestone: Day 90 - Journey Complete!"
else
    echo "🏆 JOURNEY COMPLETE! Congratulations!"
fi

echo ""
