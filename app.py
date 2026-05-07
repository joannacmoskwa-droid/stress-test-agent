#!/usr/bin/env python3
"""
Argument Stress-Test Web App
A simple Flask web application that walks users through a six-stage argument stress-test methodology.
"""

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session security

# Define the six stages
STAGES = [
    {
        "name": "Steel-man",
        "description": "Formulate the strongest possible version of your argument. What would make it most convincing?",
        "prompt": "Take a moment to strengthen your position as much as possible."
    },
    {
        "name": "Verify Evidence",
        "description": "Examine the evidence supporting your position. Is it reliable, relevant, and sufficient?",
        "prompt": "Consider the quality and sources of your evidence."
    },
    {
        "name": "Three Strongest Objections",
        "description": "Identify the three strongest objections to your position. Be charitable and thorough.",
        "prompt": "Think from the perspective of someone who disagrees with you."
    },
    {
        "name": "Demolition Attempt",
        "description": "Attempt to demolish your position using the objections and counter-evidence. Where does it break?",
        "prompt": "Be brutally honest about weaknesses in your position."
    },
    {
        "name": "Rebuild",
        "description": "How can you rebuild or modify your position to withstand the criticisms?",
        "prompt": "Consider how to address the weaknesses you identified."
    },
    {
        "name": "The Call",
        "description": "After this process, what is your final position? Has it changed, strengthened, or weakened?",
        "prompt": "Reflect on your original position vs. your current thinking."
    }
]

@app.route('/')
def index():
    # Clear any existing session data when starting fresh
    session.clear()
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    position = request.form.get('position', '').strip()
    if not position:
        flash('Please enter your position or argument to continue.', 'error')
        return redirect(url_for('index'))
    
    # Initialize session data
    session['position'] = position
    session['current_stage'] = 0  # 0-indexed
    session['stage_data'] = {}  # To store user's notes for each stage
    
    return redirect(url_for('stage'))

@app.route('/stage', methods=['GET', 'POST'])
def stage():
    if 'position' not in session:
        return redirect(url_for('index'))
    
    current_stage_idx = session['current_stage']
    
    if current_stage_idx >= len(STAGES):
        return redirect(url_for('complete'))
    
    stage = STAGES[current_stage_idx]
    
    if request.method == 'POST':
        # User clicked "Continue" - save their notes and move to next stage
        notes = request.form.get('notes', '').strip()
        session['stage_data'][str(current_stage_idx)] = notes
        session['current_stage'] = current_stage_idx + 1
        
        # If we've completed all stages, go to completion page
        if session['current_stage'] >= len(STAGES):
            return redirect(url_for('complete'))
        
        return redirect(url_for('stage'))
    
    # GET request - show the stage
    notes = session['stage_data'].get(str(current_stage_idx), '')
    
    progress = {
        'current': current_stage_idx + 1,
        'total': len(STAGES),
        'percentage': int(((current_stage_idx) / len(STAGES)) * 100)
    }
    
    return render_template('stage.html', 
                         stage=stage, 
                         stage_num=current_stage_idx + 1,
                         notes=notes,
                         progress=progress)

@app.route('/complete')
def complete():
    if 'position' not in session:
        return redirect(url_for('index'))
    
    # Prepare data for display
    position = session['position']
    stage_data = session.get('stage_data', {})
    
    stages_data = []
    for i, stage in enumerate(STAGES):
        stages_data.append({
            'name': stage['name'],
            'notes': stage_data.get(str(i), '')
        })
    
    return render_template('complete.html',
                         position=position,
                         stages=stages_data)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)