import streamlit as st

st.set_page_config(page_title="Python MCQ Exam", layout="centered")

st.title("📝 Unit 2: Python MCQ Practice (50 Questions)")

# ----------- QUESTIONS ----------- #

questions = [
{
"q":"What will be the output?\n\nprint(2 + 3 * 4)",
"options":["14","20","24","Error"],
"ans":"A",
"exp":"Multiplication has higher precedence → 3*4=12 → 12+2=14"
},
{
"q":"Which data type is immutable in Python?",
"options":["List","Dictionary","Set","Tuple"],
"ans":"D",
"exp":"Tuple is immutable, others are mutable"
},
{
"q":"What will be the output?\n\nprint(type(10))",
"options":["<class 'int'>","int","number","error"],
"ans":"A",
"exp":"type() returns class type"
},
{
"q":"Which keyword is used to define a function?",
"options":["function","define","def","fun"],
"ans":"C",
"exp":"'def' is used to define functions"
},
{
"q":"What will be the output?\n\nprint('Hello' * 2)",
"options":["HelloHello","Hello 2","Error","None"],
"ans":"A",
"exp":"String repetition operator '*' repeats string"
},
{
"q":"Which of the following is used for comments?",
"options":["//","#","/* */","--"],
"ans":"B",
"exp":"# is used for single line comments"
},
{
"q":"What will be output?\n\nprint(bool([]))",
"options":["True","False","Error","None"],
"ans":"B",
"exp":"Empty list evaluates to False"
},
{
"q":"Which operator is used for exponentiation?",
"options":["^","**","//","%"],
"ans":"B",
"exp":"** is exponent operator"
},
{
"q":"What will be output?\n\nprint(10//3)",
"options":["3","3.33","4","Error"],
"ans":"A",
"exp":"// gives floor division"
},
{
"q":"Which structure stores key-value pairs?",
"options":["List","Tuple","Set","Dictionary"],
"ans":"D",
"exp":"Dictionary stores key-value pairs"
},
]

# Extend to 50
while len(questions) < 50:
    questions.append(questions[len(questions) % 10])

# ----------- SESSION ----------- #

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answered = [False]*50

# ----------- DISPLAY QUESTION ----------- #

q = questions[st.session_state.index]

st.markdown(f"### Question {st.session_state.index+1} of 50")
st.write(q["q"])

# Proper option formatting
choice = st.radio(
    "Select your answer:",
    options=["A","B","C","D"],
    format_func=lambda x: f"{x}) {q['options'][ord(x)-65]}"
)

# ----------- ACTION BUTTONS ----------- #

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Previous") and st.session_state.index > 0:
        st.session_state.index -= 1

with col2:
    if st.button("✅ Submit Answer"):
        if not st.session_state.answered[st.session_state.index]:
            st.session_state.answered[st.session_state.index] = True
            
            if choice == q["ans"]:
                st.success("Correct ✅")
                st.session_state.score += 1
            else:
                st.error(f"Wrong ❌ | Correct Answer: {q['ans']}")
            
            st.info(f"💡 Explanation: {q['exp']}")

with col3:
    if st.button("➡️ Next") and st.session_state.index < 49:
        st.session_state.index += 1

# ----------- SCORE ----------- #

st.markdown(f"### 🎯 Score: {st.session_state.score}")