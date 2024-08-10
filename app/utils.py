import spacy
import re

# Load SpaCy's English model
nlp = spacy.load('en_core_web_sm')

def extract_name(text):
    """
    Extracts the first PERSON entity found in the text.
    """
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_email(text):
    """
    Extracts the first email address found in the text.
    """
    email = re.findall(r'\S+@\S+', text)
    if email:
        return email[0]
    return None

# Example usage
if __name__ == "__main__":
    resume_text = """
    John Doe
    john.doe@example.com
    Experienced software engineer with expertise in Python, AI, and machine learning...
    """
    print("Name:", extract_name(resume_text))
    print("Email:", extract_email(resume_text))
