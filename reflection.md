# Reflection: Static Code Analysis

The supplied handout does not list the four reflection questions referenced by the repository README. The following prompts are inferred from the handout's learning outcomes; replace them with the instructor's exact questions if those are provided separately.

## 1. What is static code analysis, and how is it useful?

Static code analysis inspects source code without running it. In this lab, it helped identify security risks, error-prone practices, and style problems early. Running the program was still useful because it revealed incorrect seat handling that the tools did not report.

## 2. How do Pylint, Bandit, and Flake8 differ?

Pylint checks broad code quality, naming, documentation, and likely defects. Bandit focuses on common security risks, such as weak hashes and unsafe file permissions. Flake8 reports Python style and formatting problems. Their reports overlap in a few areas, but each gives a different view of the same source.

## 3. Which issues mattered most, and how were they fixed?

The highest-severity findings were the world-writable permissions and the MD5 digest. I removed the permission change and switched to SHA-256. I also replaced the bare exception handler, fixed the shared mutable default, and added validation so reservations must use an integer seat within the show's capacity.

## 4. What did the tools teach you about code quality and maintainability?

Clean formatting and documentation make code easier to review, while explicit error handling and input validation make behavior more predictable. The tools caught many issues, but they did not detect every functional problem; running the program and examining its output remained necessary. Rerunning the analyzers after changes confirmed that the reported findings were addressed.
