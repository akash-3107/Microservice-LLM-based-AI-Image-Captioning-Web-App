import wikipedia

def get_context_from_caption(caption: str, max_articles=2):
    keywords = extract_keywords(caption)
    context = []

    for kw in keywords[:max_articles]:
        try:
            summary = wikipedia.summary(kw, sentences=2)
            context.append(f"{kw.title()}: {summary}")
        except Exception:
            continue

    return "\n".join(context)

def extract_keywords(text: str):
    # Simple fallback: pick 2–3 nouns manually
    # You can replace with spaCy for better NLP
    words = text.lower().split()
    stopwords = {"a", "the", "on", "in", "at", "with", "of", "is", "are"}
    keywords = [word for word in words if word not in stopwords and len(word) > 3]
    return list(set(keywords))
