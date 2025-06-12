# keyword_dictionary.py

ANCIENT_HISTORY_KEYWORDS = {
    'harappa': 'Indus Valley Civilization',
    'mohenjo-daro': 'Indus Valley Civilization',
    'ashoka': 'Ashokan Edicts',
    'maurya': 'Mauryan Empire',
    'gupta': 'Gupta Period',
    'vedic': 'Vedic Period',
    'buddhism': 'Buddhism',
    'jainism': 'Jainism',
    'kautilya': 'Mauryan Empire',
    'arthashastra': 'Mauryan Empire',
    'rock-cut': 'Rock-cut Architecture',
    'stupa': 'Buddhist Architecture',
    'sangam': 'Sangam Period',
    'chola': 'Chola Dynasty',
    'pallava': 'Pallava Dynasty'
}

MATH_KEYWORDS = {
    'algebra': 'Algebra',
    'calculus': 'Calculus',
    'geometry': 'Geometry',
    'trigonometry': 'Trigonometry',
    'probability': 'Probability',
    'statistics': 'Statistics',
    'linear algebra': 'Linear Algebra',
    'differential equation': 'Differential Equations'
}

PHYSICS_KEYWORDS = {
    'mechanics': 'Mechanics',
    'thermodynamics': 'Thermodynamics',
    'electromagnetism': 'Electromagnetism',
    'optics': 'Optics',
    'relativity': 'Relativity',
    'quantum': 'Quantum Mechanics',
    'newton': 'Newtonian Mechanics',
    'einstein': 'Theory of Relativity'
}

ECONOMICS_KEYWORDS = {
    'microeconomics': 'Microeconomics',
    'macroeconomics': 'Macroeconomics',
    'gdp': 'Gross Domestic Product (GDP)',
    'inflation': 'Inflation',
    'monetary policy': 'Monetary Policy',
    'fiscal policy': 'Fiscal Policy',
    'supply and demand': 'Supply and Demand',
    'market structure': 'Market Structure'
}

# A dictionary to easily access keyword maps by subject name
SUBJECT_KEYWORD_MAPS = {
    'ancient_history': ANCIENT_HISTORY_KEYWORDS,
    'math': MATH_KEYWORDS,
    'physics': PHYSICS_KEYWORDS,
    'economics': ECONOMICS_KEYWORDS
}

def get_keyword_map(subject: str) -> dict:
    """
    Returns the keyword map for a given subject.
    Returns an empty dict if the subject is not found.
    """
    return SUBJECT_KEYWORD_MAPS.get(subject.lower(), {})
