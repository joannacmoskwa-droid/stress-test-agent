# Argument Stress-Test CLI Tool

A simple Python command-line tool that guides users through a six-stage argument stress-test methodology.

## Features

- Accepts user's position as input at start
- Progresses through six stages in strict order:
  1. Steel-man
  2. Verify Evidence
  3. Three Strongest Objections
  4. Demolition Attempt
  5. Rebuild
  6. The Call
- Waits for user to type "continue" before moving to next stage
- Prevents skipping ahead
- Simple text-based interface

## How to Run

1. Make sure you have Python 3 installed
2. Save the script as `argument_stress_test.py`
3. Run it with: `python3 argument_stress_test.py`
4. Follow the prompts:
   - Enter your position/argument when asked
   - For each stage, read the description and work through the exercise
   - Type exactly "continue" (lowercase) when ready to proceed to the next stage
   - The tool will not allow you to skip ahead

## Stages Explained

1. **Steel-man**: Formulate the strongest possible version of your argument
2. **Verify Evidence**: Examine the evidence supporting your position
3. **Three Strongest Objections**: Identify the three strongest objections to your position
4. **Demolition Attempt**: Attempt to demolish your position using objections
5. **Rebuild**: How can you rebuild or modify your position to withstand criticisms?
6. **The Call**: What is your final position after this process?

## Example Usage

```
$ python3 argument_stress_test.py
=== Argument Stress-Test Tool ===

Enter your position or argument to stress-test: Renewable energy is the best solution for climate change

Your position: Renewable energy is the best solution for climate change

We will now proceed through six stages. Type 'continue' after each stage to proceed.

Stage 1: Steel-man
-----------------
Formulate the strongest possible version of your argument. What would make it most convincing?

Type 'continue' to proceed to the next stage: continue
...
```

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Notes

- The tool is designed for interactive use only
- Input validation ensures users must type exactly "continue" to proceed
- Empty positions are not allowed
- The tool guides reflection but does not provide automated analysis