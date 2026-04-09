# =================================================================
# PROJECT: Real-Time Chat Backend
# DESCRIPTION: Multi-room chat server simulation using WebSocket logic.
# DELIVERABLE: Python-based server handling real-time communication.
# =================================================================

import datetime

class ChatServer:
    def __init__(self):
        # Dictionary to manage multiple rooms: {room_name: [list_of_messages]}
        self.rooms = {
            "General": [],
            "Tech-Support": [],
            "Intern-Squad": []
        }
        print("🚀 Chat Server Started: Listening for WebSocket connections...")

    def broadcast_message(self, room_name, user, message):
        """Simulates sending a message to all users in a specific room."""
        if room_name in self.rooms:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            formatted_msg = f"[{timestamp}] {user}: {message}"
            
            # Storing message in room history
            self.rooms[room_name].append(formatted_msg)
            
            print(f"📡 [Room: {room_name}] New Broadcast -> {formatted_msg}")
        else:
            print(f"❌ Error: Room '{room_name}' does not exist.")

    def get_room_history(self, room_name):
        """Fetches the conversation history for a specific room."""
        print(f"\n--- 💬 History for #{room_name} ---")
        history = self.rooms.get(room_name, [])
        if not history:
            print("No messages yet.")
        for msg in history:
            print(msg)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    server = ChatServer()

    # 1. Simulating users joining and chatting in different rooms
    print("\n--- Real-Time Activity Simulation ---")
    
    # Activity in 'General' Room
    server.broadcast_message("General", "Aditya", "Hey everyone! Task 18 is live.")
    server.broadcast_message("General", "Rahul", "Awesome! Real-time chats are cool.")

    # Activity in 'Intern-Squad' Room
    server.broadcast_message("Intern-Squad", "Priya", "Has anyone finished the documentation?")
    server.broadcast_message("Intern-Squad", "Aditya", "Almost done, just 2 more tasks to go!")

    # 2. Displaying Room Logs (The 'Chat History' feature)
    server.get_room_history("General")
    server.get_room_history("Intern-Squad")

    print("\n" + "="*45)
    print("✅ Task 18 Complete: Multi-room Chat Logic implemented.")
    print("STATUS: WebSocket Simulation Successful.")
    print("="*45)
