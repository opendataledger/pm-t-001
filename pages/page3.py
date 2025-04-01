import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions and sidebar functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

st.title(" 📝 3rd-4th Grade - List of Words")

st.write("(*Users are logged out after 15 minutes of inactivity!)")

# Streamlit interface for the test
st.write(
    """
(A)"abandon", "absent", "absolute", "academy", "ache",
"address", "adult", "afterglow", "against", "airliner", "alley", "allspice", "almond", "already", "alter",
"ambition", "amusement", "ancestor", "annual", "apology", "appetite", "argue", "artist", "assign", "astronomer",
"athlete", "autograph", "autumn", "awesome".

    """
)

st.write(
    """
 (B)"backpack", "badger", "bagel", "bait", "banana", "barefoot",
"bark", "barley", "barrier", "baste", "beaver", "beehive", "beige", "beverage", "beware", "biology",
"black hole", "blade", "blockage", "blueberry", "blurt", "blush", "borrow", "bottom", "bravery", "bridesmaid",
"bridle", "bronco", "brownie", "building", "built-in", "buttermilk".
    
    """
)

st.write(
    """
 (C)"calm", "camel", "canine", "capsule", "California", 
"cashew", "caterpillar", "catwalk", "cautious", "cement", "century", "champion", "charming", "cheerful", "childish",
"chuckle", "circuit", "circulate", "citizenship", "climate", "coconut", "collection", "comma", "company", "compel",
"computer", "concern", "condone", "copy", "cousin", "creakier", "creepy", "cricket", "curtsy", "custard".
    
    """
)

st.write(
    """
 (D)"dairy", "dazzled", "deaden", "decaf", "decent", "decimal", "decline", "dentist", "dependable", "desktop",
"dessert", "develop", "diary", "dipper", "direction", "disappoint", "disease", "dishonest", "dismiss", "dispute",
"distrust", "dizzy", "doggy", "dose", "downwind", "dramatic", "dribble", "drinkable", "drudge", "duet".
    
    """
)

st.write(
    """
 (E)"eagle", "earnings", "easiest", "easygoing", "echo", "economical", "edition", "educate", "eggplant", "either",
"elderly", "electrify", "element", "elevator", "elude", "emotion", "empower", "enable", "ending", "energy",
"entirely", "entrap", "entry", "error", "essay", "esteem", "ever", "example", "exchange", "exercise",
"export", "eye-catching", "eyelash".
    
    """
)

st.write(
    """
 (F)"factual", "falcon", "famous", "farmstead", "faucet", "fearless", "ferret",
"festival", "fidget", "field", "filmstrip", "fizzling", "flavor", "fleece", "foliage", "footstep", "foresight",
"forestry", "formula", "forthright", "framed", "frank", "freaky", "frightful", "frown", "fudge", "funnel".
"furry".
    
    """
)

st.write(
    """
 (G)"gadget", "gala", "galaxy", "garden", "garment", "garnish", "gathering", "generous", "genius",
"gentlefolk", "geology", "German", "germfree", "giggle", "giraffe", "glassblower", "glimpse", "gloomy", "goalpost", "goggles",
"gosling", "grader", "granite", "graph", "gravity", "gravy", "greedy", "griddle", "grime", "grungy",
"guardian", "guide", "guitar", "gummy", "gusto".
    
    """
)

st.write(
    """
 (H)"hairdresser", "hallway", "halt", "handful", "handsaw",
"hapless", "harmonica", "harp", "harvest", "hateful", "hawk", "headfirst", "healer", "heavenly", "hefty",
"hemline", "heritage", "hipbone", "Hispanic", "history", "hoarse", "honorable", "hotel", "hottest", "housemaid", "humid",
"hurricane", "hurried".
    
    """
)

st.write(
    """
 (I)"igloo", "illness", "image", "immune", "impact", "imprint", "imprison", "incoming",
"index", "indigo", "infest", "inform", "inherit", "injury", "inkling", "inland", "inquest", "inscribe",
"insertion", "insulate", "interest", "intrude", "inventive", "Irish", "iron", "irritate".
    
    """
)

st.write(
    """
 (J)"jabbed", "jacket", "jailbird",
"janitor", "jawbone", "jelly", "journal", "June", "junior".
    
    """
)

st.write(
    """
 (K)"kennel", "keynote", "kidnap", "kindness", "kitty",
"knuckle", "kook".
    
    """
)

st.write(
    """
 (L)"landing", "landscape", "larva", "lately", "latitude", "lavender", "lawyer", "leader",
"leakage", "leap", "legally", "leotard", "liberty", "ligament", "light-footed", "likeness", "limiting", "linger",
"lining", "listen", "liven", "lofty", "logbook", "longhorn", "loudness", "loveliness", "luminous", "lure",
"lush".
    
    """
)

st.write(
    """
 (M)"machine", "magazine", "magical", "magnet", "majority", "mammoth", "manager", "marine", "massage",
"massive", "mechanical", "medicine", "medley", "meow", "merge", "mermaid", "microwave", "migrant", "mineral",
"mingled", "minimal", "misshapen", "mistletoe", "mistreat", "modest", "modify", "molasses", "muffler", "muscle",
"mystery", "myth".
    
    """
)

st.write(
    """
 (H)"napkin", "narrate", "national", "naturalize", "nearby", "necessary", "necklace", "neglect",
"nephew", "newlywed", "nineteenth", "noel", "noggin", "nomad", "nonfiction", "nonviolent", "normal", "nosebleed",
"noted", "notion", "nourish", "novel", "noxious", "nudging", "numeric", "nunnery", "nuzzle", "nylon".
    
    """
)

st.write(
    """
 (O)"oarsman", "obsess", "obstinate", "obtain", "oddity", "offense", "oilcloth", "okra", "once", "oodles",
"oozy", "operate", "opposite", "opt", "orbit", "ordeal", "ore", "organ", "origin", "ouch",
"ounce", "outlandish", "outside", "overcome", "overripe", "ozone".
    
    """
)

st.write(
    """
 (P)"painful", "panic", "parasite", "parish",
"particle", "pastry", "pasture", "patrolman", "peach", "peacock", "pecan", "pedicure", "percent", "perky",
"perplex", "perspire", "phonics", "phrase", "physical", "pierce", "pledge", "pliable", "pointless", "positive",
"poultice", "preacher", "precious", "predict", "priceless", "primary", "prosper", "proverb", "purebred".
    
    """
)

st.write(
    """
 (Q)"quail",
"quaint", "quart", "quash", "quest", "quibbling", "quilt", "quirk", "quite", "quoted".
    
    """
)

st.write(
    """
 (R)"radar",
"radio", "raggedy", "raisin", "readable", "rebate", "recess", "recollect", "refashion", "regardful", "register",
"release", "relic", "remedy", "reporter", "reptile", "respond", "retail", "retreat", "revenge", "rhino",
"riflery", "romance", "rooster", "rotating", "rough", "rowdy", "ruby", "rudeness", "rust".
    
    """
)

st.write(
    """
 (S)"sacred",
"salmon", "salute", "sarcastic", "sawdust", "scientist", "scorpion", "seamstress", "secretary", "seventh", "several",
"shabbily", "sibling", "sketch", "slippery", "sluggish", "snoopy", "soccer", "soprano", "sourdough", "soybean",
"spirited", "sponsor", "stadium", "stomach", "struggle", "subtract", "succeed", "suddenly", "superior", "syllable",
"system".
    
    """
)

st.write(
    """
 (T)"tabulate", "talent", "tattered", "tattletale", "teethe", "tempting", "tennis", "term", "textbook",
"thankfully", "theft", "thermostat", "thicken", "thievery", "throat", "thumbnail", "thunderbolt", "tickling", "timid",
"together", "toughen", "tourism", "treasure", "tremor", "tribal", "trombone", "trouble", "tulip", "tuneful",
"turmoil", "twitter", "typhoon".
    
    """
)

st.write(
    """
 (U)"umpire", "unable", "underhand", "underneath", "unfair", "unicorn", "uninstall",
"unit", "universe", "unlisted", "unpleasant", "unseal", "unsure", "untangle", "upright", "upturn", "urban",
"usable", "utterly".

    
    """
)

st.write(
    """
 (V)"vacate", "valor", "valuable", "variety", "vast", "vehicle", "venom", "verdict",
"vibrant", "victor", "vinegar", "violence", "visiting", "visual", "vocal", "vowel", "voyage", "vulture".
    
    """
)

st.write(
    """
 (W)"wakeful", "waltz", "watermelon", "weather", "welcome", "westerly", "whitener", "wholesome", "wisdom", "worrisome",
"writing".


    """
)

st.write(
    """
 (X)"xylem".
    
    """
)

st.write(
    """
 (Y)"yank", "yardage", "yearly", "yoga", "youthful".
    
    """
)

st.write(
    """
 (Z)"zap", "zest", "zookeeper".
    
    """
)
