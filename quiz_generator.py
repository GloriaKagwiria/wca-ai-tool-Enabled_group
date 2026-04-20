#==============================================================
# QUIZ GENERATOR- ENABLED GROUP-PROJECT(Powered by claude AI)
# Members : 1(Setup) |2 (Prompt) |3 (API) |4(Input) |5(Main)
# How to run : python quiz_generator.py
#===============================================================

#===============================================================
# Member 1- Project Setup $ API Configuration
# Commit 1: Add project imports
# Commit 2: Configure anthropic client using environment variable
# Commit 3: Add project-level documentation and header comments
#================================================================

import anthropic
import os

# The API key is loaded from the environment variable ANTHROPIC_API_KEY
# To set it permanently, run : setx ANTHROPIC_API_KEY "your_key_here"
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


#=================================================================