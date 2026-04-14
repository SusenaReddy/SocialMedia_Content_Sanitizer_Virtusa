# summary.py

def generate_summary(user_flags):
    with open("data/summary.txt", "w") as file:

        file.write("USER MODERATION SUMMARY\n")
        file.write("=" * 40 + "\n\n")

        total_users = len(user_flags)
        total_flags = sum(user_flags.values())

        file.write(f"Total Users: {total_users}\n")
        file.write(f"Total Violations: {total_flags}\n\n")

        file.write("User-wise Violations:\n")

        for user in user_flags:
            file.write(f"{user}: {user_flags[user]}\n")

    print("Summary file created ✔")