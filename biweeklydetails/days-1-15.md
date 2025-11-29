# 📘 Days 1–15 — Coding, AI Foundations & Setup (EXTREME DETAILED PLAN)
### Part of the 90-Day Study Plan (Coding · AI/LLMs · Cybersecurity · Networking)

---

# 🧭 Overview (Days 1–15)

These first 15 days build your foundation in:

- Python fundamentals  
- JavaScript fundamentals  
- GitHub setup & workflow  
- Prompt engineering basics  
- LLM concepts  
- First small automation script  
- Your first AI-powered script  

You will complete **two major free courses**, set up all your dev tooling, and create the first 2–3 public GitHub repos.

---

# 📅 DAILY BREAKDOWN (EXTREME DETAIL)

---

# 🔵 **Day 1 — Setup + GitHub + Tools**

### **Goals**
- Install core tools  
- Create GitHub repos  
- Prepare your development environment  

### **Tasks**
#### **1. Install Tools**
- **Python 3.x** → https://www.python.org/downloads/  
- **Node.js LTS** → https://nodejs.org/en  
- **VS Code** → https://code.visualstudio.com/  
- **Git** → https://git-scm.com/  
- **Postman** → https://www.postman.com/  

#### **2. Create GitHub Repositories**
Go to https://github.com/new and create:

| Repo Name | Purpose |
|----------|---------|
| `python-tools` | All Python scripts |
| `js-projects` | JavaScript exercises + Node scripts |
| `ai-playground` | AI/LLM projects & prompt logs |

Commit starter READMEs.

---

# 🔵 **Day 2 — JavaScript Fundamentals (freeCodeCamp)**

### **Course:**  
**freeCodeCamp – JavaScript Algorithms & Data Structures**  
🔗 https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/

### **Modules Today**
- Introduction  
- **Basic JavaScript** → complete first 40–60 challenges  

### **Practice**
Create:
- `variables.js`  
- `functions.js`  
- `loops.js`

### **Deliverables**
- Push JS files to `js-projects`  
- Update README with “Day 2 progress”  

---

# 🔵 **Day 3 — Continue JS + Arrays & Strings**

### **Modules Today**
Continue **Basic JavaScript**, complete sections on:
- Strings  
- Arrays  
- For Loops  

### **Practice**
Create:
- `arrayPractice.js`  
- `stringFormatter.js`

### **Deliverables**
- Commit exercises  
- Add daily log to README  

---

# 🔵 **Day 4 — Python Fundamentals (Python for Everybody)**

### **Course:**  
**Python for Everybody** (Coursera – Free Audit)  
🔗 https://www.coursera.org/specializations/python

### **Modules Today**
- Variables  
- Expressions  
- Conditionals  

### **Practice**
Scripts:
- `hello.py`  
- `mathPractice.py`  
- `conditions.py`

### **Deliverables**
- Commit Python files to `python-tools`  

---

# 🔵 **Day 5 — Python + Git Workflow**

### **Modules Today**
- Looping  
- Basic logic  
- Git workflow (terminal)

### **Git Example**
```bash
git add .
git commit -m "Day 5 progress"
git push
```
### **Practice**
Scripts:
- `loops.py`
- `fizzbuzz.py`

### **Deliverables**
- GitHub streak started  
- README updated  

---

# 🔵 **Day 6 — Begin Prompt Engineering (DeepLearning.AI)**

### **Course:**  
**Prompt Engineering for ChatGPT — DeepLearning.AI**  
🔗 https://www.coursera.org/learn/prompt-engineering

### **Modules Today**
- Lesson 1: *Introduction to Prompting*
- Lesson 2: *Principles of Effective Prompts*

### **Practice**
Create file:  
`ai-playground/prompts/day6.md` containing:
- 5 good prompts  
- 5 bad prompts  
- Why each worked or failed  

### **Deliverables**
- Commit prompt log to `ai-playground` repo  

---

# 🔵 **Day 7 — Prompt Patterns & Context Management**

### **Modules Today**
- Chain-of-Thought prompting  
- Role prompting  
- Step-by-step reasoning prompts  
- Multi-turn refinement  

### **Practice**
Create:
- `cot_examples.md` – 5 chain-of-thought experiments  
- Compare outputs with/without CoT  

### **Deliverables**
- Commit both markdown files  
- Add to README: “Prompt Engineering Notes” section  

---

# 🔵 **Day 8 — Start Hugging Face LLM Course (Transformers)**

### **Course:**  
**Hugging Face – LLM & Transformers Course**  
🔗 https://huggingface.co/learn

### **Modules Today**
- What are LLMs?  
- Tokenizers 101  
- Attention basics  
- Transformer overview  

### **Practice**
Create Jupyter notebook:  
- `tokenizer_test.ipynb`  
  - Load tokenizer  
  - Encode/decode text  
  - Analyze tokens  

### **Deliverables**
- Commit notebook to `ai-playground`  

---

# 🔵 **Day 9 — Hugging Face: First Text Generation Script**

### **Modules Today**
- Using pretrained models  
- Text generation pipeline  
- Safety & truncation basics  

### **Practice**
Create script:  
`hf_generate.py`  
- Load `distilgpt2`  
- Generate text  
- Add args for:
  - max_length  
  - temperature  
  - prompt input  

### **Deliverables**
- Commit script  
- Add usage instructions to README  

---

# 🔵 **Day 10 — Python Automation Script**

### **Goal**
Build your first meaningful automation tool.

### **Task**
Create:  
`file_organizer.py`

### **Suggested Features**
- Sort files by extension  
- Auto-create folders  
- Handle missing folders  
- Optional `--path` argument  
- Optional `--dry-run` mode  

### **Deliverables**
- Commit script  
- Add Before/After screenshot in README  

---

# 🔵 **Day 11 — API Basics + AI Summarizer**

### **Modules Today**
Learn:
- Python `requests`  
- REST API basics  
- JSON parsing  
- Calling OpenAI or HF Inference API  

### **Practice**
Create:  
`ai_summarizer.py`  
- Input: large block of text  
- Output: summary  
- Add CLI flag: `--bullets` or `--short`  

### **Deliverables**
- Commit script  
- Add example screenshot  

---

# 🔵 **Day 12 — Node.js CLI Tool**

### **Goal**
Create your first Node.js command-line program.

### **Project:**  
`text-cleaner.js`

### **Features**
- Remove special characters  
- Trim whitespace  
- Convert to lowercase  
- Optional flags:
  - `--uppercase`  
  - `--remove-num`  
  - `--remove-symbols`  

### **Deliverables**
- Commit script  
- Add usage examples:
node text-cleaner.js input.txt --uppercase

---

# 🔵 **Day 13 — Intermediate Python: JSON, Files, Error Handling**

### **Modules Today**
Python for Everybody:
- Working with files  
- Try/Except  
- Dictionaries  
- JSON parsing  

### **Practice Scripts**
- `json_parser.py` – reads + extracts data  
- `log_reader.py` – scans logs for errors  

### **Deliverables**
- Commit code  
- Write “Day 13 — What I Learned” in README  

---

# 🔵 **Day 14 — First Real AI Project (Choose One)**

Choose **ONE** of the following:

### ✔ **1. AI Resume Analyzer**  
- Input: resume text  
- Output:
- Skills extracted  
- Missing skills  
- Readability score  
- Improve-this-resume suggestions  

### ✔ **2. AI Study Planner Generator**  
- Input: goals + timeframe  
- Output: structured multi-week plan  

### ✔ **3. AI Coding Helper CLI**  
- Input: code snippet  
- Output:
- Bug explanations  
- Improvements  
- Rewrite suggestions  

### **Requirements**
- CLI script OR web app  
- Clear README  
- Example outputs  
- Code well-commented  

### **Deliverables**
Folder:  
`/ai-projects/project1/`  

Files:
- `main.py` or `index.js`
- `requirements.txt` (if Python)
- README (description, install, usage, screenshots)

---

# 🔵 **Day 15 — Review + Portfolio Polish**

### **Tasks**
- Refactor any messy code  
- Add screenshots to READMEs  
- Add badges or shields (optional)  
- Update GitHub profile README  
- Write 15-day summary:
- What I built  
- What I learned  
- What I struggled with  
- What I’ll tackle next  

### **Certificates to Add**
- freeCodeCamp progress screenshot  
- Prompt Engineering certificate (if you completed paid version)  
- Hugging Face learning notes  

### **Final Deliverables**
By the end of Day 15 you have:

- ✔ JavaScript fundamentals  
- ✔ Python fundamentals  
- ✔ Prompt engineering basics  
- ✔ Hugging Face LLM fundamentals  
- ✔ 1–2 AI mini projects  
- ✔ A clean, active GitHub portfolio  

---

# 🔗 Quick Links Summary

### **Coding**
- freeCodeCamp JS → https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/
- Python for Everybody → https://www.coursera.org/specializations/python

### **AI / LLMs**
- Prompt Engineering → https://www.coursera.org/learn/prompt-engineering
- Hugging Face Course → https://huggingface.co/learn

### **Tools**
- Python → https://python.org
- Node.js → https://nodejs.org
- VS Code → https://code.visualstudio.com
- Git → https://git-scm.com

---

# ✅ End of Days 1–15  
Ready for **Days 16–30** or a **full /90days folder with a .md file for every block**?
