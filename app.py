# --- Project- Growth Mindset Challenge: Web App with Streamlit ----#
# 01: importing streamlit to make app with streamlit 
import streamlit as st                          
# 02: importing random module to select random questions each time.
import random                                   
# 03 importing time to provide a delay before refreshing app.
import time
# 04: create a list of dictionaries in which each dictionary store a question, answer & hint.
my_question =[
    {"question":"What comes once in a minute, twice in a moment, but never in a thousand years?","answer": "letter M","hint":"It's in music, in mice, in momements."},
    {"question":"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo","hint": "It repeats what you say."},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "Footsteps","hint": "You make these when walking.","hint": "Think about digging in the ground."},
    {"question": "The more you remove from it, the bigger it gets. What is it?", "answer": "hole","hint": "Think about digging in the ground."},
    {"question": "I have hands but no thumbs, a face but no eyes. What am I?", "answer": "clock","hint": "It helps you tell time."},
    {"question": "The more you share me, the less you have. What am I?", "answer": "secret", "hint": "Once you tell someone, it's no longer just yours."},
    {"question": "I fly without wings, I cry without eyes. What am I?", "answer": "cloud","hint": "You see it in the sky and it brings rain."},
    {"question": "What has to be broken before you can use it?", "answer": "egg","hint": "It's something you eat."},
    {"question": "What is always in front of you but can't be seen?", "answer": "future","hint": "It's what comes next in life."},
    {"question": "I am tall when I’m young, and short when I’m old. What am I?", "answer": "candle","hint": "It melts as it burns."},
]
# 05: Setting up App title e.i main heading and a subheading.
st.title("🧠Brain Teasers & Puzzle Solver")
st.markdown("<h4 style='text-align: center; color: darkblue; font-weight: bold;'>Let's test your intelligence!</h4>", unsafe_allow_html=True)

# 06: Setting up Sidebar Title & Welcome Message
st.sidebar.title("🎯 Progress Status!")  # Sidebar Title
st.sidebar.info("Welcome to the Brain Teasers Game! 🎉") 

# 07: Creating two variable (correct & total) for tracking progress.
if "correct" not in st.session_state:
    st.session_state.correct = 0
if "total" not in st.session_state:
    st.session_state.total = 0

# 08: Creating Sidebar subheader as progress bar
st.sidebar.subheader("📊 Progress")
progress = st.session_state.correct / st.session_state.total if st.session_state.total else 0
st.sidebar.progress(progress)
st.sidebar.write(f"✅ {st.session_state.correct} / {st.session_state.total} correct")

# 09: condition for selecting random questions.
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(my_question)

# 10: To display the question in app.
disp_question = st.session_state.current_question
st.write(f"<br><h5>Question: {disp_question['question']}</h5>", unsafe_allow_html=True)

# 11: To get user answer
user_answer = st.text_input("Enter Your **Answer**:").strip().lower()

# 12: To check answer of user 
if st.button("Check Answer"):
    if user_answer:
        st.session_state.total += 1  # it will total attempt

        if user_answer == disp_question["answer"].lower():
            st.session_state.correct += 1  # will increment 1 if answer is correct
            st.success("🎊Correct Answer! Very Good!😊")
        else:
            st.warning(f"☠ Opps it's Wrong! 💡Hint! **{disp_question['hint']}**.")

        time.sleep(3)   # app will refresh after 3 second
        st.rerun()  
    else:
        st.info("🔹 Please enter an answer before checking.")  

        
# Button to get a new question
if st.button("New Question"):
    st.session_state.current_question = random.choice(my_question)
    st.rerun()
