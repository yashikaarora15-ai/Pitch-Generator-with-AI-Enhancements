import re

# -------------------------------------------------
# 1️⃣ Basic whitespace cleanup (safe)
# -------------------------------------------------
def clean_input(text):
    if not text:
        return ""
    
    # Remove extra spaces
    text = " ".join(text.strip().split())
    
    return text


# -------------------------------------------------
# 2️⃣ Fix a/an article intelligently
# -------------------------------------------------
def fix_articles(text):
    # Replace "a apple" → "an apple"
    text = re.sub(r'\b[Aa]\s+([aeiouAEIOU])', r'an \1', text)
    return text


# -------------------------------------------------
# 3️⃣ Fix duplicate punctuation
# -------------------------------------------------
def fix_punctuation(text):
    text = re.sub(r'[.]{2,}', '.', text)
    text = re.sub(r'[,]{2,}', ',', text)
    text = re.sub(r'[!]{2,}', '!', text)
    return text


# -------------------------------------------------
# 4️⃣ Normalize important tech words
# -------------------------------------------------
def normalize_tech_terms(text):
    replacements = {
        r'\bai\b': 'AI',
        r'\bml\b': 'ML',
        r'\bdl\b': 'DL',
        r'\bui\b': 'UI',
        r'\bux\b': 'UX'
    }

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    return text


# -------------------------------------------------
# 5️⃣ Capitalize 
# -------------------------------------------------
def capitalize_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    formatted = []

    for s in sentences:
        if s:
            formatted.append(s[0].upper() + s[1:])
        else:
            formatted.append(s)

    return " ".join(formatted)
# -------------------------------------------------
# 6️⃣ Final Pitch Sanitizer
# -------------------------------------------------
def sanitize_pitch(text):
    text = fix_articles(text)
    text = fix_punctuation(text)
    text = normalize_tech_terms(text)
    text = capitalize_sentences(text)
    text = " ".join(text.split())  # final spacing cleanup
    
    return text