#!/usr/bin/env python3
"""
Daily Study Plan Extractor
Extracts daily tasks from Semister6.csv and generates markdown files
"""

import csv
import os
from pathlib import Path

def parse_csv_to_daily_plans(csv_path, output_dir):
    """Parse CSV and generate daily plan markdown files"""
    
    # Read CSV
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for i, row in enumerate(rows, start=1):
        day_num = i
        
        # Extract key information
        title = row.get('Title', f'Day {day_num}')
        date = row.get('Date', '')
        week = row.get('Week', '')
        phase = row.get('Phase', '')
        contest = row.get('Contest/Event', '')
        
        # Subject details
        os_task = row.get('OS (1.5hr)', '')
        os_action = row.get('OS Action', '')
        
        devops_task = row.get('DevOps (1.5hr)', '')
        devops_action = row.get('DevOps Action', '')
        
        dl_task = row.get('DL/AML (1.25hr)', '')
        
        adm_task = row.get('ADM (45min)', '')
        
        dsa_task = row.get('DSA (30min)', '')
        
        interview_task = row.get('Interview Prep (30min)', '')
        
        project_task = row.get('Project Task', '')
        
        networking_task = row.get('Networking', '')
        
        # Generate markdown
        md_content = f"""# Day {day_num} - {title}

> **Date:** {date}  
> **Week:** {week}  
> **Phase:** {phase}  
> **Contest/Event:** {contest if contest else 'None'}

---

## 🎯 Today's Schedule

### 🖥️ Operating Systems (1.5 hours)
**Topic:** {os_task}

**Action Items:**
{os_action}

**Deliverables:**
- [ ] Complete reading/coding
- [ ] Solve practice problems
- [ ] Update notes

---

### 🚀 DevOps (1.5 hours)
**Topic:** {devops_task}

**Action Items:**
{devops_action}

**Deliverables:**
- [ ] Complete setup/implementation
- [ ] Document configurations
- [ ] Test deployments

---

### 🧠 Deep Learning / AML (1.25 hours)
**Topic:** {dl_task}

**Deliverables:**
- [ ] Complete implementation
- [ ] Run experiments
- [ ] Document results

---

### 🔢 Advanced Discrete Mathematics (45 minutes)
**Topic:** {adm_task}

**Deliverables:**
- [ ] Solve problems
- [ ] Write proofs
- [ ] Update formula sheet

---

### 📊 DSA (30 minutes)
**Topic:** {dsa_task}

**Deliverables:**
- [ ] Solve problems on LeetCode
- [ ] Understand patterns
- [ ] Code optimal solutions

---

### 🎤 Interview Prep (30 minutes)
**Topic:** {interview_task}

**Deliverables:**
- [ ] Practice problems
- [ ] Review patterns
- [ ] Mock interview (if scheduled)

---

### 💻 Project Work
**Task:** {project_task}

**Deliverables:**
- [ ] Complete task
- [ ] Push to GitHub
- [ ] Update documentation

---

### 🌐 Networking & Career
**Activities:** {networking_task}

**Deliverables:**
- [ ] Complete networking activities
- [ ] Update profiles
- [ ] Send applications

---

## 📝 Notes Section

### Key Learnings


### Challenges Faced


### Solutions Found


---

## ✅ End of Day Checklist

- [ ] All subjects covered
- [ ] Notes updated
- [ ] Code committed
- [ ] Progress logged
- [ ] Tomorrow planned

---

**Energy Level:** ___ / 10  
**Productivity:** ___ / 10  
**Overall:** ✅ Complete / ⏳ Partial / ❌ Incomplete

---

[← Previous Day](./day{day_num-1:02d}.md) | [Next Day →](./day{day_num+1:02d}.md)
"""
        
        # Write to file
        output_file = os.path.join(output_dir, f'day{day_num:02d}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"✅ Generated: day{day_num:02d}.md")
    
    print(f"\n🎉 Successfully generated {len(rows)} daily plan files in {output_dir}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent.parent
    csv_path = script_dir / "Semister6.csv"
    output_dir = script_dir / "daily-plans"
    
    if not csv_path.exists():
        print(f"❌ Error: CSV file not found at {csv_path}")
        exit(1)
    
    parse_csv_to_daily_plans(csv_path, output_dir)
    print("\n💡 Tip: You can now review each day's plan in the daily-plans/ folder!")
