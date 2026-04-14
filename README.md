# SocialMedia Content Sanitizer
This project implements a Content Moderation System for a school-based social media platform. The goal is to ensure a safe and controlled online environment by automatically screening user-generated content before publication.
# Key Features
Word Filtering & Masking
Detects banned words such as bad, toxic, hate
Replaces them with *** to sanitize content
Link Extraction
Identifies URLs starting with http
Stores extracted links in a separate file (links_found.txt) for security review
Post Processing
Processes a list of user posts efficiently
Differentiates between clean and flagged content
User Activity Tracking
Maintains a dictionary to track how many times each user triggers moderation
Final Report Generation
# Displays summary:
Total Posts Screened: X | Cleaned: Y | Blocked: Z
# Business Value
Ensures safe digital communication for students
Prevents abusive language and malicious links
Provides basic analytics for moderation tracking
Can be extended into real-world moderation systems
# Tech Stack
Python (Core)
File Handling
String Processing
Dictionaries & Lists
# Output Files
links_found.txt → Stores extracted URLs
Cleaned posts → Displayed in console
# Use Case
Ideal for:
Educational platforms
Beginner Python projects
Content moderation prototypes
