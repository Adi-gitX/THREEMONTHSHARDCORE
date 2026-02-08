# 🖥️ Operating Systems

> **Time Allocation:** 1.5 hours/day  
> **Exam Weight:** High  
> **Practical Component:** Nand2Tetris OS Implementation

---

## 📚 Course Overview

This comprehensive OS curriculum covers everything from process management to building a complete operating system from scratch using the Nand2Tetris platform.

---

## 🗓️ Learning Path

### **Phase 1: Foundation (Weeks 1-3)**

#### Week 1: Processes & Architecture
- **Day 1-2:** OS Architecture, Services, Process Concepts
  - OS layer diagram
  - System calls (fork, exec, wait)
  - PCB state transitions
- **Day 3-5:** System Calls & Modes
  - open/read/write/close
  - User vs Kernel mode
  - Protection rings
- **Day 6-7:** Process Creation & IPC
  - Pipes & inter-process communication
  - IPC methods comparison

**📝 Key Deliverables:**
- OS architecture diagram
- System call implementations in C
- IPC code examples

#### Week 2: CPU Scheduling
- **Algorithms Covered:**
  - FCFS (First Come First Served)
  - SJF (Shortest Job First)
  - SRTF (Shortest Remaining Time First)
  - Round Robin (RR)
  - Priority Scheduling
- **Skills:**
  - Gantt chart drawing
  - TAT & WT calculations
  - Context switch analysis

**📝 Key Deliverables:**
- 15+ scheduling problems solved
- Comparison tables for all algorithms
- Formula sheet

#### Week 3: Synchronization
- **Topics:**
  - Semaphores (Binary & Counting)
  - Producer-Consumer Problem
  - Readers-Writers Problem
  - Monitors & Condition Variables
- **Skills:**
  - Code implementations
  - Deadlock prevention
  - Starvation analysis

**📝 Key Deliverables:**
- Semaphore implementations
- Classic problem solutions
- Sync pattern summary

---

### **Phase 2: Midsem Domination (Weeks 4-7)**

#### Week 4-5: Deadlocks
- Deadlock conditions (4 necessary conditions)
- Banker's Algorithm (safety check)
- Resource Allocation Graphs
- Detection & recovery strategies

#### Week 6-7: Memory Management
- Paging & address translation
- TLB & multi-level paging
- Page replacement algorithms (FIFO, LRU, Optimal)
- Belady's Anomaly
- Virtual memory & thrashing

**📝 Midsem Preparation:**
- Past papers (3+)
- 50+ MCQs solved
- Model answers for 10-mark questions

---

### **Phase 3: Advanced Topics (Weeks 8-11)**

#### Nand2Tetris OS Implementation
Build a complete operating system in Jack language:

**Modules to Implement:**
1. **Memory.jack** - Memory allocation
   - `alloc()` - Dynamic allocation
   - `deAlloc()` - Garbage collection

2. **Screen.jack** - Graphics
   - `drawPixel()`, `drawLine()`, `drawRect()`
   - Bitmap manipulation

3. **Keyboard.jack** - Input handling
   - `readChar()`, `readLine()`, `readInt()`

4. **String.jack** - String operations
   - String manipulation from scratch

5. **Math.jack** - Mathematical operations
   - `multiply()`, `divide()`, `sqrt()`
   - Bit manipulation techniques

6. **Output.jack** - Display output

7. **Sys.jack** - System functions
   - `init()`, `halt()`, `error()`

**Final Project:** Pong Game using your OS!

#### File Systems & Disk Scheduling
- File allocation methods
- Directory structures
- Disk scheduling algorithms (FCFS, SSTF, SCAN, C-SCAN)
- DMA vs interrupt-driven I/O

---

### **Phase 4: Final Lock-in (Weeks 12-13)**

#### Comprehensive Revision
- **Day 78-79:** Processes + Scheduling
- **Day 80-81:** Sync + Deadlocks
- **Day 82-83:** Memory + Files
- **Day 84:** Nand2Tetris final review
- **Day 85-89:** Mock exams & speed drills
- **Day 90:** Final exam execution

**📝 Final Deliverables:**
- Complete Nand2Tetris OS with documentation
- Technical architecture document
- 3+ past papers solved
- Comprehensive formula sheet

---

## 🛠️ Resources

### Essential Textbooks
- **Operating System Concepts** by Silberschatz, Galvin, Gagne (Dinosaur Book)
- **Modern Operating Systems** by Tanenbaum
- **Nand2Tetris** by Nisan & Schocken

### Online Resources
- [Nand2Tetris Course](https://www.nand2tetris.org/)
- [OS Dev Wiki](https://wiki.osdev.org/)
- [Linux From Scratch](http://www.linuxfromscratch.org/)

### Coding Practice
- Implement system calls in C
- Write scheduling simulators
- Build sync primitives
- Complete Nand2Tetris projects

---

## 📊 Assessment Strategy

### Contest Preparation
- **Contest 1 (Day 7):** Processes & basics
- **Contest 2 (Day 42):** Memory management
- **Contest 3 (Day 49):** Comprehensive midsem
- **Contest 4 (Day 90):** Final exam

### Study Techniques
1. **Visual Learning:** Draw diagrams for every concept
2. **Active Coding:** Implement algorithms in C
3. **Problem Solving:** Solve 3-5 problems per topic
4. **Answer Writing:** Practice 10-mark questions
5. **Speed Drills:** Timed MCQ sessions

---

## 🎯 Success Metrics

- [ ] All 6 scheduling algorithms mastered
- [ ] Banker's algorithm solved (10+ problems)
- [ ] Nand2Tetris OS complete & tested
- [ ] Page replacement algorithms (15+ problems)
- [ ] Pong game running on custom OS
- [ ] 3+ past papers solved
- [ ] Midsem & Final exams: 85%+ target

---

## 📝 Notes Template

For each topic, maintain:
```markdown
## [Topic Name]

### Key Concepts
- Concept 1
- Concept 2

### Formulas
- Formula 1
- Formula 2

### Problems Solved
1. Problem description → Solution approach
2. ...

### Code Implementations
[Link to code]

### Diagrams
[Link to diagrams]

### Questions for Review
- Question 1
- Question 2
```

---

## 🔗 Related Resources

- [Back to Complete Plan](../../README.md)
- [DevOps](../devops/)
- [Journey Tracker](../../../journey/)

---

**Remember:** OS is foundational. Master these concepts and everything else becomes easier!

*Last Updated: Day 0*
