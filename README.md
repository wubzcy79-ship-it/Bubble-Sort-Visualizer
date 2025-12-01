# Project Name: Bubble Sort Visualizer
My final project for CISC 121.  
I built a simple Bubble Sort visualizer with Python and Gradio.  
This app can take a list of integers and show how Bubble Sort program works step by step.

# My hugingface link: https://huggingface.co/spaces/Alduin000/Bubble_sort
This link opens the online version of my app. You can enter numbers, click “Run”, and watch the whole sorting steps.
A Sample Picture:<img width="1832" height="955" alt="屏幕截图 2025-12-01 014454" src="https://github.com/user-attachments/assets/81da69fb-1384-4d7a-b7e6-b426836f7353" />

# Problem Breakdown & Computational Thinking
1, Decomposition: This program can be broken into "read the user input from the textbox", "Convert the input into a list of integers", "Compare each pair of adjacent numbers" and "Swap them if the left number is bigger".

2, Pattern Recognition: We can consider that bubble sort just repeat looking at two neighboring values and deciding if they should be swapped. Then, move them to the next pair.

3, Abstraction: 
  
  App Contents ->  The two numbers being compared  
                   Whether they are swapped  
                   The updated list after each comparison  
                   Each full pass through the list  
                   
  Hidden -> Loop counters (i and j)  
            Low-level Python details  
            Some strange temporary variables 

4, Algorithm Design: 
Input: 

A list of integers by users

Output: 

A text book which can show all steps

A text book which can show the final sorted list

5, Flowchart:

<img width="712" height="688" alt="屏幕截图 2025-12-01 020817" src="https://github.com/user-attachments/assets/ca9e3d01-2a30-415f-abf1-06f20d2ab724" />

# How to run the App

# Run it online 

You can also use this app directly on Hugging Face:

https://huggingface.co/spaces/Alduin000/Bubble_sort

When you entry this page, just input an integer list and click "Run"

# If you want to run it on local environment just make sure you have python and required package (Open cmd and input "pip install gradio")

# Testing & Verification

I tested my bubble sort visualizer in some case and all situations seems correct.

<img width="1592" height="891" alt="屏幕截图 2025-12-01 023303" src="https://github.com/user-attachments/assets/d8673a44-6195-4155-a975-2d9627cbb462" />

<img width="1608" height="880" alt="屏幕截图 2025-12-01 023325" src="https://github.com/user-attachments/assets/4c870e6b-9371-4ae2-a676-61018c3d7ea4" />

# AI Acknowledgement (Level 4)

In this project, I used ChatGPT 5.1 to help me with organizing the structure of my README, improving my initial own code and helping me understand how to design a clean Gradio interface



        
