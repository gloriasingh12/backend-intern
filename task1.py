# =================================================================
# PROJECT: Blog Backend System (Memory-Persistence Version)
# DESCRIPTION: Fixed sqlite3.OperationalError for Online Compilers.
# DELIVERABLE: A functional API logic using In-Memory SQLite.
# =================================================================

import sqlite3
import hashlib

class BlogBackend:
    def __init__(self):
        # FIXED: Using ':memory:' instead of a filename to avoid permission errors
        self.conn = sqlite3.connect(':memory:') 
        self.create_tables()
        print("📁 Database Connected: [In-Memory Mode] (No file errors!)")

    def create_tables(self):
        """Creates tables for Users, Posts, and Comments."""
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                          (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts 
                          (id INTEGER PRIMARY KEY, author TEXT, title TEXT, content TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS comments 
                          (id INTEGER PRIMARY KEY, post_id INTEGER, commenter TEXT, comment TEXT)''')
        self.conn.commit()

    def register_user(self, username, password):
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        self.conn.commit()
        print(f"👤 User '{username}' registered successfully.")

    def create_post(self, author, title, content):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO posts (author, title, content) VALUES (?, ? , ?)", (author, title, content))
        self.conn.commit()
        print(f"📝 Blog Created: '{title}' by {author}")

    def add_comment(self, post_id, commenter, comment):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO comments (post_id, commenter, comment) VALUES (?, ?, ?)", 
                       (post_id, commenter, comment))
        self.conn.commit()
        print(f"💬 Comment added by {commenter} on Post ID {post_id}")

    def get_blog_feed(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        print("\n--- 🌐 BLOG FEED ---")
        for post in posts:
            print(f"\n[{post[0]}] {post[2]} | Author: {post[1]}")
            cursor.execute("SELECT commenter, comment FROM comments WHERE post_id=?", (post[0],))
            comments = cursor.fetchall()
            for c in comments:
                print(f"   -> {c[0]}: {c[1]}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    app = BlogBackend()
    app.register_user("aditya_tripathi", "secure_pass_123")
    app.create_post("aditya_tripathi", "My NLP Internship Journey", "17 tasks and counting!")
    app.add_comment(1, "rahul_qa", "Great job on the tasks, Aditya!")
    app.get_blog_feed()
    print("\n✅ Task 17 Fixed & Complete.")
