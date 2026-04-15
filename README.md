
## Challenge: Student Grade Analyzer

---

### Problem Statement:

Aapko ek program likhna hai jo **students ke grades** ko analyze kare.

---

### Data:

```python
students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 78),
    ("Fatima", 95),
    ("Bilal", 88),
    ("Zara", 92),
    ("Omar", 76),
    ("Ayesha", 95)
]
```

---

### Tasks:

1. **Average Grade** - Sab students ke grades ka average nikaalo (round to 2 decimal places)

2. **Top Student** - Sabse zyada grade wala student ka naam aur grade find karo

3. **Grade Categories** - Har student ko grade dena:
   - 90+ → "A"
   - 80-89 → "B"
   - 70-79 → "C"
   - Below 70 → "D"

4. **Passing Students** - Un students ki list banao jinka grade 80 ya usse zyada hai

5. **Unique Grades** - Saari unique grades ki list banao (sorted ascending)

6. **Grade Frequency** - Batayo kaunsi grade kitni baar aayi hai

---

### Expected Output Format:

```
Average Grade: 86.38

Top Student: Fatima (95)

Grade Categories:
Ali: 85 → B
Sara: 92 → A
...

Passing Students (Grade >= 80):
Sara, Fatima, Bilal, Zara, Ayesha, Ali

Unique Grades (Sorted): [76, 78, 85, 88, 92, 95]

Grade Frequency:
76: 1 time
78: 1 time
85: 1 time
88: 1 time
92: 2 times
95: 2 times
```

---

### Bonus Challenge:

Bina `max()`, `min()`, `sum()`, `sorted()` functions ke karo (manually loop se).

---

### Rules:

✅ Sirf **basic loops, conditions, lists, dictionaries** use karo  
✅ `sum()`, `max()`, `min()`, `sorted()` allowed hai (bonus mein nahi)  
✅ Output **exact format** mein likhna zaroori nahi, lekin sahi information honi chahiye

---

### Submit:

Apna code likh kar bhejo, main check karunga aur feedback dunga! 💪

Kya aapko ye challenge karna hai?