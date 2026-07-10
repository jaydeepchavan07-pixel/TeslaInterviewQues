# TeslaInterviewQues
# Hi there, I'm Jaydeep! 👋

Welcome to my GitHub profile. Here are some of my optimized algorithmic solutions:

### 🚀 Featured Code Implementations

<details>
<summary><b>1. Longest Substring Without Repeating Characters (Python)</b></summary>
    
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
Time Complexity: $O(n)$ using the Sliding Window technique.  
Space Complexity: $O(min(m, n))$ utilizing a Hash Map tracker.

#### Output - Longest Substring Without Repeating Characters (Python) 
<img width="707" height="125" alt="Longest Substring Without Repeating Characters (Python) Output" src="https://github.com/user-attachments/assets/66724820-f331-45db-86ad-281820e97511" />
</details>


