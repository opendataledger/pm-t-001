import streamlit as st
import requests
from navigation import make_sidebar, check_user_inactivity  # Import necessary functions and sidebar functions

# Check for inactivity and logout if necessary
check_user_inactivity()

# Add sidebar
make_sidebar()

st.title(" 📝 5th-6th Grade - List of Words")

st.write("(*Users are logged out after 15 minutes of inactivity!)")

# Streamlit interface for the test
st.write(
    """
(A)"abbreviate", "abnormality", "abode", "abrasion", "abundantly", "academic",
    "accessory", "accordion", "acidic", "acne", "acrobat", "adhesive",
    "admirable", "adoption", "adversary", "affected", "affliction", "affordable",
    "agenda", "airport", "alimony", "allergic", "alliance", "alpaca",
    "alphabetical", "amateur", "amplify", "amusing", "animate", "anklebone",
    "annex", "antibacterial", "antibiotic", "anxiety", "apparition", "appease",
    "applause", "aptitude", "aquamarine", "arcade", "arrangement", "assortment",
    "athletic", "attractive", "auditory", "avalanche", "avocado",

    """
)

st.write(
    """
 (B)"badminton", "balky", "Ballyhoo", "barbarian", "bareback", "bargain", "barrette",
    "bashfulness", "beacon", "bedazzle", "bedridden", "beforehand", "behavior",
    "believable", "beneficial", "benevolent", "biannual", "bicultural", "bicycle",
    "billionaire", "bimonthly", "biodiversity", "bionics", "birthmark", "blamable",
    "blarney", "blissful", "blistering", "bluebonnet", "bolster", "bonfire",
    "boomerang", "botulism", "boulevard", "bountiful", "braggart", "braille",
    "brainstorm", "brilliance", "brisket", "brooch", "buffered", "buffoonery",
    "bulbous", "bureau", "burglarize",
    
    """
)

st.write(
    """
 (C)"calculate", "calendar", "canopy", "capitalism", "cardiac", "carnation", "cartridge",
    "cataract", "cavernous", "centimeter", "ceremony", "chaplain", "charitable", "choppiness",
    "cinema", "circulation", "circumstance", "clearance", "clergy", "clincher", "closure",
    "cohesion", "coincidence", "colander", "columnist", "combustion", "commercial",
    "communicable", "commute", "complaint", "concentrate", "concerto", "confirmed",
    "congratulate", "connection", "connive", "consultation", "convention", "convoy", "corrode",
    "corruption", "cramming", "creative", "critical", "curiosity", "currency", "curtail",
    
    """
)

st.write(
    """
 (D)"damask", "dauntless", "debonair", "debt", "decagon", "deceit", "declining", "deductible",
    "deflate", "deformity", "dehydrate", "delivery", "democracy", "deodorant", "desperate", 
    "detestable", "development", "devotion", "diagram", "dictation", "dietary", "diligent",
    "diorama", "discipline", "discreet", "disembark", "disinfect", "dispensable", "disregard",
    "district", "divergence", "doleful", "domain", "dominance", "dosage", "downcast", 
    "draftsman", "drone", "dumpling", "dwindle", "dynasty",
    
    """
)

st.write(
    """
 (E)"earliest", "earphone", "earsplitting", "editorial", "effective", "egoism", "elaborate", 
    "elapse", "elasticity", "electromagnet", "eligible", "emanate", "embroidery", "emergency", 
    "emotional", "employee", "encore", "endear", "endurance", "energetic", "engagement", 
    "enjoyably", "enormity", "entirety", "environment", "episode", "equate", "erase", 
    "escapism", "estimate", "ethical", "everglade", "evict", "evidence", "excel", "exercising", 
    "exhale", "existence", "expenditure", "experience", "exploration", "expound", "extremity",
    
    """
)

st.write(
    """
 (F)"fabulous", "facedown", "factorization", "famish", "fanciful", "fatalism", "fattened", 
    "federalist", "feminine", "ferocious", "fiberglass", "fictionalize", "fidelity", "fiercely",
    "filbert", "filtration", "flagrant", "flatterer", "flounce", "food chain", "footbridge", 
    "foreclose", "foreign", "forerunner", "forgery", "forgetfulness", "formative", "fortitude",
    "foyer", "fraction", "fragile", "fragrance", "frankfurter", "fraternity", "freebie",
    "freedbee", "freedom", "frontier", "functional", "funeral", "furlough", "fuzziness",
    
    """
)

st.write(
    """
 (G)"gangplank", "gasoline", "gaudy", "gauze", "gearless", "gemstone", "generality", 
    "generation", "genetic", "geographical", "geometric", "giddy", "gingerly", "glacier", 
    "gloominess", "gluttony", "goldenrod", "good-humored", "goodwill", "gooseneck", 
    "gorgeous", "govern", "gradually", "graffiti", "granola", "graphic", "gravitation", 
    "greasier", "greatness", "greengrocer", "griminess", "grinning", "grizzled", "grouchy", 
    "guidance", "guidebook", "gumbo", "gurgle",
    
    """
)

st.write(
    """
 (H)"habitable", "haggard", "hamstring", "handicapped", "handily", "handlebar", "happiness",
    "happy-go-lucky", "harmfully", "hatchery", "hauntingly", "heatedly", "heather",
    "heatstroke", "hedgehog", "heighten", "henceforth", "hepatitis", "herbicide","hexagon", 
    "hibachi", "hideous", "hindrance", "hoist", "hominid", "homophone", "honeycomb", 
    "hoopskirt", "horoscope", "hotheaded", "hovercraft", "humidity", "hummingbird", 
    "husbandry", "hydrology", "hyena", "hygienic", "hyphen", "hypnosis", "hysterics",
    
    """
)

st.write(
    """
 (I)"icicle", "idealism", "identical", "ideology", "ignoring", "illegal", "imaginable", 
    "imitative", "immense", "immodest", "immovable", "impassable", "impeach", "impossible", 
    "improper", "improvise", "incidence", "incision", "inconvenience", "indecision", 
    "independent", "indicator", "inedible", "infatuate", "inferior", "inherent", 
    "injustice", "innovative", "instructor", "insulation", "insurance", "interesting", 
    "intermittent", "internist", "intrusive", "inventory", "invigorate", "invitation", 
    "irrational", "irrigation", "issue",
    
    """
)

st.write(
    """
 (J)"jaguar", "jamboree", "jawbreaker", "jellyfish", "jetty", "jitterbug", "jobholder", 
    "joggled", "joist", "jubilation", "juniper", "justify",
    
    """
)

st.write(
    """
 (K)"kelp", "kernel", "kidney", "kindhearted", "kinship", "Kleenex", "knighthood", 
    "knitting", "knockabout",
    
    """
)

st.write(
    """
 (L)"laboratory", "lacerate", "lamentation", "laminate", "landline", "languid", "larceny", 
    "lattice", "lawlessly", "layette", "league", "leastwise", "leathery", "lectern", 
    "leeway", "legality", "legislature", "leisure", "lemon", "levelheaded",
    "licorice", "lifeline", "light-year", "limerick", "lineage", "liquefy",
    "listener", "lobbyist", "locality", "loneliness", "loose", "lottery", "loudmouth",
    "lumberyard", "luminescent", "luxurious", "lynx",
    
    """
)

st.write(
    """
 (M)"magnetic", "magnolia", "mainstream", "maize", "malefactor", "malformation", 
    "malicious", "manageable", "marathon", "mascara", "masterful", "materialize", 
    "maturity", "maximum", "Maya", "meaningful", "medication", "meditative", "melodrama", 
    "membrane", "memorial", "mercenary", "merchant", "metallic", "meteorologist", 
    "migratory", "miniature", "minivan", "minority", "misconception", "misguidance", 
    "misspend", "mistletoe", "mistrust", "monitor", "monotone", "mosquito", "motley", 
    "multitude", "murmur", "mutate",
    
    """
)

st.write(
    """
 (H)"nape", "narcotic", "narrator", "nationalism", "natural resource", "navigable", 
    "navigator", "necessitate", "needful", "neglectful", "negotiate", "neighborhood", 
    "nervy", "nethermost", "nettle", "neutralize", "newcomer", "newspaperman", "nifty", 
    "nightly", "ninepin", "nitpick", "noiseless", "nonchalant", "nonprofit", "nonsense", 
    "nonverbal", "nonviolence", "normalize", "northeasterly", "nostalgic", "notoriety", 
    "nougat", "novitiate", "nozzle", "nuisance", "numeral", "nurturant", "nuthatch", 
    "nutlet", "nutriment",
    
    """
)

st.write(
    """
 (O)"obese", "obeying", "obituary", "oblivious", "obscure", "observant", "obviously",
    "occupation", "odometer", "Offertory", "officiate", "olive", "ominous", "onslaught", 
    "opacity", "openhearted", "operating", "opposable", "optimal", "optometry", "orate", 
    "orbiter", "orderliness", "ordinary", "oregano", "organic", "original", "ornery", 
    "outburst", "outlying", "outwardly", "outweigh", "overestimate", "override", 
    "oversupply", "oxygen",
    
    """
)

st.write(
    """
 (P)"packaging", "palpitate", "panhandle", "paradise", "paradox", "parakeet", "paralysis",
    "pathogen", "patriotic", "pedestal", "pedicure", "penalize", "penetrate", "penitence", 
    "pepperoni", "percentage", "perfection", "perilous", "perplexity", "pesticide", 
    "petroleum", "pictorial", "pineapple", "pinkie", "pinky", "plaintiff", "plasticity", 
    "poisonous", "policyholder", "polyester", "portable", "portfolio", "possession", 
    "practical", "precinct", "predestine", "predicament", "proactive", "problematic", 
    "proceed", "profession", "prosperous", "puzzling",
    
    """
)

st.write(
    """
 (Q)"quaintness", "qualm", "quarantine", "quarterback", "queasier", "quick bread",
    "quince", "quitting", "quizzes",
    
    """
)

st.write(
    """
 (R)"racketeer", "radiantly", "radical", "railroad", "ramshackle", "raspy", "rationale", 
    "realistic", "reasoning", "reassure", "rebroadcast", "rebuttal", "receive", 
    "recession", "reconcile", "reconstruct", "rectangular", "reference", "refrigerate", 
    "regardless", "regiment", "relentless", "relevant", "reluctantly", "remnant", 
    "replacement", "replica", "reptilian", "respectable", "restaurant", "retort", 
    "retriever", "revenue", "review", "ricotta", "ridiculous", "roadrunner", "rodent", 
    "rollicking", "roughneck", "rowdiness", "rubella", "russet",
    
    """
)

st.write(
    """
 (S)"sabotage", "salsa", "sarcasm", "satisfactory", "scandal", "scarcely", "schedule", 
    "scorekeeper", "scourge", "seasonable", "seclusion", "sectional", "sedative", 
    "seizure", "semiarid", "sensational", "seriously", "seventh", "shrewd", "siesta", 
    "simplicity", "singular", "situation", "skittish", "sociable", "solidify", "solstice",
    "specific", "spectacle", "spectrum", "splendid", "squirm", "statement", "stationary", 
    "stereotype", "strategy", "stubborn", "subjective", "substantial", "summary", 
    "supplement", "survive", "syllabicate", "symbolism", "synthetic",
    
    """
)

st.write(
    """
 (T)"taffeta", "talkative", "tastefully", "taxation", "technician", "telescopic", 
    "temperament", "tension", "terrier", "terrific", "textual", "theatrical", "thermometer", 
    "thesis", "threaten", "thwart", "tightwad", "timberline", "tincture", "tinsel", 
    "toilsome", "tollgate", "tomorrow", "topical", "tousle", "toxemia", "tragedy", 
    "translate", "treasurer", "tremendous", "triangular", "trophy", "trustworthy", 
    "tunnel", "turbojet", "twentieth", "typewriter", "typify",
    
    """
)

st.write(
    """
 (U)"ultima", "unaffected", "unaligned", "unbearable", "unblemished", "unclassified", 
    "underpass", "unenclosed", "uneventful", "uniformity", "university", "unlined", 
    "unplug", "unravel", "unutterable", "uproarious", "usage", "uttermost",
    
    """
)

st.write(
    """
 (V)"vaccinate", "validity", "vandalism", "vanquish", "vaporize", "vegetative", "velocity", 
    "vendetta", "veneer", "venture", "Venus", "version", "veterinarian", "victimize", 
    "vigilant", "vindicate", "visitation", "vitality", "vivid", "vocation", "volcanic", 
    "volume",
    
    """
)

st.write(
    """
 (W)"waistband", "wallaby", "warehouse", "warrant", "wash-and-wear", "waspish", "wearable",
    "web-footed", "wharf", "wheelchair", "wherefore", "white blood cell", "whitening", 
    "wireless", "wisecrack", "wittingly", "woozy", "workmanship",


    """
)

st.write(
    """
 (X)"xylophone",
    
    """
)

st.write(
    """
 (Y)"yacht", "yearling",.
    
    """
)

st.write(
    """
 (Z)"zealous", "zestfully"
    
    """
)


#################################################################################
