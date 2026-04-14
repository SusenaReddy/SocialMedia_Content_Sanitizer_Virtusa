def generate_report(total, cleaned, blocked, links, user_flags):
    with open("data/report.txt", "w") as f:
        f.write("SOCIAL MEDIA CONTENT MODERATION REPORT\n")
        f.write("=" * 45 + "\n\n")
        f.write(f"Total Posts: {total}\n")
        f.write(f"Cleaned Posts: {cleaned}\n")
        f.write(f"Blocked Posts: {blocked}\n")
        f.write(f"Total Links Found: {len(links)}\n\n")