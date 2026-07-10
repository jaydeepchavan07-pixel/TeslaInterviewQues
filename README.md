# Hi there, I'm Jaydeep! 👋

<h1 align="center">⚡ Tesla Coding Interview Preparation Repository</h1>

<p align="center">
🚀 A premium interview preparation repository containing Tesla coding interview questions with optimized solutions, dry runs, explanations, and interview tips.
</p>

<p align="center">
⭐ Python • Java • C# • DSA • System Design • Interview Prep
</p>

<p align="center">
Curated coding interview solutions with explanations, dry runs, complexity analysis, and interview tips.
</p>

<p align="center">
<img src="https://komarev.com/ghpvc/?username=jaydeepchavan07-pixel&color=blue"/>
</p>

## 📊 Repository Stats

| Metric | Value |
|:------|:------|
| ✅ Problems Solved | **2** |
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
| 1 | Longest Substring Without Repeating Characters | 🐍 [Python](Python/Sliding_Window/001_LongestSubstringWithoutRepeatingCharacters.py) | 🟨 Medium | ✅ |
| 2 | Reorder Data in Log Files | 🐍 [Python](Python/Sorting/002_ReorderDataInLogFiles.py) | 🟨 Medium | ✅ |
| 3 | Group Anagrams | 🟨 Medium | ⏳ |
| 4 | LRU Cache | 🟥 Hard | ⏳ |
| 5 | Merge Intervals | 🟨 Medium | ⏳ |

## 📊 Difficulty Distribution

| Difficulty | Count |
|------------|------:|
| 🟩 Easy | 0 |
| 🟨 Medium | 2 |
| 🟥 Hard | 0 |

## 📚 Table of Contents

- [1. Longest Substring Without Repeating Characters (Python)](#1-longest-substring-without-repeating-characters-python)
- [2. Reorder Data in Log Files (Python)](#2-reorder-data-in-log-files-python)


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

#### ⚠️ Edge Cases

- Empty string
- Single character
- All identical characters
- All unique characters
- Unicode characters

#### 📖 Related Problems

- LeetCode #76 – Minimum Window Substring
- LeetCode #159 – Longest Substring with At Most Two Distinct Characters
- LeetCode #340 – Longest Substring with At Most K Distinct Characters

</details>
</details>

## 2. Reorder Data in Log Files (Python)

<details>
<summary><b>Click to expand solution</b></summary>

## 📌 Problem Overview

| Property | Value |
|----------|-------|
| Problem | Reorder Data in Log Files |
| Original Problem | [LeetCode #937](https://leetcode.com/problems/reorder-data-in-log-files/) |
| Solution | [Python Solution](Python/<Folder>/<FileName>.py) |
| Difficulty | 🟨 Medium |
| Topics | String, Sorting, Array |

---

## 📝 Problem Statement

You are given an array of logs, where each log is a space-delimited string with an identifier as the first word.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.

Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

All letter-logs come before all digit-logs.

The letter-logs are sorted lexicographically by their contents. If their contents are the same, sort them lexicographically by their identifiers.

The digit-logs maintain their relative ordering.

Return the final ordering of the logs.

### Example

```text
Input: logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
...

Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
...

Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs maintain their relative positions: "dig1 8 1 5 1" stays before "dig2 3 6".
...
```

---

## 💡 Approach

The core idea is to separate the logs into two streams based on their content type, apply a custom sorting mechanism to the letter-logs, and leave the digit-logs untouched to maintain stability.

Split & Classify: Iterate through the list of logs. Split each log at the very first space character to isolate the identifier from the content.

Character Filtering: Examine the first character of the content segment. If it is a numeric digit, append the log to a digit_logs list. Otherwise, append it to a letter_logs list.

Stable Custom Sort: Sort the letter_logs using Python's built-in Timsort algorithm by assigning a custom sorting key. The key returns a structural tuple (content, identifier). Python naturally processes tuple elements positionally—sorting by content first, and breaking ties with the identifier.

Concatenate: Merge the sorted letter_logs with the original-order digit_logs array.

Example:

- Use a Hash Map to store...
- Maintain two pointers...
- Update answer whenever...

---

## 🤔 Why This Approach?

Why brute force is slow: A generic sorting function trying to dynamically compare pairs of digit-logs vs letter-logs across all sorting boundaries introduces high runtime overhead and can easily break stable placement constraints if not implemented perfectly.

Why this algorithm is optimal: It cleanly maps the problem to standard Python infrastructure. Sorting only the letter-logs saves execution steps, while linear partitioning ensures that digit-logs are processed in an ideal $O(N)$ sweep without violating their absolute positions.

Why interviewer likes this approach: It tests clean manipulation of strings (split(..., maxsplit=1)) and evaluates a strong conceptual understanding of custom sorting metrics via key functions and compound tuple structures.

---

## 💻 Optimal <Language> Solution

```python

def reorderLogFiles(logs: list[str]) -> list[str]:
    letter_logs = []
    digit_logs = []
    
    # 1. Separate logs into respective containers
    for log in logs:
        # maxsplit=1 splits only at the first space instance
        identifier, content = log.split(" ", 1)
        
        if content[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)
            
    # 2. Sort letter_logs dynamically using a tuple key
    # (Primary Sort: Content, Secondary Sort: Identifier)
    letter_logs.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
    
    # 3. Concatenate and return complete list
    return letter_logs + digit_logs

test_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
result = reorderLogFiles(test_logs)
print("The input is:", test_logs)
print("The output is:", result)

```

---

## 📸 Output Screenshot

<img src="![alt text](002_ReorderDataInLogFiles.png)" width="700"/>

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|-----------|-------|
| Time | `$O(M \cdot N \log N)$` |
| Space | `$O(M \cdot N)$` |

---

## 🔍 Dry Run
<details>
<summary><b>Click to expand the step-by-step dry run & complexity breakdown</b></summary>
### Example Input

```text
logs = ["dig1 8 1", "let1 art", "let2 art"]
```

### Initial State

```python
letter_logs = []
digit_logs = []
```

### Step-by-Step Execution

| Step | Action | State | Result |
|------|--------|-------|--------|
|1|...|...|...|
|2|...|...|...|

---

## 🧠 Complexity Breakdown

### Time Complexity

The time complexity is $O(M \cdot N \log N)$, where $N$ represents the total number of logs, and $M$ marks the maximum length of a single log string. Partitioning the elements takes $O(M \cdot N)$ steps. Sorting the list of letter-logs performs $O(N \log N)$ structural string operations. Because string comparison operations depend directly on string length, comparing two strings scales up by a factor of $M$.

### Space Complexity

The space complexity settles at $O(M \cdot N)$. The algorithm requires auxiliary dynamic arrays (letter_logs and digit_logs) to host split-out elements, replicating the structure of the input space up to the total character content count.

---

## 🎯 Interview Tips

Mention brute force first: Confirm that handling both classification and stable sorting logic simultaneously within a single complex comparator can easily compromise relative layout requirements.

Explain optimization: Explicitly specify how Python's built-in Timsort behaves stably, making a simple divide-and-conquer tracking array approach bulletproof.

Mention edge cases: Validate conditions involving exact duplicate content text layers that trigger your identifier logic explicitly.

Discuss complexity before coding: Clearly outline how log text length boundaries influence operations during key string splitting functions.

---

## ⚠️ Edge Cases

Identical Content: Letter-logs with identical text contents correctly verify identifier fallback sorting keys.

Pure Digit/Letter Logs: Arrays holding entirely digit logs or exclusively letter logs loop correctly without empty exceptions.

Varying Word Counts: The string split implementation properly captures everything after the identifier, regardless of whitespace counts or string contents.

Single Log Present: Array elements under base parameters function smoothly.

---

## 📖 Related Problems

Merge Sorted Array

Custom Sort String

Sort Colors

---

## 🔗 Files

- 🐍 Python: `Python/<Folder>/<FileName>.py`

</details>


</details>

---


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