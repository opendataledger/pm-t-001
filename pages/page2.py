import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

########################################################################################

# Updated list of words
words = [
    "anklebone", "blamable", "botulism", "braggart", "braille", "buffered",
    "cataract", "damask", "emanate", "existence", "fiercely", "flagrant", 
    "flounce", "food chain", "footbridge", "fragrance", "graffiti", "griminess", 
    "haggard", "hindrance", "hygienic", "intermittent", "jamboree", "Kleenex", 
    "lamentation", "light-year", "liquefy", "malefactor", "manageable", 
    "meditative", "misspend", "motley", "necessitate", "notoriety", "nougat", 
    "novitiate", "nurturant", "nuthatch", "nutlet", "nutriment", "odometer", 
    "Offertory", "penitence", "quick bread", "racketeer", "raspy", "rationale", 
    "russet", "scarcely", "scourge", "spectacle", "syllabicate", "taffeta", 
    "tincture", "tousle", "toxemia", "typify", "ultima", "unaligned", "unlined", 
    "vegetative", "Venus", "wallaby", "web-footed", "xylophone", "yacht", "zealous"
]

# Create 26 tests (A-Z)
def create_tests(words_list):
    tests = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        filtered_words = [word for word in words_list if word.startswith(letter)]
        tests[letter] = filtered_words
    return tests

tests = create_tests(words)

# Streamlit application
st.title("👍 Selected 5th-6th Grade - Spelling Game")

def pronounce(word):
    # Embed the ResponsiveVoice script into Streamlit using components
    st.components.v1.html(f"""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    <script>
        responsiveVoice.speak("{word}", "US English Female");
    </script>
    """, height=0)  # Set height=0 to hide the script output

def pronounce_again(word):
    # Embed the ResponsiveVoice script into Streamlit using components
    st.components.v1.html(f"""
    <script src="https://code.responsivevoice.org/responsivevoice.js?key=Ytp4Wvua"></script>
    <script>
        responsiveVoice.speak("{word}", "US English Male");
    </script>
    """, height=0)  # Set height=0 to hide the script output

# Select test
letter = st.sidebar.selectbox("Select a letter below:", list(tests.keys()))
words_to_test = tests[letter]

# Initialize session state for tracking the current word index
if 'current_word_index' not in st.session_state:
    st.session_state.current_word_index = 0
    st.session_state.score = 0

# Get the current word based on the index
current_word_index = st.session_state.current_word_index

# Show the current word
if current_word_index < len(words_to_test):
    current_word = words_to_test[current_word_index]

    st.subheader("✳️ Instructions - How to play the spelling game:")
    st.write("1️⃣ STEP-1. Select a spelling game and a letter from the [LEFT SIDEBAR]")
    st.write("2️⃣ STEP-2. Press [BUTTON-🔴Pronounce Word] to hear the spelling word")
    st.write("3️⃣ STEP-3. The word will be pronounced once")
    st.write("4️⃣ STEP-4. Click on the ✏️ TEXT BOX-Your Answer below")
    st.write("5️⃣ STEP-5. Type your answer in the ✏️ TEXT BOX-Your Answer below")
    st.write("6️⃣ STEP-6. Press [BUTTON-🟡Submit] to submit your answer")
    st.write("7️⃣ STEP-7. Press [BUTTON-🟢Next Word] to proeed after you get the result")
    
    st.write("(⚠️ Users are logged out after 15 minutes of inactivity!)")

    # Show pronunciation button
    if st.button("🔴Pronounce Word - Female Voice", key="pronounce"):
        pronounce(current_word)

    # Show pronunciation again button
    if st.button("🔴Pronounce Word - Male Voice", key="pronounce_again"):
        pronounce_again(current_word)
    
    # Inject JavaScript to focus the input field automatically
    st.components.v1.html("""
    <script>
        window.onload = function() {
            const inputField = document.querySelector('input[data-baseweb="input"]');
            if (inputField) {
                inputField.focus();  // Automatically focus the input field when the page loads
            }
        };
    </script>
    """, height=0)

    # Input field for user's answer
    user_input = st.text_input(
        "✏️ Your answer (hidden word):",
        key=f"input_{current_word_index}",  # Unique key to force resetting input field
    )

    # Handle button display logic
    submit_button = st.button("🟡Submit", key="submit")
    next_word_button = st.button("🟢Next Word", key="next_word")
    
    # CSS for custom button styles
    st.markdown("""
    <style>
        .stButton>button {
            background-color: green;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
        .stTextInput input {
            font-size: 18px;
        }
        .score-text {
            color: blue;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Handle the logic when the submit button is clicked
    if submit_button:
        # Pronounce the next word right after the user submits
        if user_input.strip().lower() == current_word:
            st.success("Correct! ✔️")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect! ❌ The correct spelling is: {current_word}")
        
        # Hide the Pronounce and Submit buttons, show Next Word button
        submit_button = None
        st.session_state.current_word_index += 1

    # Display the current score (correct answers / total_words)
    st.markdown(f"**Your current score: {st.session_state.score} / {current_word_index + 1}**", unsafe_allow_html=True)

    # If at the end, reset or display the final score
    if st.session_state.current_word_index >= len(words_to_test):
        st.markdown(f"**Your final score is: {st.session_state.score} / {len(words_to_test)}**", unsafe_allow_html=True)
        if st.button("▶️Restart"):
            st.session_state.current_word_index = 0
            st.session_state.score = 0

            st.subheader("✳️ Instructions - How to start or restart the spelling game:")
            st.write("1️⃣ STEP-1. Select a spelling game and a letter from the [LEFT SIDEBAR]")
            st.write("2️⃣ STEP-2. Press [BUTTON-▶️Restart] above to start or restart a new game")
            
            st.write("(⚠️ Users are logged out after 15 minutes of inactivity!)")
else:
    st.markdown(f"**Your final score is: {st.session_state.score} / {len(words_to_test)}**", unsafe_allow_html=True)
    if st.button("▶️Restart"):
        st.session_state.current_word_index = 0
        st.session_state.score = 0

        st.subheader("✳️ Instructions - How to start or restart the spelling game:")
        st.write("1️⃣ STEP-1. Select a spelling game and a letter from the [LEFT SIDEBAR]")
        st.write("2️⃣ STEP-2. Press [BUTTON-▶️Restart] above to start or restart a new game")

        st.write("(⚠️ Users are logged out after 15 minutes of inactivity!)")
