from config import prefixes, suffixes
def extract_links(text):
    links = []
    words = text.split()
    for word in words:
        if word.startswith("http"):
            links.append(word)

    return links
# -----------------------------
# CLEAN TEXT FUNCTION
# -----------------------------
def clean_text(text, banned_words):
    words = text.split()
    new_words = []

    for word in words:
        # keep links unchanged
        if word.startswith("http"):
            new_words.append(word)
            continue

        stripped = word.strip(".,!?;:")
        lower = stripped.lower()

        for bad in banned_words:

            # 1. EXACT MATCH
            if lower == bad:
                word = word.replace(stripped, "***")
                break

            # 2. SUFFIX CASE (bad + suffix)
            elif lower.startswith(bad):
                suffix = lower[len(bad):]

                if suffix in suffixes:
                    word = word.replace(stripped, "***" + suffix)
                    break

            # 3. PREFIX CASE (prefix + bad)
            elif lower.endswith(bad):
                prefix = lower[:-len(bad)]

                if prefix in prefixes:
                    word = word.replace(stripped, prefix + "***")
                    break

        new_words.append(word)

    return " ".join(new_words)