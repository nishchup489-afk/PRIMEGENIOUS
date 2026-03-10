# Prime Genius

**Project Title:** Find Prime Factors of a Number
**Series:** #Project 4 of 100 Python Projects

---

## Live Preview

* Live App: [https://primegenious.onrender.com](https://primegenious.onrender.com)
* GitHub Repository: [https://github.com/nishchup489-afk/PRIMEGENIOUS](https://github.com/nishchup489-afk/PRIMEGENIOUS)
* CLI Version: [https://github.com/nishchup489-afk/PRIMEGENIOUS/blob/main/sample.py](https://github.com/nishchup489-afk/PRIMEGENIOUS/blob/main/sample.py)

---

## Stack Used

### CLI Version

* Pure Python

### Web Version

* FastAPI *(Flask can also be used)*
* Poetry *(you can also use venv)*
* TailwindCSS v4 (via browser CDN) *(vanilla CSS can also work)*
* Render for deployment

---

## Other Projects in the "100 Python Projects" Series

[https://github.com/nishchup489-afk/100-Python-Projects](https://github.com/nishchup489-afk/100-Python-Projects)

---

# Explanation

## Pure Theory

### Prime Numbers

Prime numbers are numbers that are **only divisible by 1 and the number itself**.

Examples:

```
2, 3, 5, 19, 73 ...
```

---

### Factors

Factors are **smaller numbers you multiply to get the original number**.

Example:

```
12 = 1 × 12
12 = 1 × 2 × 6
12 = 1 × 2 × 2 × 3
```

---

### Prime Factors

Prime factors are **factors that are prime numbers**.

Example:

```
12 = 1 × 2 × 6
```

This is **not prime factorization**, because **6 is not prime**.

So we divide 6 further:

```
12 = 1 × 2 × 2 × 3
```

Now every factor except 1 is prime.

So the **prime factors are:**

```
2, 2, 3
```

---

# Important Notes

* `1` is **not a prime number**
* The **smallest prime number is 2**, so we always start from 2
* Even numbers (except 2) are **never prime numbers**

Mathematical observation:

If

$$
c = a \times b
$$

Then at least one of the numbers must satisfy

$$
\sqrt{c} \ge a \quad \text{or} \quad \sqrt{c} \ge b
$$

This means we **only need to test factors up to the square root of the number**.

---

# How to Get Prime Factors (Math Process)

Suppose the number

```
n = 60
```

---

## Step 1

Keep dividing by the **smallest prime (2)** until it is no longer divisible.

```
60 / 2 = 30    → [2]
30 / 2 = 15    → [2, 2]
15 / 2 = ❌
```

---

## Step 2

Move to the **next prime (3)**.

```
15 / 3 = 5     → [2, 2, 3]
```

---

## Step 3 (Optional in small cases)

Check the square root limit.

```
√60 = 7.7459 ≈ 7
```

So all factors must be **≤ 7**.

---

## Step 4

Continue dividing.

```
5 / 5 = 1
```

Now the number becomes **1**, meaning the process stops.

Final prime factors:

```
[2, 2, 3, 5]
```

---

# Example 2

```
84
```

Limit:

```
√84 = 9.17 ≈ 9
```

---

### Step 1

```
84 / 2 = 42   → [2]
42 / 2 = 21   → [2, 2]
21 / 2 = ❌
```

---

### Step 2

```
21 / 3 = 7   → [2, 2, 3]
7 / 3 = ❌
```

---

### Step 3

```
7 / 5 = ❌
```

---

### Step 4

```
7 / 7 = 1   → [2, 2, 3, 7]
```

Prime factors:

```
[2, 2, 3, 7]
```

---

# Implementation Logic (In Code)

### Remember

To reduce unnecessary computation we **exclude many cases**.

Steps:

1. Take input and create a number list
2. Remove all numbers divisible by `2` and append `2`
3. Remove all numbers divisible by `3` and append `3` *(optional but efficient)*
4. Start iteration from next prime `i = 5`
5. Stop checking numbers larger than the square root

```
while i*i <= inp
```

6. Only divide when divisible

```
while inp % i == 0
```

7. Skip even numbers

```
i += 2
```

8. Finally if the remainder itself is prime

```python
if inp > 1:
    numbers.append(inp)
```

---

## CLI Version

Full CLI implementation:

[https://github.com/nishchup489-afk/PRIMEGENIOUS/blob/main/sample.py](https://github.com/nishchup489-afk/PRIMEGENIOUS/blob/main/sample.py)

---

## Need Help?

If you get stuck:

* Check the repository issues
* Revisit the logic explained above

Or contact:

**Email:** [nishchup489@gmail.com](mailto:nishchup489@gmail.com)

---

## Part of

**100 Python Projects Challenge** 🚀

Learning by building, one project at a time.
