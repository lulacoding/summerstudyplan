import os

# ============================================================
# 90-DAY ULTRA STUDY PACK GENERATOR (Days 1–15 Fully Written)
# ============================================================

OUTPUT_FOLDER = "dailytasks"

# Create folder if missing
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------------------
# DAY TEMPLATES (1–15)
# ---------------------------

day_templates = {
    1: """# 📘 Day 1 — Environment Setup & GitHub Initialization

## 🎯 Goals
- Install all core tools
- Create GitHub repositories
- Prepare your development environment

## 📚 Learning Links
- Python → https://www.python.org/downloads/
- Node.js → https://nodejs.org/en
- VS Code → https://code.visualstudio.com/
- Git → https://git-scm.com/
- Postman → https://www.postman.com/

---

## 🛠️ Today’s Tasks
### 1. Install Required Tools
- Install Python 3.x  
- Install Node.js LTS  
- Install VS Code  
- Install Git  
- Install Postman

### 2. Create GitHub Repositories
Create these at https://github.com/new:  
- `python-tools`
- `js-projects`
- `ai-playground`

Initialize each with a README.

---

# ✍️ NOTES (Write what you did, what worked, what failed)
-  

---

# 🧠 SELF-TEST QUESTIONS
1. Why do programmers use GitHub?  
2. What is version control?  
3. What’s the difference between Git and GitHub?  
4. What is a repository?  
5. Why is it important to document your work?

_Write your answers here:_
-  
-  
-  

---

# 🚀 WHAT I BUILT TODAY
(Document everything you set up)
-  

---

# 📌 REFLECTION
- What confused you today?
- What went well?
- What do you need to revisit?

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Customize your GitHub profile README
- Install helpful VS Code extensions (GitLens, Python, Prettier)
""",

    2: """# 📘 Day 2 — JavaScript Fundamentals (freeCodeCamp)

## 🎯 Goals
- Begin JavaScript basics
- Complete first 40–60 challenges on freeCodeCamp

## 📚 Course
freeCodeCamp — JavaScript Algorithms & Data Structures  
https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/

---

## 🛠️ Today’s Tasks
- Complete Introduction + first part of *Basic JavaScript*
- Create files:
  - variables.js
  - functions.js
  - loops.js
- Commit all files to your `js-projects` repository

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is a variable?  
2. What are `let`, `var`, and `const`?  
3. What is a function?  
4. What is a loop used for?  
5. Write a simple function example here:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Make a function that reverses a string manually.
""",

    3: """# 📘 Day 3 — JS Arrays & Strings

## 🎯 Goals
- Learn arrays & string manipulation
- Build basic data-processing functions

## 📚 Course
Continue freeCodeCamp Basic JavaScript.

---

## 🛠️ Today’s Tasks
Create:
- arrayPractice.js
- stringFormatter.js

Exercises to do:
- Accessing array elements  
- Looping over arrays  
- String slicing  
- String methods  

Commit all progress to GitHub.

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is an array?  
2. How do you access the third item in an array?  
3. What does `.push()` do?  
4. What does `.pop()` do?  
5. Write an example array below:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a JS function that finds the largest number in an array.
""",

    4: """# 📘 Day 4 — Python Fundamentals (Python for Everybody)

## 🎯 Goals
- Learn Python basics (variables, expressions, conditionals)

## 📚 Course Link
Python for Everybody (Coursera – Free Audit)  
https://www.coursera.org/specializations/python

---

## 🛠️ Today’s Tasks
Write:
- hello.py  
- mathPractice.py  
- conditions.py  

Complete Coursera modules:
- Variables  
- Expressions  
- Conditionals  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is a Python variable?  
2. What is a conditional?  
3. What does `input()` do?  
4. Write an `if/elif/else` example:  
5. What is the difference between `=` and `==`?

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Write a script that asks for your name and greets you differently based on time of day.
""",

    5: """# 📘 Day 5 — Python Loops + Git Workflow

## 🎯 Goals
- Learn Python loops
- Practice Git workflow from terminal

---

## 🛠️ Today’s Tasks
Create:
- loops.py  
- fizzbuzz.py  

Learn:
- `for` loops  
- `while` loops  
- Git commands:
git add .
git commit -m "Day 5 progress"
git push

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is the difference between a `for` loop and a `while` loop?  
2. What does `git commit` do?  
3. What is the purpose of `git push`?  
4. Explain what FizzBuzz is:  
5. Write an example loop below:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Modify FizzBuzz to print custom words based on user input.
"""
}
# CONTINUATION OF DAY TEMPLATES (Days 6–10)

day_templates.update({

    6: """# 📘 Day 6 — Prompt Engineering Basics (DeepLearning.AI)

## 🎯 Goals
- Understand what prompts are
- Learn how LLMs interpret instructions
- Begin applying prompt-engineering principles

## 📚 Course Link
Prompt Engineering for ChatGPT (DeepLearning.AI)  
https://www.coursera.org/learn/prompt-engineering

---

## 🛠️ Today’s Tasks
- Complete:
  - Lesson 1: Introduction to Prompting  
  - Lesson 2: Principles of Prompt Writing
- Create:
  - prompts/day6.md
    - 5 good prompts  
    - 5 bad prompts  
    - Why the good ones work

---

# ✍️ NOTES
- 

---

# 🧠 SELF-TEST QUESTIONS
1. What is prompt engineering?  
2. Why do “bad prompts” fail?  
3. What does “be specific” mean in prompting?  
4. What is a model “instruction”?  
5. Write 2 prompts that produced different results today.

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Create a prompt that forces the model to perform multi-step reasoning.
""",

    7: """# 📘 Day 7 — Prompt Patterns & CoT (Chain of Thought)

## 🎯 Goals
- Learn advanced prompting strategies
- Master chain-of-thought reasoning techniques

## 📚 Course Continuation
Prompt Engineering for ChatGPT (DeepLearning.AI)

---

## 🛠️ Today’s Tasks
- Study:
  - Chain-of-Thought prompting  
  - Role Prompting  
  - Multi-step refinement  
- Create:
  - cot_examples.md  
  - Compare 5 prompts with/without reasoning steps

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is chain-of-thought prompting?  
2. How does role prompting work?  
3. Why might step-by-step reasoning improve results?  
4. What’s the danger of overusing CoT?  
5. Write your best CoT prompt today:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Try one extremely complex reasoning prompt (math, cybersecurity scenario, etc.).
""",

    8: """# 📘 Day 8 — Hugging Face LLM Course (Transformers Intro)

## 🎯 Goals
- Learn how LLMs actually work
- Understand tokenization
- Begin studying transformer architecture

## 📚 Course Link
Hugging Face – Transformers & LLM Course  
https://huggingface.co/learn

---

## 🛠️ Today’s Tasks
Complete:
- Intro to LLMs  
- Tokenization section  
- Transformer basics  

Create:
- tokenizer_test.ipynb  
  - encode/decode text  
  - view token IDs  
  - compare tokenization of two sentences

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is a token?  
2. Why do LLMs use tokenization instead of raw text?  
3. What is an embedding?  
4. What problem do transformers solve?  
5. Write an example of tokenized text below:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Try building a custom tokenizer using Hugging Face’s `tokenizers` library.
""",

    9: """# 📘 Day 9 — HF Models + First Text Generator

## 🎯 Goals
- Load pretrained models
- Learn the HF pipeline API
- Build your first text-generating Python script

## 📚 Course Section
Hugging Face “Using Pretrained Models”

---

## 🛠️ Today’s Tasks
Create:
- hf_generate.py  
  Features:
    - Load model (distilgpt2 recommended)  
    - Accept user prompt  
    - Print generated text  
    - Use temperature & max_length options  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is a pretrained model?  
2. Why is `distilgpt2` lightweight?  
3. What does temperature do?  
4. What does max_length do?  
5. Write your prompt + generation results below:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add command line arguments using argparse.
""",

    10: """# 📘 Day 10 — Python Automation Script

## 🎯 Goals
- Build your first useful automation tool
- Strengthen Python scripting & file operations

---

## 🛠️ Today’s Tasks
Create:
- file_organizer.py

Features:
- Sort files by extension  
- Auto-create folders  
- Use os & shutil  
- Add optional:
  - --path argument  
  - --dry-run mode  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What does shutil.move() do?  
2. How do you list files in a directory?  
3. What is a file extension?  
4. Why use argparse?  
5. Write pseudocode for your script:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add logging + a “verbose” mode.
"""
})

# CONTINUATION OF DAY TEMPLATES (Days 11–15)

day_templates.update({

    11: """# 📘 Day 11 — API Basics + AI Summarizer Tool

## 🎯 Goals
- Learn Python requests module
- Understand REST APIs
- Build your first AI-powered summarizer tool

---

## 🛠️ Today’s Tasks
Create:
- ai_summarizer.py  

Features:
- Input text  
- Call LLM API (OpenAI / HF Inference API)  
- Output a summary  
- Add options: --short, --bullets  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is an API?  
2. What is an endpoint?  
3. What is JSON?  
4. Write a sample API request here:  
5. What prompt did you use for summarizing?

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add translation or sentiment analysis options.
""",

    12: """# 📘 Day 12 — Node.js CLI Tool

## 🎯 Goals
- Build your first Node.js command-line utility
- Learn how Node handles arguments & stdin

---

## 🛠️ Today’s Tasks
Create:
- text-cleaner.js

Features:
- Convert text to lowercase  
- Remove special characters  
- Normalize whitespace  
- Optional flags:
  - --uppercase  
  - --remove-num  
  - --remove-symbols  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What is Node.js?  
2. What does process.argv do?  
3. How do you read a file in Node?  
4. What is a CLI tool used for?  
5. Write your favorite function from today:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Turn your script into an NPM package.
""",

    13: """# 📘 Day 13 — Intermediate Python (Files, JSON, Try/Except)

## 🎯 Goals
- Learn more complex Python features
- Build scripts that handle real data

---

## 🛠️ Today’s Tasks
Write:
- json_parser.py  
- log_reader.py  

Topics:
- Working with files  
- Try/Except blocks  
- JSON parsing  
- Dictionaries  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What does try/except do?  
2. How do you read a file in Python?  
3. What is a dictionary?  
4. Why is JSON useful?  
5. Write a simple try/except example:

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add error logging to your scripts.
""",

    14: """# 📘 Day 14 — First Real AI Project

## 🎯 Goals
- Build a complete AI-powered tool
- Practice project structure, documenting, and GitHub workflow

---

## 🛠️ Today’s Tasks
Choose ONE project:

1. AI Resume Analyzer  
2. AI Study Planner Generator  
3. AI Coding Helper CLI  

Requirements:
- Accept input  
- Call LLM API  
- Produce useful output  
- Add README + examples  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What project did you choose and why?  
2. What API did you use?  
3. What problems did you encounter?  
4. What feature worked the best?  
5. What will you add next?

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
-  

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add a GUI using Tkinter or a web UI using Flask.
""",

    15: """# 📘 Day 15 — Review + Portfolio Polish

## 🎯 Goals
- Review everything from Days 1–14
- Clean up repos, document progress
- Improve your portfolio presentation

---

## 🛠️ Today's Tasks
- Refactor messy code  
- Update READMEs  
- Add screenshots  
- Write a 15-day progress summary  
- Add certificates:
  - freeCodeCamp progress  
  - Prompt Engineering certificate  
  - HF notes summaries  

---

# ✍️ NOTES
-  

---

# 🧠 SELF-TEST QUESTIONS
1. What skills improved the most in the last 15 days?  
2. What still confuses you?  
3. What was the biggest win so far?  
4. Which repo are you most proud of?  
5. What is your plan for Days 16–30?

---

# 🚀 WHAT I BUILT TODAY
-  

---

# 📌 REFLECTION
- What should I change for the next 15 days?
- What habits worked well?
- What habits failed?

---

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a portfolio webpage that showcases your GitHub projects.
"""
})
day_templates.update({

    16: """# 📘 Day 16 — Networking Foundations (TCP/IP + OSI)

## 🎯 Goals
- Understand how data moves across networks
- Learn OSI layers and TCP/IP stack fundamentals

## 📚 Learning
- Professor Messer: Network+ OSI/TCP  
  https://www.professormesser.com/network-plus/n10-008/

---

## 🛠️ Tasks
- Watch OSI Model + TCP/IP lessons  
- Create notes:
  - What each OSI layer does  
  - 3 protocol examples per layer

Create file: notes/day16-network-basics.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. List all 7 OSI layers in order.  
2. What is encapsulation?  
3. What is TCP vs UDP?  
4. Give 5 protocol examples.  
5. What does Layer 3 handle?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Draw OSI model from memory.
""",

    17: """# 📘 Day 17 — Subnets & IP Addressing

## 🎯 Goals
- Understand subnetting
- Perform binary conversions and CIDR calculations

## 📚 Learning
- FreeCCNAWorkbook — Subnetting  
  https://www.freeccnaworkbook.com/

---

## 🛠️ Tasks
- Study:
  - IPv4 classes  
  - Subnet masks  
  - CIDR notation  
- Create:
  - subnet_practice.md
  - Solve 10 subnet questions

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a subnet?  
2. Convert /26 to a subnet mask.  
3. How many hosts in /27?  
4. What does CIDR stand for?  
5. Convert 255.255.255.0 to CIDR.

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Make your own subnet cheat sheet.
""",

    18: """# 📘 Day 18 — Wireshark Basics

## 🎯 Goals
- Use Wireshark to capture & inspect network packets
- Understand low-level protocol behaviors

## 📚 Learning
- Wireshark Docs  
  https://www.wireshark.org/docs/

---

## 🛠️ Tasks
- Install Wireshark  
- Capture:
  - DNS lookup  
  - TCP handshake  
  - HTTP request  
- Save PCAPs to `/captures/day18/`

Write: wireshark-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a packet?  
2. Explain 3-way handshake.  
3. What does DNS do?  
4. What is a Wireshark filter?  
5. What is a protocol dissector?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Extract a full HTTP conversation using “Follow TCP Stream.”
""",

    19: """# 📘 Day 19 — Linux Essentials

## 🎯 Goals
- Learn core Linux commands
- Understand file permissions & processes

## 📚 Learning
- Linux Journey  
  https://linuxjourney.com/

---

## 🛠️ Tasks
Learn commands:
- ls, cd, pwd  
- mkdir, rm, mv, cp  
- chmod, chown  
- ps, kill  

Create: linux_practice.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What does chmod do?  
2. What is a PID?  
3. What is /etc?  
4. Absolute vs relative path?  
5. Give example: grant rwx to user only.

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Install & use htop.
""",

    20: """# 📘 Day 20 — Linux Shell Scripting

## 🎯 Goals
- Learn bash scripting fundamentals
- Automate small tasks with loops, conditions & variables

## 📚 Learning
- freeCodeCamp — Bash Scripting  
  https://www.freecodecamp.org/news/bash-scripting-tutorial-linux/

---

## 🛠️ Tasks
Create scripts:
- hello.sh  
- backup.sh  
- cleanup.sh  

Scripts must include:
- variables  
- loops  
- conditions  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. How to make a script executable?  
2. Purpose of `#!/bin/bash`?  
3. What is `$1`?  
4. Write a loop example.  
5. Write a condition example.

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Script that monitors disk usage & alerts.
""",

    21: """# 📘 Day 21 — Virtual Machines & Networking

## 🎯 Goals
- Learn how virtual networks work inside VirtualBox
- Understand Host-Only, NAT, Bridged modes

## 📚 Learning
VirtualBox Networking Guide  
https://www.virtualbox.org/manual/ch06.html

---

## 🛠️ Tasks
- Install Ubuntu VM  
- Test:
  - NAT mode  
  - Bridged networking  
  - Host-only networking  
- Document in: virtualization-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is NAT mode?  
2. What is bridged mode?  
3. Define host-only.  
4. Why use a VM NIC?  
5. When to use each mode?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Install 2 VMs & test connectivity between them.
""",

    22: """# 📘 Day 22 — Cybersecurity Foundations (Threat Landscape)

## 🎯 Goals
- Understand modern cyber threats
- Learn key terminology

## 📚 Learning
Cybrary Intro to Cybersecurity  
https://www.cybrary.it/course/introduction-to-it-and-cybersecurity/

---

## 🛠️ Tasks
Study:
- Malware types  
- Social engineering  
- Attack vectors  

Write: notes/threat-landscape.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Define malware.  
2. What is ransomware?  
3. What is phishing?  
4. CIA triad?  
5. What is an attack vector?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Research a real breach from 2023-2025.
""",

    23: """# 📘 Day 23 — Cybersecurity Lab Setup

## 🎯 Goals
- Build your own cybersecurity learning lab
- Learn safe VM isolation

## 🛠️ Tasks
- Install:
  - Kali Linux  
  - Security Onion  

Setup:
- NAT networking  
- Snapshots  
- Isolation  

Write: lab-setup.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Why use VMs for cyber labs?  
2. What is a snapshot?  
3. Why NOT run malware on host?  
4. Tools included in Kali?  
5. What is Security Onion used for?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add a Windows VM for full attack chain simulation.
""",

    24: """# 📘 Day 24 — Linux for Cybersecurity (Kali Tools)

## 🎯 Goals
- Learn recon & enumeration tools
- Understand basic offensive techniques

## 🛠️ Tasks
Explore tools:
- nmap  
- whois  
- dig  
- traceroute  
- netcat  

Document: kali-recon-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is nmap?  
2. What is enumeration?  
3. What is a port?  
4. What can netcat do?  
5. Purpose of traceroute?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Scan your isolated lab network.
""",

    25: """# 📘 Day 25 — Web Basics (HTTP/HTTPS)

## 🎯 Goals
- Understand how the web works
- Learn request/response behavior

## 📚 Learning
MDN HTTP Basics  
https://developer.mozilla.org/en-US/docs/Web/HTTP

---

## 🛠️ Tasks
Study:
- HTTP Methods  
- Status Codes  
- Headers  
- Cookies  

Write: http-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. GET vs POST?  
2. What is a cookie?  
3. What does HTTPS add?  
4. Explain 200, 404, 500.  
5. What is a header?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Use Postman to explore APIs.
""",

    26: """# 📘 Day 26 — Web Security Basics (OWASP)

## 🎯 Goals
- Learn top web vulnerabilities
- Understand how attacks work

## 📚 Learning
OWASP Top 10  
https://owasp.org/www-project-top-ten/

---

## 🛠️ Tasks
Study:
- XSS  
- SQL Injection  
- CSRF  
- Broken Authentication  

Write: owasp-top10-summary.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is XSS?  
2. SQL injection?  
3. What is CSRF?  
4. What is a vulnerability?  
5. What is mitigation?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Test concepts on DVWA (LOW difficulty).
""",

    27: """# 📘 Day 27 — Python for Cybersecurity

## 🎯 Goals
- Use Python for recon, parsing, automation

## 🛠️ Tasks
Write:
- port_scan.py  
- banner_grabber.py  
- service_finder.py  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a socket?  
2. How does a port scanner work?  
3. What is a banner?  
4. Why automate recon?  
5. Libraries useful for cybersecurity?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add threading to your port scanner.
""",

    28: """# 📘 Day 28 — Ethical Hacking Basics (TryHackMe)

## 🎯 Goals
- Hands-on hacking basics
- Learn structured pentesting approach

## 📚 Learning
TryHackMe Free Rooms:
- Intro to Cybersecurity  
- Basic Pentesting  
- Linux Fundamentals  
https://tryhackme.com/

---

## 🛠️ Tasks
- Complete 2–3 rooms  
- Write: tryhackme-notes.md  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is pentesting?  
2. What is enumeration?  
3. Privilege escalation?  
4. Tools used today?  
5. Hardest challenge?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Complete “Pickle Rick” or “Ice”.
""",

    29: """# 📘 Day 29 — Secure Coding Practices

## 🎯 Goals
- Write safer code
- Understand common coding bugs

## 📚 Learning
OWASP Secure Coding Practices  
https://owasp.org/www-project-secure-coding-practices/

---

## 🛠️ Tasks
Study:
- Input validation  
- Output encoding  
- Authentication security  

Write: secure-coding-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is sanitization?  
2. Why validate input?  
3. What is output encoding?  
4. Example of insecure code?  
5. Secure version?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a secure login system in Python.
""",

    30: """# 📘 Day 30 — Mini Project + Review

## 🎯 Goals
- Consolidate Days 16–29
- Build first real cybersecurity coding project

---

## 🛠️ Choose One Project
### 🔹 Option A — Python Network Scanner  
- Scan IP range  
- Detect open ports  
- Save to JSON  

### 🔹 Option B — Log Analyzer  
- Parse logs  
- Detect failed logins  
- Highlight anomalies  

### 🔹 Option C — Simple Security Dashboard  
- Show processes  
- Network connections  
- System info  

Create folder: /projects/day30-mini-project/

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Which project did you pick?  
2. What did you learn?  
3. What errors did you fix?  
4. How does your tool help security?  
5. What will you upgrade?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add a GUI or web interface.
"""
})

day_templates.update({

    31: """# 📘 Day 31 — Python for Automation (Advanced)

## 🎯 Goals
- Expand automation skills
- Learn advanced Python modules for productivity

## 📚 Learning
- Automate the Boring Stuff (Chapters 10–12)  
  https://automatetheboringstuff.com/

---

## 🛠️ Tasks
Create scripts:
- pdf_renamer.py  
- excel_merger.py  
- email_sender.py  

Practice with:
- os  
- shutil  
- smtplib  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What does shutil do?  
2. What is smtplib used for?  
3. How to loop through files?  
4. What is an exception?  
5. Write a try/except example.

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Create a CLI “task automation menu” app.
""",

    32: """# 📘 Day 32 — Web Development Basics (HTML/CSS)

## 🎯 Goals
- Learn how websites are structured
- Understand HTML/CSS fundamentals

## 📚 Learning
- freeCodeCamp HTML/CSS  
  https://www.freecodecamp.org/learn/2022/responsive-web-design/

---

## 🛠️ Tasks
Build:
- index.html  
- style.css  
- Create a personal homepage  

Topics:
- Tags  
- Elements  
- Classes  
- IDs  
- Flexbox  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is HTML?  
2. What is CSS?  
3. What does `<div>` do?  
4. Class vs ID?  
5. How does flexbox work?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Make your homepage responsive.
""",

    33: """# 📘 Day 33 — JavaScript DOM Manipulation

## 🎯 Goals
- Learn how JS interacts with HTML
- Modify DOM elements dynamically

## 📚 Learning
MDN - DOM Guide  
https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model

---

## 🛠️ Tasks
Create:
- dom_practice.js  
- Build a to-do list in HTML/CSS/JS  

Learn:
- querySelector  
- addEventListener  
- innerText / innerHTML  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is the DOM?  
2. What is an event listener?  
3. Difference between innerText and innerHTML?  
4. How do you select an element?  
5. How does DOM manipulation make dynamic pages?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add localStorage to your to-do app.
""",

    34: """# 📘 Day 34 — Flask API Development

## 🎯 Goals
- Learn backend fundamentals
- Build a simple Python API

## 📚 Learning
Flask Mega Tutorial (Free)  
https://flask.palletsprojects.com/

---

## 🛠️ Tasks
Create:
- app.py  
- routes for /hello, /sum, /info  
- Use JSON responses  
- Test using Postman  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a route?  
2. How do you return JSON?  
3. What is an API?  
4. What is a GET vs POST?  
5. Why use Postman?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add input validation + error handling.
""",

    35: """# 📘 Day 35 — Node.js Backend Basics

## 🎯 Goals
- Learn Express.js
- Build a simple Node-based API

## 📚 Learning
Express.js Guide  
https://expressjs.com/

---

## 🛠️ Tasks
Create:
- server.js  
- Routes:
  /ping  
  /user  
  /time  

Install:
- express  
- nodemon  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is Express.js?  
2. What does npm init do?  
3. Why use nodemon?  
4. What is middleware?  
5. JSON response example?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a basic CRUD system.
""",

    36: """# 📘 Day 36 — Databases (SQL)

## 🎯 Goals
- Learn SQL basics
- Use SQLite or MySQL

## 📚 Learning
SQLBolt  
https://sqlbolt.com/

---

## 🛠️ Tasks
Practice:
- SELECT  
- INSERT  
- UPDATE  
- DELETE  
- WHERE  
- JOIN  

Create:
- database_practice.sql  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is SQL?  
2. Difference between table & row?  
3. What is a join?  
4. Write a SELECT with WHERE.  
5. Write an INSERT query.

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a mini “User DB” with 3 tables.
""",

    37: """# 📘 Day 37 — Databases (NoSQL + MongoDB)

## 🎯 Goals
- Understand NoSQL vs SQL
- Learn MongoDB basics

## 📚 Learning
MongoDB University Free Courses  
https://learn.mongodb.com/

---

## 🛠️ Tasks
Learn:
- Documents  
- Collections  
- Queries  

Create:
- mongo_practice.js  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. SQL vs NoSQL difference?  
2. What is a document?  
3. What is a collection?  
4. Write one MongoDB query.  
5. Use-case for NoSQL?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a Node API connected to MongoDB.
""",

    38: """# 📘 Day 38 — Docker Basics

## 🎯 Goals
- Learn containerization
- Run your first Docker apps

## 📚 Learning
Docker Docs:  
https://docs.docker.com/get-started/

---

## 🛠️ Tasks
- Install Docker  
- Build Dockerfile for Python app  
- Run container  
- Explore:
  - docker ps  
  - docker images  
  - docker build  

Create:
docker-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is Docker?  
2. What is a container?  
3. What is an image?  
4. Role of Dockerfile?  
5. Difference between VM and container?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Containerize your Flask API.
""",

    39: """# 📘 Day 39 — Kubernetes Basics

## 🎯 Goals
- Understand orchestration concepts
- Learn K8s components

## 📚 Learning
Kubernetes Docs  
https://kubernetes.io/docs/home/

---

## 🛠️ Tasks
Learn:
- Pods  
- Deployments  
- Services  
- Nodes  

Document:
kubernetes-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is K8s?  
2. What is a Pod?  
3. What is a Deployment?  
4. What is a Node?  
5. Why use Kubernetes?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Install Minikube & deploy a pod.
""",

    40: """# 📘 Day 40 — Cloud (AWS Essentials)

## 🎯 Goals
- Learn basics of AWS Cloud platform

## 📚 Learning
AWS Cloud Practitioner Essentials (FREE)  
https://www.aws.training/Details/Curriculum?id=20685

---

## 🛠️ Tasks
Study:
- EC2  
- S3  
- IAM  

Create:
aws-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is EC2?  
2. What is S3?  
3. What is IAM?  
4. What is a region?  
5. Why use cloud computing?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Deploy a static website on S3.
""",

    41: """# 📘 Day 41 — Cloud (Azure Basics)

## 🎯 Goals
- Understand Microsoft Azure fundamentals

## 📚 Learning
Microsoft Learn — Azure Fundamentals  
https://learn.microsoft.com/en-au/training/paths/az-900-describe-cloud-concepts/

---

## 🛠️ Tasks
Study:
- Azure VMs  
- Blob Storage  
- VNets  

Write: azure-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is Azure VM?  
2. What is a VNet?  
3. Blob Storage use-case?  
4. Azure vs AWS?  
5. Why choose multi-cloud?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Create a free Azure VM.
""",

    42: """# 📘 Day 42 — Cybersecurity: Windows Internals

## 🎯 Goals
- Understand Windows system architecture
- Learn processes, registries, logs

## 📚 Learning
Windows Internals Book (FREE Chapters)  
Sysinternals Docs  
https://learn.microsoft.com/en-us/sysinternals/

---

## 🛠️ Tasks
Study:
- Processes  
- Services  
- Registry  
- Event Logs  

Tools:
- Process Explorer  
- Autoruns  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is the registry?  
2. What is svchost?  
3. What is a Windows Event Log?  
4. What is a service?  
5. Why use Sysinternals tools?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Monitor suspicious processes manually.
""",

    43: """# 📘 Day 43 — Malware Analysis Basics

## 🎯 Goals
- Understand *static* malware analysis fundamentals
- NO real malware — safe samples only

## 📚 Learning
Malware Unicorn PDF  
https://malwareunicorn.org/

---

## 🛠️ Tasks
Learn:
- Hashing (SHA256)  
- Strings analysis  
- File metadata  
- PE structure  

Use tools:
- strings  
- peid  
- hashcalc  

Write: malware-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is static analysis?  
2. What is a hash?  
3. What is PE file?  
4. What can “strings” reveal?  
5. Why NEVER run live malware?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Analyze a benign sample from Malware Traffic Analysis.
""",

    44: """# 📘 Day 44 — Cyber Defense: SOC Fundamentals

## 🎯 Goals
- Learn how Security Operations Centers work
- Understand detection & monitoring

## 📚 Learning
Blue Team Level 1 Roadmap  
https://securityblue.team/

---

## 🛠️ Tasks
Study:
- SIEM  
- Alerts  
- Indicators of Compromise  
- Incident Response  

Write: soc-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a SIEM?  
2. What is alert fatigue?  
3. What is an IOC?  
4. Stages of IR?  
5. Why SOC analysts need scripting?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Install Wazuh and generate sample events.
""",

    45: """# 📘 Day 45 — Midway Review + Build a SOC Tool

## 🎯 Goals
- Combine scripting, networking, and detection skills
- Build a real blue-team tool

---

## 🛠️ Mini Project Options

### 🔹 Option A — Log Parsing & Alert Tool  
- Parse logs  
- Detect anomalies  
- Output alerts  

### 🔹 Option B — Basic SIEM Dashboard (Python)  
- Read log files  
- Visualize events  
- Show top sources  

### 🔹 Option C — Network Connection Monitor  
- Show open ports  
- List active connections  
- Alert on suspicious ones  

Create folder: /projects/day45-soc-tool/

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What did I build?  
2. What techniques did it use?  
3. What detections did I add?  
4. What could be improved?  
5. Does this reflect SOC-style work?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add real-time monitoring features.
"""
})
day_templates.update({

    46: """# 📘 Day 46 — Applied Cryptography (Basics)

## 🎯 Goals
- Understand how encryption works
- Learn fundamentals of symmetric & asymmetric crypto

## 📚 Learning
Crypto 101 (Free)  
https://crypto101.io/

---

## 🛠️ Tasks
Study:
- Hashing vs Encryption  
- Symmetric Key Crypto  
- Public/Private Keys  
- TLS basics  

Write:
- crypto-notes.md  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is hashing used for?  
2. AES = symmetric or asymmetric?  
3. What is RSA?  
4. What is TLS?  
5. What is digital signing?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Use Python's hashlib to hash text.
""",

    47: """# 📘 Day 47 — Applied Cryptography (Hands-On)

## 🎯 Goals
- Apply cryptographic functions using Python

## 📚 Learning
Python cryptography library  
https://cryptography.io/

---

## 🛠️ Tasks
Create scripts:
- hash_file.py  
- encrypt.py  
- decrypt.py  

Learn:
- Fernet keys  
- Hashing algorithms  
- Secure random  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a key?  
2. What is salt?  
3. What is nonce?  
4. Why is crypto hard to “make yourself”?  
5. What is key rotation?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a “secure notes” encrypted file system.
""",

    48: """# 📘 Day 48 — Cybersecurity Red Team: Enumeration

## 🎯 Goals
- Improve offensive recon skills
- Practice safe enumeration techniques

## 📚 Learning
TryHackMe — Red Teaming Fundamentals  
https://tryhackme.com/

---

## 🛠️ Tasks
Use:
- nmap (advanced flags)  
- enum4linux  
- smbmap  
- nikto  

Document items in:
- enumeration-notes.md  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is enumeration?  
2. What is SMB?  
3. What is an attack surface?  
4. Why enumerate before exploitation?  
5. What is service fingerprinting?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Create a custom Python enumeration script.
""",

    49: """# 📘 Day 49 — Vulnerability Scanning

## 🎯 Goals
- Learn about vulnerability scanning tools
- Understand CVEs, scoring, and scanning logic

## 📚 Learning
- Nessus Essentials (FREE)  
https://www.tenable.com/products/nessus/nessus-essentials

---

## 🛠️ Tasks
- Install Nessus Essentials  
- Scan your isolated network  
- Analyze:
  - CVSS scores  
  - Vulnerability categories  

Write: vuln-scan-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a vulnerability?  
2. What is CVE?  
3. What is CVSS score?  
4. What is a false positive?  
5. Difference between scanner & pentesting?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Export results and create a report.
""",

    50: """# 📘 Day 50 — Exploitation Basics (Safe Practice)

## 🎯 Goals
- Learn how exploits work at a conceptual level
- Practice ONLY inside safe labs

## 📚 Learning
TryHackMe — Metasploit Introduction  
https://tryhackme.com/

---

## 🛠️ Tasks
Practice:
- msfconsole basics  
- search, use, set  
- auxiliary scanning  
- exploit simulation  

Write: metasploit-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is Metasploit?  
2. What is an exploit?  
3. What is payload?  
4. What is a session?  
5. Why use labs, not real targets?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a Metasploit automation script.
""",

    51: """# 📘 Day 51 — Detection Engineering Intro

## 🎯 Goals
- Learn core detection logic
- Understand indicators, logs & signatures

## 📚 Learning
Sigma Rules  
https://sigmahq.io/

Elastic Detection Rules  
https://www.elastic.co/guide/en/security/current/detections-ui-overview.html

---

## 🛠️ Tasks
- Study detection logic  
- Analyze:
  - Authentication failures  
  - Suspicious process starts  
- Write beginner Sigma-like rules in:
  detection-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is detection engineering?  
2. What is a signature?  
3. What are IOCs?  
4. What logs matter in Windows?  
5. Why behavior > signature?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build your own simple log signature matcher.
""",

    52: """# 📘 Day 52 — Log Analysis (SIEM Simulation)

## 🎯 Goals
- Learn how to analyze logs
- Practice detection mindset

## 📚 Learning
Splunk Boss of the SOC (Free samples)  
https://bots.splunk.com/

---

## 🛠️ Tasks
Analyze:
- Web logs  
- Auth logs  
- Network events  

Find:
- Failed logins  
- Suspicious requests  
- Spike anomalies  

Write:
log-analysis-day52.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a SIEM?  
2. Why correlate events?  
3. What is an anomaly?  
4. What is log normalization?  
5. What is event forwarding?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a Python script to highlight anomalies.
""",

    53: """# 📘 Day 53 — Blue Team Tooling: Wazuh

## 🎯 Goals
- Learn how Wazuh works as an open-source SIEM
- Understand agents, dashboards, and alerts

## 📚 Learning
Wazuh Documentation  
https://documentation.wazuh.com/

---

## 🛠️ Tasks
- Install Wazuh Manager (or review cloud demo)
- Add one VM as an agent  
- Trigger:
  - File modification events  
  - Authentication failures  

Write: wazuh-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is Wazuh?  
2. What is an agent?  
3. What does FIM mean?  
4. What is an alert rule?  
5. Why central logging?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build your own event generator script.
""",

    54: """# 📘 Day 54 — Memory Forensics Introduction

## 🎯 Goals
- Learn how RAM forensics works
- Practice with Volatility (safe samples)

## 📚 Learning
Volatility Wiki  
https://volatilityfoundation.org/

---

## 🛠️ Tasks
Perform on *safe sample*:
- imageinfo  
- pslist  
- netscan  
- dlllist  

Write: memory-forensics-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is memory forensics?  
2. What can pslist reveal?  
3. What is netscan?  
4. Why analyze volatile memory?  
5. What is a memory dump?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Attempt a basic rootkit detection.
""",

    55: """# 📘 Day 55 — Python Project: Log Analyzer v2

## 🎯 Goals
- Build a more advanced automated log-analysis tool

---

## 🛠️ Tasks
Features:
- Detect brute-force attempts  
- Detect anomalies  
- Visualize results (matplotlib)  

Create folder: /projects/log-analyzer-v2/

Files:
- analyzer.py  
- patterns.json  
- results.json  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What pattern did you detect?  
2. Why JSON for rules?  
3. How did you visualize data?  
4. What improvements next?  
5. What logs did you use?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add real-time monitoring.
""",

    56: """# 📘 Day 56 — Network Monitoring Tools

## 🎯 Goals
- Learn live network monitoring
- Understand visibility tools

## 📚 Learning
Tools:
- iftop  
- tcpdump  
- ntop  
- Wireshark live  

---

## 🛠️ Tasks
Capture:
- Live packets  
- DNS traffic  
- HTTP headers  

Document:
network-monitoring-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is tcpdump?  
2. What is a pcap?  
3. What is packet filtering?  
4. How to read traffic safely?  
5. What is network visibility?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a tcpdump wrapper script (Python).
""",

    57: """# 📘 Day 57 — Identity & Access Management (IAM)

## 🎯 Goals
- Learn IAM concepts
- Understand authentication systems

## 📚 Learning
Auth0 Documentation  
https://auth0.com/docs

---

## 🛠️ Tasks
Study:
- MFA  
- RBAC  
- OAuth2 flow  
- JWTs  

Write:
iam-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is RBAC?  
2. What is MFA?  
3. What is OAuth2?  
4. What is JWT?  
5. Why identity is “new perimeter”?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build simple JWT validator in Python.
""",

    58: """# 📘 Day 58 — Secure Network Architecture

## 🎯 Goals
- Learn how secure environments are designed
- Understand segmentation, DMZs, firewalls

## 📚 Learning
Cisco SAFE Blueprint (Free PDFs)

---

## 🛠️ Tasks
Study:
- DMZ architecture  
- Firewalls  
- Segmentation  
- VLANs  
- VPNs  

Create: network-architecture-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is segmentation?  
2. What is a DMZ?  
3. Stateful vs stateless firewall?  
4. What is a VPN?  
5. Why use zero trust?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Design a secure network diagram.
""",

    59: """# 📘 Day 59 — Infrastructure as Code (Terraform)

## 🎯 Goals
- Learn provisioning automation
- Understand IaC principles

## 📚 Learning
Terraform Documentation  
https://developer.hashicorp.com/terraform/docs

---

## 🛠️ Tasks
Learn:
- providers  
- variables  
- resources  

Create:
terraform-example/main.tf

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is IaC?  
2. What is Terraform used for?  
3. What is a provider?  
4. What is a resource?  
5. Why version-control infrastructure?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Deploy S3 bucket using Terraform.
""",

    60: """# 📘 Day 60 — Mid-Phase Project (Cyber + Cloud)

## 🎯 Goals
- Build a large combined project using skills from Days 46–60

---

## 🛠️ Project Options

### 🔹 Option A — Cloud-Based Log Collection System  
- Collect logs from VM  
- Store in cloud DB  
- Analyze using Python  

### 🔹 Option B — Encrypted File Transfer Tool  
- Use AES/RSA  
- Verification via hashing  

### 🔹 Option C — Live Network Monitor Dashboard  
- Collect network stats  
- Build dashboard (Flask or Node)  

Create folder: /projects/day60-final/

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What project did you build?  
2. What skills combined?  
3. Hardest part?  
4. What to add next?  
5. Could this be portfolio-ready?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add authentication to your project.
"""
})
day_templates.update({

    61: """# 📘 Day 61 — DevOps Foundations

## 🎯 Goals
- Learn the fundamentals of DevOps
- Understand CI/CD, pipelines, and automation workflows

## 📚 Learning
Azure DevOps + GitHub Actions Docs  
https://learn.microsoft.com/en-us/devops/  
https://docs.github.com/en/actions

---

## 🛠️ Tasks
Study:
- CI vs CD  
- Automated testing  
- Deployment workflows  

Create:
devops-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is CI?  
2. What is CD?  
3. Why automate deployments?  
4. What is GitHub Actions?  
5. Example CI workflow?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Create a CI workflow file in any of your repos.
""",

    62: """# 📘 Day 62 — GitHub Actions Hands-On

## 🎯 Goals
- Build your first automated workflow
- Understand YAML automation logic

## 📚 Learning
GitHub Actions Starter Workflows  
https://docs.github.com/en/actions/using-workflows

---

## 🛠️ Tasks
Create:
- .github/workflows/python-tests.yml  
- Run automated Python tests  

Learn:
- triggers  
- jobs  
- steps  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a workflow?  
2. What is a trigger?  
3. What is a job?  
4. Why automate tests?  
5. How do actions improve collaboration?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add linting to your workflow.
""",

    63: """# 📘 Day 63 — Containers + CI/CD Integration

## 🎯 Goals
- Integrate Docker + GitHub Actions
- Build and push a container image automatically

## 📚 Learning
GitHub Actions + Docker Docs

---

## 🛠️ Tasks
- Create Dockerfile  
- Create workflow for:
  - build image  
  - push to container registry (GHCR)  

Write:
docker-ci-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Why containerize applications?  
2. What is GHCR?  
3. What does docker build do?  
4. What does docker push do?  
5. Why combine CI with containers?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add vulnerability scanning to CI pipeline.
""",

    64: """# 📘 Day 64 — Infrastructure as Code (Terraform Advanced)

## 🎯 Goals
- Work with Terraform provisioning automation
- Build multiple resources as a single module

## 📚 Learning
Terraform Modules Guide  
https://developer.hashicorp.com/terraform/language/modules

---

## 🛠️ Tasks
- Create Terraform module:
  - network.tf  
  - instance.tf  
  - outputs.tf  

- Deploy small infrastructure setup (VM + network)

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a module?  
2. What are outputs?  
3. What is terraform init used for?  
4. What is terraform plan?  
5. Why use IaC in security?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Create an S3 + CloudFront module.
""",

    65: """# 📘 Day 65 — Cloud Security Best Practices

## 🎯 Goals
- Understand how to secure cloud environments
- Learn IAM, networking, and storage protection

## 📚 Learning
AWS Security Best Practices  
https://docs.aws.amazon.com/whitepapers/latest/security-best-practices/

---

## 🛠️ Tasks
Study:
- IAM hardening  
- MFA Everywhere  
- Bucket policies  
- Network ACLs  
- Security Groups  

Write: cloud-security-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Difference between SG and NACL?  
2. What is least privilege?  
3. Why encrypt S3 buckets?  
4. What is an IAM role?  
5. Why cloud auditing matters?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Configure a secure S3 bucket with bucket policy + encryption.
""",

    66: """# 📘 Day 66 — Serverless Computing (AWS Lambda)

## 🎯 Goals
- Learn how serverless works
- Deploy your first Lambda function

## 📚 Learning
AWS Lambda Docs  
https://docs.aws.amazon.com/lambda/

---

## 🛠️ Tasks
Create:
- lambda_handler.py  
- IAM role for Lambda  
- Deploy via console or CLI  

Write:
serverless-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is serverless?  
2. What triggers a Lambda?  
3. What languages can Lambda run?  
4. Why serverless for security?  
5. What are cold starts?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add API Gateway → Lambda → DynamoDB workflow.
""",

    67: """# 📘 Day 67 — API Security (OWASP)

## 🎯 Goals
- Learn API-focused vulnerabilities
- Understand how to secure endpoints

## 📚 Learning
OWASP API Top 10  
https://owasp.org/API-Security/

---

## 🛠️ Tasks
Study:
- API1: Broken Object Level Auth  
- API5: Broken Function Level Auth  
- API7: Rate Limiting  
- API8: Injection  

Write:
api-security-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is BOLA?  
2. Why rate-limit APIs?  
3. What is token-based auth?  
4. What is parameter tampering?  
5. What is API schema validation?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Secure one of your earlier APIs using JWT.
""",

    68: """# 📘 Day 68 — Web App Pentesting Basics

## 🎯 Goals
- Learn web exploitation basics
- Practice safe web hacking in labs

## 📚 Learning
PortSwigger Web Security Academy  
https://portswigger.net/web-security

---

## 🛠️ Tasks
Do labs:
- SQL Injection  
- Authentication bypass  
- Broken access control  

Write:
web-pentest-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is SQLi?  
2. What is access control?  
3. Why brute force can work?  
4. What is session fixation?  
5. What is input sanitization?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Try “Blind SQL injection with timing”.
""",

    69: """# 📘 Day 69 — JavaScript Security

## 🎯 Goals
- Learn secure JS coding
- Understand frontend attack surface

## 📚 Learning
OWASP JavaScript Security Guide

---

## 🛠️ Tasks
Study:
- XSS  
- DOM-based injection  
- CSP (Content Security Policy)  

Write:
js-security-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is DOM XSS?  
2. What is CSP?  
3. Why sanitize output?  
4. What is eval() danger?  
5. What is a JS gadget?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Implement CSP in your earlier JS project.
""",

    70: """# 📘 Day 70 — Python Secure Coding

## 🎯 Goals
- Improve code quality & hardening
- Understand Python-specific security flaws

## 📚 Learning
Bandit (Python Security Scanner)  
https://bandit.readthedocs.io/

---

## 🛠️ Tasks
- Install Bandit  
- Scan 3 old Python projects  
- Fix vulnerabilities  

Write:
python-secure-coding-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Why avoid eval()?  
2. What is subprocess injection?  
3. What is insecure deserialization?  
4. Why pin dependencies?  
5. What is Bandit used for?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add logging + validation to all scripts.
""",

    71: """# 📘 Day 71 — DevSecOps Overview

## 🎯 Goals
- Integrate security into DevOps workflows

## 📚 Learning
DevSecOps Playbook  
https://www.devsecops.org/

---

## 🛠️ Tasks
Study:
- Shift-left security  
- Automated scans  
- Secrets management  
- SAST vs DAST  

Write:
devsecops-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is shift-left security?  
2. SAST vs DAST?  
3. Why automate scanning?  
4. What are secrets?  
5. What is supply-chain risk?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add secrets detection scan to GitHub Actions.
""",

    72: """# 📘 Day 72 — Secrets Management

## 🎯 Goals
- Learn how to securely store sensitive information

## 📚 Learning
Hashicorp Vault  
https://developer.hashicorp.com/vault/docs

---

## 🛠️ Tasks
Study:
- Secret engines  
- K/V storage  
- Token authentication  

Write:
secrets-management-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Why never hardcode credentials?  
2. What is Vault?  
3. What is secret rotation?  
4. What is token auth?  
5. What is a lease?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a Python script that fetches secrets from Vault.
""",

    73: """# 📘 Day 73 — Threat Modeling

## 🎯 Goals
- Learn structured approach to identifying threats

## 📚 Learning
Microsoft STRIDE Model  
https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool

---

## 🛠️ Tasks
Perform threat model on one of your apps:
- Identify threats  
- Map to STRIDE  
- Document mitigations  

Write:
threat-model-day73.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What does STRIDE stand for?  
2. What is threat modeling?  
3. Why identify mitigations?  
4. What are data flows?  
5. What is trust boundary?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Draw a DFD diagram for your app.
""",

    74: """# 📘 Day 74 — Incident Response (IR) Basics

## 🎯 Goals
- Understand IR process, roles, documentation

## 📚 Learning
NIST Incident Response Guide  
https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

---

## 🛠️ Tasks
Study IR phases:
- Preparation  
- Detection  
- Containment  
- Eradication  
- Recovery  
- Post-incident lessons  

Write:
ir-basics-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Name 4 IR phases.  
2. Why preparation is essential?  
3. What is containment?  
4. What is IR documentation?  
5. Why perform post-incident review?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Write a mock IR report.
""",

    75: """# 📘 Day 75 — Build Incident Response Automation

## 🎯 Goals
- Build a Python/Node tool that automates IR triage tasks

---

## 🛠️ Project Ideas

### 🔹 Option A — Log Collector Tool  
- Collect logs from directories  
- Compress them  
- Hash outputs for integrity  

### 🔹 Option B — IOC Scanner  
- Scan directories  
- Match known IoCs  
- Provide alerts  

### 🔹 Option C — Process Anomaly Detector  
- List running processes  
- Identify suspicious ones  

Create folder:
projects/day75-incident-tool/

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What tool did you build?  
2. What IR phase does it help?  
3. What logic did it use?  
4. What can be added next?  
5. Could SOC analysts use this?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Add GUI or terminal menu system.
"""
})

day_templates.update({

    76: """# 📘 Day 76 — Security Automation with Python

## 🎯 Goals
- Learn how Python automates security tasks
- Build re-usable automation modules

## 📚 Learning
Automate Cybersecurity Tasks with Python  
(Free resources across SANS blogs, GitHub)

---

## 🛠️ Tasks
Write:
- log_parser.py  
- event_normalizer.py  
- alert_helper.py  

Use libraries:
- json  
- re  
- datetime  

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Why automate security tasks?  
2. What is normalization?  
3. Why use regex?  
4. What timestamp formats exist?  
5. What tasks did your script automate?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Connect your script to a webhook for alerting.
""",

    77: """# 📘 Day 77 — Bug Bounty Basics

## 🎯 Goals
- Learn how ethical bug bounty hunting works
- Study safe vulnerability reporting

## 📚 Learning
HackerOne 101  
https://www.hacker101.com/

---

## 🛠️ Tasks
Study:
- Recon approach  
- What makes a valid report  
- Scope, rules, disclosure policy  

Write: bugbounty-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is scope?  
2. What is responsible disclosure?  
3. What is an invalid report?  
4. Why screenshots matter?  
5. Why PoC quality is critical?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Attempt Hacker101 CTF levels.
""",

    78: """# 📘 Day 78 — Mobile Security Basics

## 🎯 Goals
- Understand mobile app attack surface
- Learn about Android/iOS security architecture

## 📚 Learning
OWASP Mobile Top 10  
https://owasp.org/www-project-mobile-top-10/

---

## 🛠️ Tasks
Study:
- M1 Improper Platform Usage  
- M3 Insecure Communication  
- M6 Insecure Authorization  

Write: mobile-security-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is APK?  
2. What is mobile sandboxing?  
3. What is MITM attack?  
4. What is certificate pinning?  
5. Benefits of mobile OS security model?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Decompile a benign APK and inspect code.
""",

    79: """# 📘 Day 79 — Reverse Engineering Fundamentals

## 🎯 Goals
- Learn how binaries work
- Understand reversing workflow (safe, simple samples)

## 📚 Learning
Beginner Reversing Guide  
Malware Unicorn  
https://malwareunicorn.org/

---

## 🛠️ Tasks
Use:
- Ghidra  
- strings  
- objdump  

Analyze:
- control flow  
- functions  
- imports  

Write: reverse-engineering-day79.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is disassembly?  
2. What are imports?  
3. What is control flow graph?  
4. What is symbol table?  
5. Why reverse engineering helps security?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Reverse a simple crackme.
""",

    80: """# 📘 Day 80 — Reverse Engineering (Intermediate)

## 🎯 Goals
- Analyze more complex programs
- Understand C code patterns in assembly

## 📚 Learning
Ghidra Tutorials on YouTube

---

## 🛠️ Tasks
Analyze:
- Conditionals  
- Loops  
- Common C idioms  

Identify:
- strcmp patterns  
- pointer arithmetic  
- memory access  

Write: reversing-intermediate-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. How do if/else appear in assembly?  
2. How to identify loops?  
3. What is stack frame?  
4. What is decompiler?  
5. Why understand calling conventions?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Patch a simple function to change program behavior.
""",

    81: """# 📘 Day 81 — OSINT (Open Source Intelligence)

## 🎯 Goals
- Learn information gathering from public sources
- Practice safe OSINT methodology

## 📚 Learning
OSINT Framework  
https://osintframework.com/

---

## 🛠️ Tasks
Perform:
- Username search  
- Domain lookup  
- Email analysis  

Tools:
- whois  
- hunter.io (free)  
- socialscan  

Write: osint-day81.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is OSINT?  
2. Why is passive recon important?  
3. What is WHOIS?  
4. Risks of OSINT?  
5. What tools did you use today?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Perform OSINT on one of your own domains or usernames.
""",

    82: """# 📘 Day 82 — Blockchain Security Basics

## 🎯 Goals
- Learn blockchain fundamentals
- Understand smart contract security risks

## 📚 Learning
CryptoZombies (Free)  
https://cryptozombies.io/

OWASP Smart Contract Security

---

## 🛠️ Tasks
Learn:
- Smart contracts basics  
- Blockchain immutability  
- Common vulnerabilities  

Write: blockchain-security-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is blockchain?  
2. What is a smart contract?  
3. What is reentrancy attack?  
4. Why is immutability risky?  
5. What is a consensus mechanism?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Write a basic Solidity contract on Remix IDE.
""",

    83: """# 📘 Day 83 — AI & ML Fundamentals (Security Focused)

## 🎯 Goals
- Learn how machine learning works
- Understand ML attack risks

## 📚 Learning
Google ML Crash Course  
https://developers.google.com/machine-learning/crash-course

---

## 🛠️ Tasks
Study:
- Training vs inference  
- Features, labels  
- Overfitting  

Write: ml-fundamentals-day83.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is training data?  
2. What is inference?  
3. What is overfitting?  
4. Why ML can be attacked?  
5. What is adversarial example?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Train a simple classifier using scikit-learn.
""",

    84: """# 📘 Day 84 — Applied AI Security

## 🎯 Goals
- Understand attacks on AI & LLMs
- Learn prompt injection, data poisoning, model extraction

## 📚 Learning
OWASP ML/LLM Security Top 10  
https://owasp.org/www-project-top-ten-for-large-language-model-applications/

---

## 🛠️ Tasks
Study:
- Prompt injection  
- Data poisoning  
- Insecure outputs  

Write:
ai-security-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is prompt injection?  
2. Why are LLMs vulnerable?  
3. What is model extraction?  
4. What is hallucination?  
5. How to protect LLM apps?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a hardened prompt wrapper function.
""",

    85: """# 📘 Day 85 — Threat Hunting Basics

## 🎯 Goals
- Learn proactive defense skills
- Understand threat hunting methodologies

## 📚 Learning
MITRE ATT&CK  
https://attack.mitre.org/

---

## 🛠️ Tasks
Study:
- ATT&CK matrix  
- Tactics vs Techniques  
- Mapping events to techniques  

Write: threat-hunting-day85.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is threat hunting?  
2. Difference between tactic & technique?  
3. Why hypothesis-driven hunts?  
4. What is ATT&CK used for?  
5. Example hunt idea?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Build a detection based on MITRE T1059.
""",

    86: """# 📘 Day 86 — Advanced Networking (Routing + Firewalls)

## 🎯 Goals
- Learn how routing works
- Understand firewall rules & ACL logic

## 📚 Learning
Cisco NetAcad Free Courses

---

## 🛠️ Tasks
Study:
- Static routing  
- Default routes  
- ACL structure  
- Stateful firewall behavior  

Write:
advanced-networking-notes.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What is a default route?  
2. What is ACL?  
3. Stateful vs stateless firewall?  
4. Why routing security matters?  
5. What is NAT?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Configure a pfSense VM with firewall rules.
""",

    87: """# 📘 Day 87 — Secure Coding Final Review (All Languages)

## 🎯 Goals
- Consolidate secure coding across Python, JS, Node, Bash

## 📚 Learning
OWASP Cheat Sheets  
https://cheatsheetseries.owasp.org/

---

## 🛠️ Tasks
Review:
- Input validation  
- Sanitization  
- Authentication  
- Error handling  

Write:
secure-coding-review.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Why sanitize input?  
2. Why avoid stack traces in production?  
3. What is supply-chain attack?  
4. What is dependency scanning?  
5. What are secrets?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Apply secure coding to ALL previous projects.
""",

    88: """# 📘 Day 88 — Portfolio Enhancement Day

## 🎯 Goals
- Polish GitHub
- Add documentation, screenshots, demos

---

## 🛠️ Tasks
- Update READMEs  
- Add screenshots  
- Add architecture diagrams  
- Write blog-style project explanations  

Write:
portfolio-upgrade-day88.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What project is strongest?  
2. What needs the most improvement?  
3. What skills shine the most?  
4. What is missing?  
5. Does your GitHub look professional?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Deploy a portfolio website.
""",

    89: """# 📘 Day 89 — Final Capstone Project (Planning)

## 🎯 Goals
- Plan your final 90-day capstone
- Combine coding + cyber + AI + cloud

---

## 🛠️ Project Ideas

### 🔹 Option A — AI-Augmented SOC Tool  
- Log ingestion  
- AI-assisted triage  
- Risk scoring  

### 🔹 Option B — Full Attack & Defense Lab  
- Red team chain  
- Blue team detection  
- Full report  

### 🔹 Option C — Cloud Security Automation  
- Cloud scanning  
- Misconfiguration detection  
- Reporting  

Write:
capstone-plan.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. Which capstone did you choose?  
2. What tech stack will you use?  
3. What cloud or local tools needed?  
4. What is your project timeline?  
5. Who is the “audience” of your project?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
-  

# ⭐ OPTIONAL STRETCH CHALLENGE
- Draft a full architecture diagram.
""",

    90: """# 🎓 Day 90 — Capstone Build & Graduation Day

## 🎯 Goals
- Complete your final 90-day project
- Package it into a professional portfolio piece

---

## 🛠️ Tasks
- Build project components  
- Document everything  
- Add demo video  
- Upload to GitHub  
- Write final README  
- Create LinkedIn post announcing completion  

Write: day90-final-summary.md

---

# ✍️ NOTES
-  

# 🧠 SELF-TEST QUESTIONS
1. What did you build?  
2. What skills did it showcase?  
3. What challenges did you overcome?  
4. What would you add with more time?  
5. Can you confidently speak about every part?

# 🚀 WHAT I BUILT TODAY
-  

# 📌 REFLECTION
- What was the biggest success?
- What surprised you the most?
- What did you enjoy most?

# ⭐ OPTIONAL STRETCH CHALLENGE
- Deploy your capstone publicly online.
"""
})

# ---------------------------
# WRITE TEMPLATES TO FILES
# ---------------------------

for day_num, template in day_templates.items():
    filename = f"day{day_num:02d}.md"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✓ Generated {filepath}")

print(f"\n✅ Successfully generated {len(day_templates)} day files in '{OUTPUT_FOLDER}' folder!")
