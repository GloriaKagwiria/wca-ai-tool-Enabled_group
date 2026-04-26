# wca-ai-tool-Enabled_group
## Team Members' Names
1. Gloria Kagwiria
2. Pauline Kihiu
3. Franklin Nzioki
4. Gilbert Mungai
5. Elizabeth Baraza


## Quiz Generator AI tool
- A Python-based command-line tool designed to instantly generate custom quizzes using AI.
- This tool streamlines the process of creating educational content by taking simple user inputs and transforming them into structured assessments.
### What it is
- The AI Quiz Generator is a collaborative project that leverages artificial intelligence to automate the creation of quiz questions. 
- It is designed for educators, students, or anyone looking to test their knowledge on specific subjects without the manual effort of writing questions.
### What it does
1. Customizable Topics: 
- Generates questions based on any subject the user provides.
2. Difficulty Scaling: 
- Allows users to choose their preferred challenge level (e.g., Easy, Medium, Hard).
3. Error Handling: 
- Built-in safeguards to manage API failures or connection issues gracefully.
4. Instant Output: 
- Delivers a fully formatted quiz directly to the terminal.
### How it works
1. Input Collection: 
- The script prompts the user for a specific topic and a difficulty level.
2. AI Generation: 
- It passes these parameters to a core generate_quiz() function that communicates with an AI model.
3. Result Display: 
- The tool processes the AI's response and prints a formatted quiz ready for use.
4. Stability: 
- It uses a try/except block to ensure that if something goes wrong during the generation process, the user receives a clear error message instead of a crash.
### How to run it
1. Clone the Repository:
- bash
- git clone https://github.com
- cd quiz_generator.py

2. Install Dependencies:
- (Ensure you have Python installed)
- bash
- pip install -r requirements.txt

3. Run the Application:
- Execute the main script to start the interactive prompt:
- bash
- python quiz_generator.py
  
4. Follow the Prompts:
- Enter your topic and difficulty when prompted, and wait for your quiz to generate.





