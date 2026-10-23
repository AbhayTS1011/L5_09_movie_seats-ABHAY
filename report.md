# Static Analysis Issue Report

## Project

Lab 5: Static Code Analysis — Movie Theater Seat Reservation System (`theater_system.py`). The baseline was analyzed before edits; line numbers below refer to that original source.

## Findings and fixes

| Issue | Type / severity | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Permissive file permissions (Bandit B103) | Security / High | 55 | `os.chmod(..., 0o777)` makes the reservation data readable, writable, and executable by all users. | Removed the chmod call; keep the file's platform defaults. |
| Weak ticket digest (Bandit B324) | Security / High | 25 | MD5 is unsuitable for security-sensitive identifiers. | Changed the digest to SHA-256 while retaining the short display code. |
| Shared mutable default (Pylint W0102) | Bug / Medium | 9 | The default `system_logs=[]` is reused across calls and can leak log entries. | Default to `None` and create a fresh list for each call. |
| Broad exception suppression (Bandit B110, Pylint W0702, Flake8 E722) | Reliability / Low | 18–22 | A bare `except` hides unrelated errors in seat release. | Catch only `ValueError` for a missing seat and handle an unknown show explicitly. |
| Invalid seat values accepted (manual run) | Functional bug / Medium | 11, 36–50 | The original accepted out-of-range numbers and strings; the sample run showed negative and non-integer bookings, yielding misleading availability. | Validate the show, integer type, and range 1 through the capacity before reserving; parse terminal input. |
| File handles and encoding (Pylint W1514/R1732) | Reliability / Low | 28, 33 | Files were opened without context managers or an explicit encoding. | Use `with open(..., encoding="utf-8")` for both JSON operations. |
| Style and naming (Pylint C0114/C0116/C0103/C0301/C0209; Flake8 E302/E501/E305) | Style / Low | Throughout | Missing documentation, non-snake-case function name, old string formatting, excess line lengths, and spacing errors. | Added docstrings, adopted f-strings and snake_case, and formatted to pass Flake8. |

## Before and after

- Pylint baseline: **5.87/10**; final: **10.00/10**.
- Bandit baseline: **2 High, 1 Low**; final: **no issues identified**.
- Flake8 baseline: **11 reported style errors**; final: **no output / no violations**.
- The program was run before changes. It accepted invalid seat values and showed incorrect availability. After the changes, the demonstration was run with default and invalid input; invalid text is rejected and out-of-range bookings are ignored.

## Commits

1. `80a8eea` — Fix security findings from Bandit
2. `86ef5f3` — Resolve Pylint code quality findings
3. `0beda00` — Apply Flake8 formatting cleanup

## Reflection prompt source

The provided handout discusses reflection but does not include the four questions. The companion README requests four answers. The prompts in `reflection.md` are therefore inferred from the handout's learning outcomes and are identified as such.

