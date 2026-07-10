# Hi there, I'm Jaydeep! 👋

<h1 align="center"># ⚡ Tesla Coding Interview Preparation Repository

> 🚀 A premium interview preparation repository containing Tesla coding questions with detailed explanations, dry runs, optimized solutions, and interview tips.

⭐ Python • Java • C# • DSA • System Design • Interview Prep</h1>

<p align="center">
Curated coding interview solutions with explanations, dry runs, complexity analysis, and interview tips.
</p>

<p align="center">
<img src="https://komarev.com/ghpvc/?username=jaydeepchavan07-pixel&color=blue"/>
</p>

## 📊 Repository Stats

| Metric | Value |
|:------|:------|
| ✅ Problems Solved | **1** |
| 📝 Languages | Python • Java • C# |
| 📚 Topics | DSA • Algorithms • System Design |
| 🎯 Target Companies | Tesla |

## 🎯 Why this Repository

This repository documents my journey solving coding interview problems commonly asked at Tesla.

Each solution includes:

- ✅ Problem Statement
- ✅ Optimal Solution
- ✅ Time Complexity
- ✅ Space Complexity
- ✅ Dry Run
- ✅ Interview Tips
- ✅ Related Problems
- ✅ LeetCode Link
- ✅ Output Screenshot

The goal is to build a high-quality interview preparation resource rather than simply collecting solutions.

## 🎯 Repository Goals

- Solve Tesla interview questions
- Write clean production-quality code
- Explain every algorithm
- Improve problem-solving skills
- Prepare for Software Engineer interviews

## 🧠 Techniques Covered

- Sliding Window
- Hash Map
- Two Pointers
- Dynamic Programming
- Binary Search
- Graph Algorithms
- Trees
- Greedy Algorithms
- Backtracking


## 📂 Repository Structure

```text
TeslaInterviewQues
│
├── Python
│   ├── Sliding_Window
│   │   ├── 001_LongestSubstringWithoutRepeatingCharacters.py
│   │   ├── 002_MinimumWindowSubstring.py
│   │   └── ...
│   │
│   ├── Arrays
│   ├── Trees
│   ├── Graphs
│   └── DP
│
├── Java
├── CSharp
├── Images
└── README.md
```

<p align="center">
<img src="https://komarev.com/ghpvc/?username=jaydeepchavan07-pixel&color=blue"/>
<img src="https://img.shields.io/github/stars/jaydeepchavan07-pixel/TeslaInterviewQues?style=social"/>
<img src="https://img.shields.io/github/last-commit/jaydeepchavan07-pixel/TeslaInterviewQues"/>
<img src="https://img.shields.io/github/repo-size/jaydeepchavan07-pixel/TeslaInterviewQues"/>
</p>

<p align="center">
<a href="Python/Sliding_Window/001_LongestSubstringWithoutRepeatingCharacters.py">
  <img src="https://img.shields.io/badge/Python-Solution-blue"/>
</a>
<img src="https://img.shields.io/badge/Difficulty-Medium-yellow"/>
<img src="https://img.shields.io/badge/Time-O(n)-green"/>
<img src="https://img.shields.io/badge/Space-O(min(m,n))-brightgreen"/>
</p>

## 🎯 Interview Preparation Roadmap

### Arrays & Strings
- [x] Longest Substring Without Repeating Characters
- [ ] Two Sum
- [ ] Group Anagrams

### Linked Lists
- [ ] Reverse Linked List

### Trees
- [ ] Binary Tree Level Order Traversal

### Graphs
- [ ] Number of Islands

### Dynamic Programming
- [ ] House Robber

### Greedy
- [ ] Jump Game

<p align="center">

<a href="#-progress">📈 Progress</a> •
<a href="#-table-of-contents">📚 Problems</a> •
<a href="#-upcoming-problems">🚀 Upcoming</a> •
<a href="#-author">👨‍💻 Author</a>

</p>

## 📈 Progress

| # | Problem | Solution | Difficulty | Status |
|---|---------|----------|------------|:------:|
| 1 | Longest Substring Without Repeating Characters | 🐍 [Python](Python/Sliding_Window/LongestSubstringWithoutRepeatingCharacters.py) | 🟨 Medium | ✅ |
| 2 | Two Sum | 🟩 Easy | ⏳ |
| 3 | Group Anagrams | 🟨 Medium | ⏳ |
| 4 | LRU Cache | 🟥 Hard | ⏳ |
| 5 | Merge Intervals | 🟨 Medium | ⏳ |

## 📊 Difficulty Distribution

| Difficulty | Count |
|------------|------:|
| 🟩 Easy | 0 |
| 🟨 Medium | 1 |
| 🟥 Hard | 0 |

## 📚 Table of Contents

- [1. Longest Substring Without Repeating Characters (Python)](#1-longest-substring-without-repeating-characters-python)
- [Upcoming Problems](#upcoming-problems)


## 1. Longest Substring Without Repeating Characters (Python)

<details>
<summary><b>Click to expand solution</b></summary>

### 📌 Problem Overview

| Property | Value |
|----------|-------|
| Problem | Longest Substring Without Repeating Characters |
| Original Problem | [LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Solution | [Python Solution](Python/Sliding_Window/LongestSubstringWithoutRepeatingCharacters.py) |
| Difficulty | 🟨 Medium |
| Topics | Sliding Window, Hash Map |

### 📝 Problem Statement

Given a string `s`, return the length of the **longest substring without repeating characters**.

A **substring** is a contiguous sequence of characters within the string.

The goal is to find the maximum length of a substring in which every character appears only once.

**Example**

```text
Input:  "aabcadb"
Output: 4

Explanation:
The longest substrings without repeating characters are:
"bcad"
"cadb"
```
### 💡 Approach

This solution uses the **Sliding Window** technique with a **Hash Map**.

- Maintain a window containing unique characters.
- Store the most recent index of each character.
- If a duplicate is found inside the current window, move the left pointer to exclude the duplicate.
- Update the maximum window size after processing each character.

This ensures that every character is processed only once, resulting in an **O(n)** time complexity.

### 🤔 Why Sliding Window?

A brute-force approach would generate every possible substring and check for duplicates, resulting in **O(n²)** or worse.

Using the **Sliding Window** technique, we maintain a window of unique characters and adjust its left boundary whenever a duplicate is encountered. Since each character is visited at most once by both pointers, the algorithm achieves an optimal **O(n)** time complexity.

---

### 💻 Optimal Python Solution

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        current_char = s[right]
        if current_char in char_map and char_map[current_char] >= left:
            left = char_map[current_char] + 1
            
        char_map[current_char] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length
``` 

#### 📸 Output Screenshot

<img width="707" height="125" alt="Longest Substring Without Repeating Characters (Python) Output" src="https://github.com/user-attachments/assets/66724820-f331-45db-86ad-281820e97511" />

#### ⏱️ Complexity Analysis

- **Time Complexity:** `O(n)` using the **Sliding Window** technique.
- **Space Complexity:** `O(min(m, n))` utilizing a **Hash Map** tracker.

---

#### 🔍 Detailed Walkthrough & Dry Run
**Example Input:** `"aabcadb"`

<details>
<summary><b>Click to expand the step-by-step dry run & complexity breakdown</b></summary>

#### Initial State

```python
char_map = {}
left = 0
max_length = 0
```

#### Step-by-Step Execution

| Right | Character | Duplicate Check | Map Update | Window Size | Max Length | Current Window |
|------:|:---------:|-----------------|------------|------------:|-----------:|---------------|
| 0 | 'a' | Not found | {'a': 0} | 1 | 1 | "a" |
| 1 | 'a' | Duplicate at 0 → left = 1 | {'a': 1} | 1 | 1 | "a" |
| 2 | 'b' | Not found | {'a': 1, 'b': 2} | 2 | 2 | "ab" |
| 3 | 'c' | Not found | {'a': 1, 'b': 2, 'c': 3} | 3 | 3 | "abc" |
| 4 | 'a' | Duplicate at 1 → left = 2 | {'a': 4, 'b': 2, 'c': 3} | 3 | 3 | "bca" |
| 5 | 'd' | Not found | {'a': 4, 'b': 2, 'c': 3, 'd': 5} | 4 | 4 | "bcad" |
| 6 | 'b' | Duplicate at 2 → left = 3 | {'a': 4, 'b': 6, 'c': 3, 'd': 5} | 4 | 4 | "cadb" |

#### Key Takeaways

- The **left pointer jumps instantly** to skip duplicates instead of moving one step at a time.
- The condition `char_map[current_char] >= left` ensures we only react to duplicates **inside the current window**.
- The longest substring length is **4**.
- Longest substrings are:
  - `bcad`
  - `cadb`

---

#### 🧠 Complexity Breakdown for Example Input `"aabcadb"`

#### ⏱️ Time Complexity: `O(n)`

- String length: **7**
- The loop executes exactly **7** iterations.
- Each iteration performs only constant-time hash map operations:
  - Lookup → `O(1)`
  - Update → `O(1)`
  - Pointer movement → `O(1)`
  - Maximum calculation → `O(1)`

Therefore, the total running time is **O(n)**.

#### 💾 Space Complexity: `O(min(m, n))`

For `"aabcadb"`:

- `n = 7`
- Unique characters `m = 4` (`a`, `b`, `c`, `d`)

The hash map stores at most **4** entries, so the auxiliary space is:

```text
O(min(4, 7)) = O(4)
```

which generalizes to:

```text
O(min(m, n))
```

#### 🎯 Interview Tips

- Explain why a brute-force solution is inefficient.
- Describe how the sliding window avoids revisiting characters.
- Mention that each character is processed at most once.
- Clearly justify the `O(n)` time complexity.

#### 📖 Related Problems

- LeetCode #76 – Minimum Window Substring
- LeetCode #159 – Longest Substring with At Most Two Distinct Characters
- LeetCode #340 – Longest Substring with At Most K Distinct Characters



</details>
</details>

## 🚀 Upcoming Problems

- [ ] Two Sum
- [ ] Group Anagrams
- [ ] LRU Cache
- [ ] Merge Intervals
- [ ] Word Ladder
- [ ] Serialize and Deserialize Binary Tree
- [ ] Median of Two Sorted Arrays

---

<p align="center">

⭐ If you find this repository useful, please consider giving it a star.

Made with ❤️ by Jaydeep Chavan

</p>

## 📄 License

This repository is licensed under the MIT License.

The solutions are provided for educational and interview preparation purposes.

## 🤝 Contributing

Suggestions and improvements are welcome. Feel free to open an issue or submit a pull request.

## 👨‍💻 Author

**Jaydeep Chavan**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Jaydeep%20Chavan-blue?logo=linkedin)](https://www.linkedin.com/in/jaydeep786)

[![GitHub](https://img.shields.io/badge/GitHub-jaydeepchavan07--pixel-black?logo=github)](https://github.com/jaydeepchavan07-pixel)