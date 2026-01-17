# AI Code Review Assignment (Python)

## Candidate
- Name:Martin Kiuna
- Approximate time spent:1 Hour 23 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function uses len(orders) as the divisor even though cancelled orders are excluded from the total resulting to an incorrect average.
- The function raises a zero-division-error when the imput list is empty.
- The function also returns invalid results when all orders are cancelled.

### Edge cases & risks
- Orders missing the status or amount keys will raise a KeyError.
- Non-numeric amount values will raise a TypeError or ValueError.
- An empty list or a list containing only cancelled orders is not handled safely.

### Code quality / design issues
- The function makes unsafe assumptions about the structure and validity of imput data.
- Business logic (excluding cancelled orders) is consistently applied between the numerator and the denomenator.
- No defensive programming is used to protect againist malformed imputs.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track only non-cancelled orders when calculting both the total and the count.
- Add a guard to prevent division by zero.
- Safely handle missing or invalid order data by skipping malformed entries.
- Convert amounts to float to ensure there is numeric consistency.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
If i was testing this function, I would focus on:
- An empty order list to ensure there is no division by zero.
- A list where all orders are cancelled.
- A mix of cancelled and uncancelled orders to verify the average is correct.
- Orders with missing keys or invalid amount values to confirm they are safely ignored.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Cancelled orders are still considered in the divisor.
- It does not mention failure modes such as empty imput or invalid order data.
- It overstates correctness and safety relative to actual implementation.

### Rewritten explanation
- This function calculates the average order value by summing the numeric amounts of all valid entries whose status is not "cancelled" and then dividing that total by the count of those non-cancelled orders. To ensure data integrity, any orders containing missing or invalid information are skipped during processing. If no valid orders are identified, the function returns 0.0 to prevent a division-by-zero error.

## 4) Final Judgment
- Decision: Request Changes.

- Justification: The original implementation produces incorrect averages, fails on common edge cases and is accompanied by a misleading explanation.

- Confidence & unknowns: High confidence in the indetified issues and fixes. Bussiness rules for handling zero valid orders could vary, but the chosen behaviour is safe and reasonable default.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The function trets the presence of "@" as sufficient for email validity, which is incorrect.
- The function can raise a TypeError when non-string values are present in the imput list.
- Multiple clearly invalid email formats are incorrectly counted as valid.

### Edge cases & risks
- Empty strings and malformed addresses such as "@", "user@" or "@domain.com" are counted as valid.
- Emails with multiple "@" characters are not rejected.
- Mixed-type imput is not handles safely.

### Code quality / design issues
- The function does not define or document wahat "valid" means.
- The implementation does not match the claims made in the explanation.
- Imput validation is insufficient for a function making correctness claims.

## 2) Proposed Fixes / Improvements
### Summary of changes
- validate thateach entry is a string before processing.
- Require exactly one "@" character.
- Ensure both local and domain parts are non-empty.
- Require the domain to contain atleast one dot.
- Safely ignore invalid and malformed entries.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
If I was testing this function, I would focus on:
- Empty imputs lists and lists containing only invalid entries.
- Mixed-type imputs including None and non-string values.
- Common invalid formats such as  missing local or domain parts.
- Clearly valid email addresses to ensure correct countin.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The function does not actually validate email addresses.
- It does not safely ignore invalid entries and can crash on non-string output.
-The explanation significantly overstates the correctness and robustness of the implementation.

### Rewritten explanation
- This function counts the number of valid email addresses in a provided list by applying a specific set of validation rules. To be considered valid, an entry must be a string containing exactly one "@" symbol, featuring non-empty local and domain parts, and a domain that includes at least one dot. Any malformed entries or non-string data types are safely ignored during the process, and the function returns 0 if the input list is empty.

## 4) Final Judgment
- Decision: Request Changes

- Justification: The original impementation does not correctly validate email addresses and makes unsafe assumptions about imput types and the accompanying explanation is misleading.

- Confidence & unknowns: High confidence. Full RFC-compliant validation was intentionally avoided to keep the fix minimal and appropriate to scope.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function uses the total number of imput values as the divisor even though None values are excluded from the sum.
- The function can raise a ZeroDivisionError when given an empty list

### Edge cases & risks
- Lists containing only None values return an invalid result.
- Non-numeric values cause float(v) to raise exceptions.
- Mixed-type imputs are not handled safely.

### Code quality / design issues
- Business logic is inconsistently applied between numerator and denominator.
- The function assumes all non-None values are convertible to floats.
- The explanation does not reflect the actual behavior of the code.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track the count of valid numeric measurements explicitly.
- Ignore None and non-numeric values.
- Add a guard to prevent division by zero.
- Convert values to floats only after safe validation.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
If I was testing this function, I would focus on:
- Empty imput lists.
- Mixed numeric and non-numeric imputs.
- Lists containing only None values.
- Valid numeric values provided as both numbers and numeric strings.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The function does not correctly ignore missing values in the divisor.
- It does not safely handle mixed imput types and can raise exceptions.
- The explanation incorrectly claims accuracy and safety.

### Rewritten explanation
- This function calculates the average of valid numeric measurements by summing all entries that can be safely converted to floats and dividing by the total count of those successful conversions. During processing, the function ignores None values and any entries that are incompatible with float conversion to ensure the integrity of the result. If no valid measurements are present in the data, the function returns 0.0 to prevent a division-by-zero error.

## 4) Final Judgment
- Decision: Request Changes.

- Justification: The original implementation produces incorrect averages, fails on common edge cases and is accompanied by an inaccurate explanation.

- Confidence & unknowns: High confidence in the indentified issues and fixes. The correct behaviour is safe, minimal and consistent with typical expectation for numeric aggregation.
