from config import banned_words
from utils import extract_links, clean_text
def process_posts(posts):
    cleaned_posts = []
    links_found = []
    user_flags = {}
    cleaned_count = 0
    blocked_count = 0
    for line in posts:
        parts = line.split(":", 1)
        user = parts[0].strip()
        text = parts[1].strip()
        if user not in user_flags:
            user_flags[user] = 0
        links = extract_links(text)
        links_found.extend(links)
        lower_text = text.lower()
        violations = 0
        for word in banned_words:
            if word in lower_text:
                violations += 1
        if violations >= 3:
            cleaned_text = "POST REMOVED"
            blocked_count += 1
            status = "BLOCKED"
        elif violations > 0:
            cleaned_text = clean_text(text, banned_words)
            cleaned_count += 1
            status = "CLEANED"
        else:
            cleaned_text = text
            status = "SAFE"
        user_flags[user] += violations
        cleaned_posts.append(f"{user}: {cleaned_text}")
    return cleaned_posts, links_found, user_flags, cleaned_count, blocked_count