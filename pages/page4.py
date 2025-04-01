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
    "abbreviate", "abnormality", "abode", "abrasion", "abundantly", "academic",
    "accessory", "accordion", "acidic", "acne", "acrobat", "adhesive",
    "admirable", "adoption", "adversary", "affected", "affliction", "affordable",
    "agenda", "airport", "alimony", "allergic", "alliance", "alpaca",
    "alphabetical", "amateur", "amplify", "amusing", "animate", "anklebone",
    "annex", "antibacterial", "antibiotic", "anxiety", "apparition", "appease",
    "applause", "aptitude", "aquamarine", "arcade", "arrangement", "assortment",
    "athletic", "attractive", "auditory", "avalanche", "avocado", "badminton",
    "balky", "Ballyhoo", "barbarian", "bareback", "bargain", "barrette",
    "bashfulness", "beacon", "bedazzle", "bedridden", "beforehand", "behavior",
    "believable", "beneficial", "benevolent", "biannual", "bicultural", "bicycle",
    "billionaire", "bimonthly", "biodiversity", "bionics", "birthmark", "blamable",
    "blarney", "blissful", "blistering", "bluebonnet", "bolster", "bonfire",
    "boomerang", "botulism", "boulevard", "bountiful", "braggart", "braille",
    "brainstorm", "brilliance", "brisket", "brooch", "buffered", "buffoonery",
    "bulbous", "bureau", "burglarize", "calculate", "calendar", "canopy",
    "capitalism", "cardiac", "carnation", "cartridge", "cataract", "cavernous",
    "centimeter", "ceremony", "chaplain", "charitable", "choppiness", "cinema",
    "circulation", "circumstance", "clearance", "clergy", "clincher", "closure",
    "cohesion", "coincidence", "colander", "columnist", "combustion", "commercial",
    "communicable", "commute", "complaint", "concentrate", "concerto", "confirmed",
    "congratulate", "connection", "connive", "consultation", "convention", "convoy",
    "corrode", "corruption", "cramming", "creative", "critical", "curiosity",
    "currency", "curtail", "damask", "dauntless", "debonair", "debt", "decagon",
    "deceit", "declining", "deductible", "deflate", "deformity", "dehydrate",
    "delivery", "democracy", "deodorant", "desperate", "detestable", "development",
    "devotion", "diagram", "dictation", "dietary", "diligent", "diorama",
    "discipline", "discreet", "disembark", "disinfect", "dispensable", "disregard",
    "district", "divergence", "doleful", "domain", "dominance", "dosage",
    "downcast", "draftsman", "drone", "dumpling", "dwindle", "dynasty",
    "earliest", "earphone", "earsplitting", "editorial", "effective", "egoism",
    "elaborate", "elapse", "elasticity", "electromagnet", "eligible", "emanate",
    "embroidery", "emergency", "emotional", "employee", "encore", "endear",
    "endurance", "energetic", "engagement", "enjoyably", "enormity", "entirety",
    "environment", "episode", "equate", "erase", "escapism", "estimate",
    "ethical", "everglade", "evict", "evidence", "excel", "exercising", "exhale",
    "existence", "expenditure", "experience", "exploration", "expound", "extremity",
    "fabulous", "facedown", "factorization", "famish", "fanciful", "fatalism",
    "fattened", "federalist", "feminine", "ferocious", "fiberglass", "fictionalize",
    "fidelity", "fiercely", "filbert", "filtration", "flagrant", "flatterer",
    "flounce", "food chain", "footbridge", "foreclose", "foreign", "forerunner",
    "forgery", "forgetfulness", "formative", "fortitude", "foyer", "fraction",
    "fragile", "fragrance", "frankfurter", "fraternity", "freebie", "freedbee",
    "freedom", "frontier", "functional", "funeral", "furlough", "fuzziness",
    "gangplank", "gasoline", "gaudy", "gauze", "gearless", "gemstone", "generality",
    "generation", "genetic", "geographical", "geometric", "giddy", "gingerly",
    "glacier", "gloominess", "gluttony", "goldenrod", "good-humored", "goodwill",
    "gooseneck", "gorgeous", "govern", "gradually", "graffiti", "granola", "graphic",
    "gravitation", "greasier", "greatness", "greengrocer", "griminess", "grinning",
    "grizzled", "grouchy", "guidance", "guidebook", "gumbo", "gurgle", "habitable",
    "haggard", "hamstring", "handicapped", "handily", "handlebar", "happiness",
    "happy-go-lucky", "harmfully", "hatchery", "hauntingly", "heatedly", "heather",
    "heatstroke", "hedgehog", "heighten", "henceforth", "hepatitis", "herbicide",
    "hexagon", "hibachi", "hideous", "hindrance", "hoist", "hominid", "homophone",
    "honeycomb", "hoopskirt", "horoscope", "hotheaded", "hovercraft", "humidity",
    "hummingbird", "husbandry", "hydrology", "hyena", "hygienic", "hyphen", "hypnosis",
    "hysterics", "icicle", "idealism", "identical", "ideology", "ignoring", "illegal",
    "imaginable", "imitative", "immense", "immodest", "immovable", "impassable",
    "impeach", "impossible", "improper", "improvise", "incidence", "incision",
    "inconvenience", "indecision", "independent", "indicator", "inedible", "infatuate",
    "inferior", "inherent", "injustice", "innovative", "instructor", "insulation",
    "insurance", "interesting", "intermittent", "internist", "intrusive", "inventory",
    "invigorate", "invitation", "irrational", "irrigation", "issue", "jaguar",
    "jamboree", "jawbreaker", "jellyfish", "jetty", "jitterbug", "jobholder", "joggled",
    "joist", "jubilation", "juniper", "justify", "kelp", "kernel", "kidney",
    "kindhearted", "kinship", "Kleenex", "knighthood", "knitting", "knockabout",
    "laboratory", "lacerate", "lamentation", "laminate", "landline", "languid",
    "larceny", "lattice", "lawlessly", "layette", "league", "leastwise", "leathery",
    "lectern", "leeway", "legality", "legislature", "leisure", "lemon", "levelheaded",
    "licorice", "lifeline", "light-year", "limerick", "lineage", "liquefy",
    "listener", "lobbyist", "locality", "loneliness", "loose", "lottery", "loudmouth",
    "lumberyard", "luminescent", "luxurious", "lynx", "magnetic", "magnolia",
    "mainstream", "maize", "malefactor", "malformation", "malicious", "manageable",
    "marathon", "mascara", "masterful", "materialize", "maturity", "maximum", "Maya",
    "meaningful", "medication", "meditative", "melodrama", "membrane", "memorial",
    "mercenary", "merchant", "metallic", "meteorologist", "migratory", "miniature",
    "minivan", "minority", "misconception", "misguidance", "misspend", "mistletoe",
    "mistrust", "monitor", "monotone", "mosquito", "motley", "multitude", "murmur",
    "mutate", "nape", "narcotic", "narrator", "nationalism", "natural resource",
    "navigable", "navigator", "necessitate", "needful", "neglectful", "negotiate",
    "neighborhood", "nervy", "nethermost", "nettle", "neutralize", "newcomer",
    "newspaperman", "nifty", "nightly", "ninepin", "nitpick", "noiseless",
    "nonchalant", "nonprofit", "nonsense", "nonverbal", "nonviolence", "normalize",
    "northeasterly", "nostalgic", "notoriety", "nougat", "novitiate", "nozzle",
    "nuisance", "numeral", "nurturant", "nuthatch", "nutlet", "nutriment", "obese",
    "obeying", "obituary", "oblivious", "obscure", "observant", "obviously",
    "occupation", "odometer", "Offertory", "officiate", "olive", "ominous",
    "onslaught", "opacity", "openhearted", "operating", "opposable", "optimal",
    "optometry", "orate", "orbiter", "orderliness", "ordinary", "oregano",
    "organic", "original", "ornery", "outburst", "outlying", "outwardly",
    "outweigh", "overestimate", "override", "oversupply", "oxygen", "packaging",
    "palpitate", "panhandle", "paradise", "paradox", "parakeet", "paralysis",
    "pathogen", "patriotic", "pedestal", "pedicure", "penalize", "penetrate",
    "penitence", "pepperoni", "percentage", "perfection", "perilous", "perplexity",
    "pesticide", "petroleum", "pictorial", "pineapple", "pinkie", "pinky",
    "plaintiff", "plasticity", "poisonous", "policyholder", "polyester", "portable",
    "portfolio", "possession", "practical", "precinct", "predestine", "predicament",
    "proactive", "problematic", "proceed", "profession", "prosperous", "puzzling",
    "quaintness", "qualm", "quarantine", "quarterback", "queasier", "quick bread",
    "quince", "quitting", "quizzes", "racketeer", "radiantly", "radical",
    "railroad", "ramshackle", "raspy", "rationale", "realistic", "reasoning",
    "reassure", "rebroadcast", "rebuttal", "receive", "recession", "reconcile",
    "reconstruct", "rectangular", "reference", "refrigerate", "regardless", "regiment",
    "relentless", "relevant", "reluctantly", "remnant", "replacement", "replica",
    "reptilian", "respectable", "restaurant", "retort", "retriever", "revenue",
    "review", "ricotta", "ridiculous", "roadrunner", "rodent", "rollicking",
    "roughneck", "rowdiness", "rubella", "russet", "sabotage", "salsa", "sarcasm",
    "satisfactory", "scandal", "scarcely", "schedule", "scorekeeper", "scourge",
    "seasonable", "seclusion", "sectional", "sedative", "seizure", "semiarid",
    "sensational", "seriously", "seventh", "shrewd", "siesta", "simplicity",
    "singular", "situation", "skittish", "sociable", "solidify", "solstice",
    "specific", "spectacle", "spectrum", "splendid", "squirm", "statement",
    "stationary", "stereotype", "strategy", "stubborn", "subjective", "substantial",
    "summary", "supplement", "survive", "syllabicate", "symbolism", "synthetic",
    "taffeta", "talkative", "tastefully", "taxation", "technician", "telescopic",
    "temperament", "tension", "terrier", "terrific", "textual", "theatrical",
    "thermometer", "thesis", "threaten", "thwart", "tightwad", "timberline",
    "tincture", "tinsel", "toilsome", "tollgate", "tomorrow", "topical", "tousle",
    "toxemia", "tragedy", "translate", "treasurer", "tremendous", "triangular",
    "trophy", "trustworthy", "tunnel", "turbojet", "twentieth", "typewriter",
    "typify", "ultima", "unaffected", "unaligned", "unbearable", "unblemished",
    "unclassified", "underpass", "unenclosed", "uneventful", "uniformity",
    "university", "unlined", "unplug", "unravel", "unutterable", "uproarious",
    "usage", "uttermost", "vaccinate", "validity", "vandalism", "vanquish",
    "vaporize", "vegetative", "velocity", "vendetta", "veneer", "venture",
    "Venus", "version", "veterinarian", "victimize", "vigilant", "vindicate",
    "visitation", "vitality", "vivid", "vocation", "volcanic", "volume",
    "waistband", "wallaby", "warehouse", "warrant", "wash-and-wear", "waspish",
    "wearable", "web-footed", "wharf", "wheelchair", "wherefore", "white blood cell",
    "whitening", "wireless", "wisecrack", "wittingly", "woozy", "workmanship",
    "xylophone", "yacht", "yearling", "zealous", "zestfully"
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
st.title("👍 Full 5th-6th Grade - Spelling Game")

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
letter = st.sidebar.selectbox("Select a letter:", list(tests.keys()))
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
