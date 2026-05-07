#!/usr/bin/env python3
"""
Argument Stress-Test CLI Tool

A simple command-line tool that walks a user through a six-stage argument stress-test methodology.
"""

def main():
    print("=== Argument Stress-Test Tool ===\n")
    
    # Get user's initial position
    position = input("Enter your position or argument to stress-test: ").strip()
    if not position:
        print("Error: Position cannot be empty.")
        return
    
    print(f"\nYour position: {position}\n")
    print("We will now proceed through six stages. Type 'continue' after each stage to proceed.\n")
    
    # Define the stages
    stages = [
        {
            "name": "Steel-man",
            "description": "Formulate the strongest possible version of your argument. What would make it most convincing?"
        },
        {
            "name": "Verify Evidence",
            "description": "Examine the evidence supporting your position. Is it reliable, relevant, and sufficient?"
        },
        {
            "name": "Three Strongest Objections",
            "description": "Identify the three strongest objections to your position. Be charitable and thorough."
        },
        {
            "name": "Demolition Attempt",
            "description": "Attempt to demolish your position using the objections and counter-evidence. Where does it break?"
        },
        {
            "name": "Rebuild",
            "description": "How can you rebuild or modify your position to withstand the criticisms?"
        },
        {
            "name": "The Call",
            "description": "After this process, what is your final position? Has it changed, strengthened, or weakened?"
        }
    ]
    
    # Process each stage
    for i, stage in enumerate(stages, 1):
        print(f"Stage {i}: {stage['name']}")
        print("-" * (len(stage['name']) + 8))
        print(stage['description'])
        print()
        
        # Wait for user to type "continue"
        while True:
            user_input = input("Type 'continue' to proceed to the next stage: ").strip().lower()
            if user_input == "continue":
                break
            else:
                print("Please type exactly 'continue' to proceed.")
        
        print()  # Add blank line between stages
    
    print("=== Stress-Test Complete ===")
    print("Thank you for working through the argument stress-test methodology.")

if __name__ == "__main__":
    main()