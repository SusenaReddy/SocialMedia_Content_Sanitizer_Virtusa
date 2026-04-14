from moderator import process_posts
from report import generate_report
from summary import generate_summary   # ✅ added

# read input file
with open("data/posts.txt", "r") as f:
    posts = [line.strip() for line in f if line.strip()]  # ✅ avoid empty lines

# process posts
cleaned_posts, links, user_flags, cleaned, blocked = process_posts(posts)

# save cleaned posts
with open("data/cleaned_posts.txt", "w") as f:
    for post in cleaned_posts:
        f.write(post + "\n")

# save links
with open("data/links_found.txt", "w") as f:
    for link in links:
        f.write(link + "\n")

# generate report
generate_report(len(posts), cleaned, blocked, links, user_flags)

# generate summary (separate file)
generate_summary(user_flags)   # ✅ added

print("Processing complete ✔")
print("Check 'data' folder for output files")