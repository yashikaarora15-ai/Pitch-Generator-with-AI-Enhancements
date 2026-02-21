import re

# -----------------------------
# 1. Clean user input fields
# -----------------------------
def clean_input(text):
    if not text:
        return ""

    # Remove extra spaces
    text = " ".join(text.strip().split())

    # Capitalize first letter
    text = text[0].upper() + text[1:] if len(text) > 1 else text.upper()

    return text


# -----------------------------
# 2. Fix article issues (a/an)
# -----------------------------
def fix_articles(text):
    return re.sub(r'\ba ([aeiouAEIOU])', r'an \1', text)


# -----------------------------
# 3. Remove duplicate punctuation
# -----------------------------
def fix_punctuation(text):
    text = re.sub(r'[.]{2,}', '.', text)
    text = re.sub(r'[,]{2,}', ',', text)
    text = re.sub(r'[!]{2,}', '!', text)
    return text


# -----------------------------
# 4. Final sanitizer
# -----------------------------
def sanitize_pitch(text):
    text = fix_articles(text)
    text = fix_punctuation(text)
    text = " ".join(text.split())  # final spacing cleanup
    return text