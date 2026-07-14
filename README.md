https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit?gid=1377915986#gid=1377915986

# Enhanced DSA Roadmap — 0–3 YOE AI Backend / GenAI Engineer

**Goal:** Clear coding rounds with the least possible time investment, by training _pattern recognition_ rather than memorizing individual problems. Every day now has a named pattern + 2 similar problems, so the same mental model gets reinforced 3x before you move on.

## How to use this sheet (read once)

- **Daily session stays 1 hour**: 10 min review yesterday → 40 min today's main problem → 10 min notes.
- **The 2 "Similar Practice" problems are not extra homework for today.** Do them on your weekly revision day, or whenever you have a spare 15–20 min (commute, break). They exist so the pattern gets touched 3 times, which is what actually moves it into long-term memory — not 3x the daily time.
- **Write the pattern name at the top of your notes**, not just the problem name. When you revise, you're revising "two-pointer shrinking window," not "Container With Most Water."
- Platform-agnostic: problem names below map 1:1 to LeetCode; use NeetCode's free explanations if you get stuck for >15 min, then come back and finish solving yourself.
- **If a day's main problem takes <40 min**, immediately do one Similar Practice problem in the leftover time instead of stopping early — that's the highest-ROI use of spare minutes in this whole plan.

### Difficulty pacing (unchanged, it's correct)

Days 1–20 Easy · Days 21–45 Easy-Medium · Days 46–75 Medium · Days 76+ Medium+ · No Hard problems until Phase 7 mocks.

---

# PHASE 1 — Foundations

## Week 1 — Arrays

| Day | Main Problem                        | Pattern                           | Similar Practice (do later)                                                                 |
| --- | ----------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------- |
| 1   | Linear Search / Find Max            | Single-pass traversal             | Find Minimum Element · Find the "missing number" in 1..n                                    |
| 2   | Second Largest Element              | Track top-2 in one pass           | Kth Largest by sorting (baseline, pre-heap) · Second Smallest Element                       |
| 3   | Remove Duplicates from Sorted Array | Two pointers (slow/fast)          | Remove Element · Remove Duplicates from Sorted Array II (allow 2 dupes)                     |
| 4   | Move Zeroes                         | Two pointers / in-place partition | Sort Colors (Dutch National Flag) · Segregate even/odd in-place                             |
| 5   | Best Time to Buy and Sell Stock     | Single-pass min-tracking          | Maximum Subarray (Kadane's — same "running best" instinct) · Best Time to Buy/Sell Stock II |
| 6   | Majority Element                    | Boyer–Moore voting                | Majority Element II (elements appearing > n/3) · Check if Array Is Monotonic                |
| 7   | **Revision**                        | —                                 | Re-solve Day 3 + Day 5 from scratch, untimed notes closed                                   |

**Pattern to internalize this week:** _"One pass, track a running value (max/min/count)."_ This single idea covers Days 1, 2, 5, 6.

---

## Week 2 — Hashing

| Day | Main Problem                      | Pattern                      | Similar Practice                                                                 |
| --- | --------------------------------- | ---------------------------- | -------------------------------------------------------------------------------- |
| 8   | Two Sum                           | Hashmap complement lookup    | Two Sum II (sorted input → two pointers instead) · Four Sum II                   |
| 9   | Contains Duplicate                | Hashset membership           | Contains Duplicate II (within distance k) · Ransom Note                          |
| 10  | Valid Anagram                     | Frequency counting           | Group Shifted Strings · Find the Difference                                      |
| 11  | Intersection of Two Arrays        | Hashset intersection         | Intersection of Two Arrays II (with duplicates) · Union of Two Arrays            |
| 12  | Top K Frequent Elements (concept) | Hashmap + sort/bucket sort   | Sort Characters by Frequency · K Closest Numbers to X                            |
| 13  | Longest Consecutive Sequence      | Hashset + sequence expansion | Missing Ranges · Longest Consecutive Sequence in a Binary Tree (optional, later) |
| 14  | **Revision**                      | —                            | Re-solve Day 8 + Day 13                                                          |

**Pattern to internalize:** _"Trade space for O(1) lookup."_ Any time you catch yourself writing a nested loop to check membership or count things — stop, reach for a hashmap/set.

---

# PHASE 2 — Pattern Recognition

## Week 3 — Strings

| Day | Main Problem              | Pattern                        | Similar Practice                                                                   |
| --- | ------------------------- | ------------------------------ | ---------------------------------------------------------------------------------- |
| 15  | Reverse String            | Two-pointer swap               | Reverse Vowels of a String · Reverse Words in a String                             |
| 16  | Valid Palindrome          | Two pointer + filtering        | Palindrome Number (no string conversion) · Valid Palindrome II (preview of Day 22) |
| 17  | Longest Common Prefix     | Vertical scanning              | Implement strStr() / indexOf · Add Strings                                         |
| 18  | Isomorphic Strings        | Bidirectional hashmap mapping  | Word Pattern · Is Subsequence                                                      |
| 19  | Group Anagrams            | Hashmap with sorted-string key | Find All Anagrams in a String · Group Shifted Strings (revisit)                    |
| 20  | Encode and Decode Strings | Length-prefix encoding         | String Compression · Count and Say                                                 |
| 21  | **Revision**              | —                              | Re-solve Day 16 + Day 19                                                           |

## Week 4 — Two Pointers

| Day | Main Problem              | Pattern                       | Similar Practice                                                     |
| --- | ------------------------- | ----------------------------- | -------------------------------------------------------------------- |
| 22  | Valid Palindrome II       | Two pointer, one skip allowed | Backspace String Compare · Palindromic Substrings (intro only)       |
| 23  | Container With Most Water | Greedy pointer-shrinking      | Trapping Rain Water (stretch, don't force it) · Boats to Save People |
| 24  | 3Sum                      | Sort + two pointer            | 3Sum Closest · 4Sum                                                  |
| 25  | **Revision**              | —                             | Re-solve Day 23 + Day 24                                             |

## Week 4 — Sliding Window

| Day | Main Problem                                   | Pattern                        | Similar Practice                                                                               |
| --- | ---------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------- |
| 26  | Maximum Average Subarray                       | Fixed-size window              | Maximum Sum Subarray of Size K · Minimum Size Subarray Sum                                     |
| 27  | Longest Substring Without Repeating Characters | Variable window + hashset      | Longest Substring with At Most K Distinct Characters · Longest Repeating Character Replacement |
| 28  | Permutation in String                          | Fixed window + frequency match | Find All Anagrams in a String (revisit from Day 19) · Minimum Window Substring (stretch)       |

**Pattern to internalize (Weeks 3–4):** _"Two ends moving toward or with each other."_ Every problem above is a variant of "shrink/expand a range and track something." This is the single highest-frequency interview pattern for 0–3 YOE roles — spend extra revision time here if any week gets cut short.

---

# PHASE 3 — Core Interview Patterns

## Week 5 — Binary Search

| Day | Main Problem                   | Pattern                        | Similar Practice                                                                                   |
| --- | ------------------------------ | ------------------------------ | -------------------------------------------------------------------------------------------------- |
| 29  | Binary Search                  | Classic BS                     | Sqrt(x) · Guess Number Higher or Lower                                                             |
| 30  | Search Insert Position         | Lower-bound BS                 | Find First and Last Position of Element in Sorted Array · Find Smallest Letter Greater Than Target |
| 31  | First Bad Version              | BS on a predicate/answer space | Find Peak Element · Capacity to Ship Packages Within D Days (stretch)                              |
| 32  | Search in Rotated Sorted Array | Modified BS                    | Search in Rotated Sorted Array II (with dupes) · Find Minimum in Rotated Sorted Array              |
| 33  | Koko Eating Bananas            | BS on answer space             | Minimum Number of Days to Make m Bouquets · Split Array Largest Sum (stretch)                      |

## Week 5 — Sorting

| Day | Main Problem    | Pattern                    | Similar Practice                                                                   |
| --- | --------------- | -------------------------- | ---------------------------------------------------------------------------------- |
| 34  | Merge Intervals | Sort + merge               | Insert Interval · Non-overlapping Intervals                                        |
| 35  | Meeting Rooms   | Interval sort / sweep line | Meeting Rooms II (needs min-heap, preview of Week 9) · Minimum Number of Platforms |

**Pattern to internalize:** _"If the array were sorted, this would be easy → sort it first, or binary-search on the answer itself."_ Days 31/33 (BS on answer) are the pattern most candidates never learn and it's a strong differentiator in interviews.

---

## Week 6 — Linked Lists

| Day | Main Problem             | Pattern                    | Similar Practice                                                             |
| --- | ------------------------ | -------------------------- | ---------------------------------------------------------------------------- |
| 36  | Reverse Linked List      | Iterative pointer reversal | Reverse Linked List II (partial reversal) · Swap Nodes in Pairs              |
| 37  | Middle of Linked List    | Slow/fast pointer          | Palindrome Linked List · Delete the Middle Node                              |
| 38  | Linked List Cycle        | Floyd's cycle detection    | Linked List Cycle II (find cycle start) · Happy Number (same trick, no list) |
| 39  | Merge Two Sorted Lists   | Two-pointer merge          | Sort List · Merge K Sorted Lists (stretch, previews heaps)                   |
| 40  | Remove Nth Node From End | Two pointers with a gap    | Remove Duplicates from Sorted List · Rotate List                             |

## Week 6 — Stack & Queue

| Day | Main Problem      | Pattern         | Similar Practice                                                |
| --- | ----------------- | --------------- | --------------------------------------------------------------- |
| 41  | Valid Parentheses | Stack matching  | Remove Outermost Parentheses · Baseball Game                    |
| 42  | Min Stack         | Auxiliary stack | Implement Queue using Stacks · Evaluate Reverse Polish Notation |

**Pattern to internalize:** _"Slow/fast pointers solve most linked-list problems without extra memory."_ Stack = "most recent unmatched thing" — recognize this whenever a problem mentions nesting, matching, or "undo."

---

# PHASE 4 — Tree Mastery

## Week 7 — Trees

| Day | Main Problem                 | Pattern                      | Similar Practice                                                        |
| --- | ---------------------------- | ---------------------------- | ----------------------------------------------------------------------- |
| 43  | Maximum Depth of Binary Tree | Recursive DFS                | Minimum Depth of Binary Tree · Balanced Binary Tree                     |
| 44  | Inorder Traversal            | Recursive/iterative DFS      | Iterative Inorder (with explicit stack) · Kth Smallest Element in a BST |
| 45  | Preorder Traversal           | DFS                          | Iterative Preorder · Binary Tree Paths                                  |
| 46  | Postorder Traversal          | DFS                          | Iterative Postorder · N-ary Tree Postorder Traversal                    |
| 47  | Same Tree                    | Recursive comparison         | Symmetric Tree · Subtree of Another Tree                                |
| 48  | Invert Binary Tree           | Recursive swap               | Symmetric Tree (revisit) · Flatten Binary Tree to Linked List (stretch) |
| 49  | Diameter of Binary Tree      | DFS with height + global max | Balanced Binary Tree (revisit) · Longest Univalue Path                  |

## Week 8 — BFS / DFS on Trees & Grids

| Day | Main Problem                      | Pattern              | Similar Practice                                                            |
| --- | --------------------------------- | -------------------- | --------------------------------------------------------------------------- |
| 50  | Binary Tree Level Order Traversal | BFS with queue       | Binary Tree Zigzag Level Order Traversal · Average of Levels in Binary Tree |
| 51  | Path Sum                          | DFS with running sum | Path Sum II (return all paths) · Sum Root to Leaf Numbers                   |
| 52  | Number of Islands                 | Grid DFS/BFS         | Max Area of Island · Surrounded Regions                                     |
| 53  | Flood Fill                        | Grid DFS             | Rotting Oranges (multi-source BFS — important variant) · Island Perimeter   |

**Pattern to internalize:** _"Every tree problem is DFS (go deep, use recursion) or BFS (go wide, use a queue). Pick DFS for path/depth questions, BFS for level/shortest-distance questions."_ Grid problems (Days 52–53) are just trees in disguise — same two tools.

---

# PHASE 5 — Advanced Interview Patterns

## Week 9 — Heap

| Day | Main Problem                              | Pattern                         | Similar Practice                                                                                               |
| --- | ----------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 54  | Kth Largest Element                       | Min-heap of size k              | Kth Smallest Element in a Sorted Matrix · Top K Frequent Words                                                 |
| 55  | Last Stone Weight                         | Max-heap simulation             | Reorganize String · Task Scheduler (stretch)                                                                   |
| 56  | Top K Frequent Elements (heap version)    | Hashmap + heap                  | K Closest Points to Origin · Sort Characters by Frequency (revisit — compare to Day 12's bucket-sort approach) |
| 57  | Find Median From Data Stream (study only) | Two heaps (max-heap + min-heap) | Sliding Window Median (stretch, study only — don't grind this)                                                 |
| 58  | **Revision**                              | —                               | Re-solve Day 54 + Day 56                                                                                       |

*Note: Day 12 and Day 56 are the same problem on purpose — first pass uses sort/bucket-sort (Week 2, before you know heaps), second pass uses a heap (now that you do). Comparing your two solutions side-by-side is a genuinely great exercise for understanding *why* heaps exist.*

---

## Week 10 — Graphs

| Day | Main Problem         | Pattern                              | Similar Practice                                                                                       |
| --- | -------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| 59  | Graph Representation | Adjacency list construction          | Build adjacency list from an edge list · Find the Town Judge (light graph modeling)                    |
| 60  | DFS Traversal        | Recursive/stack DFS                  | All Paths From Source to Target · Keys and Rooms                                                       |
| 61  | BFS Traversal        | Queue BFS                            | Shortest Path in Binary Matrix · Rotting Oranges (revisit)                                             |
| 62  | Number of Provinces  | Connected components                 | Number of Islands (revisit as a graph problem) · Number of Connected Components in an Undirected Graph |
| 63  | Clone Graph          | DFS/BFS + hashmap for visited copies | Copy List with Random Pointer (same "clone with mapping" idea) · Word Ladder (stretch)                 |
| 64  | Course Schedule      | Topological sort / cycle detection   | Course Schedule II (return the actual order) · Minimum Height Trees (stretch)                          |
| 65  | **Revision**         | —                                    | Re-solve Day 61 + Day 64                                                                               |

**Pattern to internalize:** _"Graphs = trees with cycles, so DFS/BFS still work — you just need a `visited` set to avoid infinite loops."_ Topological sort (Day 64) is the one genuinely new idea; it comes up in dependency-resolution style questions, which are common in backend/systems interviews.

---

# PHASE 6 — Just Enough DP

## Week 11 — Dynamic Programming

| Day | Main Problem             | Pattern                             | Similar Practice                                                                |
| --- | ------------------------ | ----------------------------------- | ------------------------------------------------------------------------------- |
| 66  | Climbing Stairs          | 1D DP / Fibonacci recurrence        | Fibonacci Number · N-th Tribonacci Number                                       |
| 67  | House Robber             | 1D DP with a take/skip choice       | House Robber II (circular array) · Delete and Earn (stretch)                    |
| 68  | Min Cost Climbing Stairs | 1D DP, minimize instead of maximize | Climbing Stairs (revisit, compare max-ways vs min-cost) · Paint Fence (stretch) |
| 69  | Coin Change              | Unbounded knapsack DP               | Coin Change II (count combinations, not min coins) · Perfect Squares            |
| 70  | **Revision**             | —                                   | Re-solve Day 67 + Day 69                                                        |

**Pattern to internalize:** _"DP = recursion + 'have I solved this exact subproblem before?'"_ At 0–3 YOE, being able to write the brute-force recursion and then add memoization is usually enough — full tabulation fluency is a stretch goal, not a requirement.

---

# PHASE 7 — Interview Simulation (Days 71–84)

Keep the alternating structure from the original plan — it's correct. One addition: on every **Mock** day, before you look at the answer, force yourself to say out loud which pattern you think it is ("this smells like sliding window because it's a substring + constraint"). That verbalization is what interviewers are actually grading.

| Day                        | Activity                                                                   |
| -------------------------- | -------------------------------------------------------------------------- |
| 71, 73, 75, 77, 79, 81, 83 | Mock interview (timed, one problem, explain out loud while solving)        |
| 72, 74, 76, 78, 80, 82, 84 | Revision: re-solve 2–3 previously-failed problems from your notes, untimed |

---

# Pattern Recognition Cheat Sheet

Use this during mocks and real interviews — read the problem, match the keyword, pick the tool.

| Signal in the problem                                 | Likely pattern                              |
| ----------------------------------------------------- | ------------------------------------------- |
| "sorted array"                                        | Binary search or two pointers               |
| "contiguous subarray/substring" + a constraint        | Sliding window                              |
| "pair/triplet that sums to X"                         | Two pointers (if sorted) or hashmap         |
| "find duplicate / has seen before"                    | Hashset                                     |
| "count frequency / most common"                       | Hashmap (+ heap or bucket sort for "top K") |
| "smallest/largest K elements"                         | Heap                                        |
| "minimize the maximum" / "maximize the minimum"       | Binary search on the answer                 |
| "tree" + "path" or "depth"                            | DFS                                         |
| "tree" or "grid" + "level" or "shortest distance"     | BFS                                         |
| "connected regions" in a grid                         | DFS/BFS flood fill                          |
| "dependency" / "order of tasks"                       | Topological sort                            |
| "cycle in a linked list"                              | Fast/slow pointers                          |
| "number of ways to do X" or "min/max cost to reach X" | Dynamic programming                         |
| "reverse", "swap in place", "next permutation"        | Two pointers, in-place manipulation         |
| "matching brackets/tags" or "undo last operation"     | Stack                                       |

---

# Expected Outcome

After ~70 core problems + ~140 similar-practice reps (done in spare minutes) + 2 weeks of mocks, you should comfortably handle:

- AI Backend Engineer interviews
- Python Backend Developer interviews
- GenAI Engineer interviews
- Startup Software Engineer interviews
- Most 0–3 YOE product-company coding rounds

**One honest caveat:** this plan maximizes _breadth of pattern recognition_, not depth on any single hard topic (no Hard-difficulty grinding, no advanced DP, no segment trees/tries). That's the correct tradeoff for a 1 hr/day, 0–3 YOE, AI-engineering-adjacent target — but if you're specifically targeting a company known for Hard-heavy rounds (some quant/big-tech teams), you'd want to extend Phase 7 by 2–3 weeks rather than compress this foundation.
