# String Mix Visualization

## Overview

This project implements a function to **visualize differences between two strings** based on the frequency of lowercase letters (`a` to `z`). The goal is to produce a summary string that shows which string has the higher occurrences of each letter.

---

## Problem Description

Given two strings `s1` and `s2`:

1. Only lowercase letters `a-z` are considered.
2. Count the frequency of each lowercase letter in both strings.
3. Consider only letters where the **maximum frequency** across both strings is **strictly greater than 1**.
4. For each relevant letter:
   - Prefix the letter sequence with `1:` if the maximum occurs in `s1`.
   - Prefix with `2:` if the maximum occurs in `s2`.
   - Prefix with `=:` if the maximum occurs in **both strings**.

5. Sort the resulting groups:
   - Descending order of substring length.
   - If lengths are equal, ascending lexicographic order (by letters and digits).

6. Join all groups with `/`.

---

## Examples

| s1 | s2 | Output |
|----|----|--------|
| `"A aaaa bb c"` | `"& aaa bbb c d"` | `"1:aaaa/2:bbb"` |
| `"my&friend&Paul has heavy hats! &"` | `"my friend John has many many friends &"` | `"2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"` |
| `"mmmmm m nnnnn y&friend&Paul has heavy hats! &"` | `"my frie n d Joh n has ma n y ma n y frie n ds n&"` | `"1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"` |
| `"Are the kids at home? aaaaa fffff"` | `"Yes they are here! aaaaa fffff"` | `"=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"` |

> Note: In Swift, R, and PowerShell, `=:` is replaced by `E:`.

---

## How It Works

1. Count lowercase letter frequency in `s1` and `s2`.
2. Determine the **maximum occurrence** for each letter.
3. Create a substring for each letter with its prefix (`1:`, `2:`, `=:`).
4. Sort substrings:
   - By length descending
   - By alphabetical order if lengths are equal
5. Join all substrings using `/`.

### Flow Diagram

```text
   +-------------------+
   |   Input Strings   |
   |       s1, s2      |
   +-------------------+
             |
             v
   +-------------------+
   | Count lowercase   |
   | letters frequency |
   +-------------------+
             |
             v
   +-------------------+
   | Compare maximum   |
   | occurrences       |
   +-------------------+
             |
             v
   +-------------------+
   | Generate substrings|
   |  with prefixes    |
   +-------------------+
             |
             v
   +-------------------+
   | Sort substrings   |
   | (length + lex)    |
   +-------------------+
             |
             v
   +-------------------+
   | Join with '/' and |
   |  return result    |
   +-------------------+

