# =================================================================
# PROJECT: AI-Powered Recommendation Engine
# DESCRIPTION: A Content-Based Filtering engine for movie suggestions.
# DELIVERABLE: Python-based backend with recommendation endpoints.
# =================================================================

import math

class RecommendationEngine:
    def __init__(self):
        # Sample Dataset: Movies with Genre Tags (Binary representation)
        # [Action, Sci-Fi, Comedy, Drama]
        self.movies = {
            "Inception":    [1, 1, 0, 0],
            "The Matrix":   [1, 1, 0, 0],
            "The Hangover": [0, 0, 1, 0],
            "Interstellar": [0, 1, 0, 1],
            "Deadpool":     [1, 0, 1, 0],
            "Joker":        [0, 0, 0, 1]
        }
        print("🤖 AI Recommendation Engine Initialized...")

    def cosine_similarity(self, v1, v2):
        """Calculates the similarity between two movie vectors."""
        sum_xx, sum_yy, sum_xy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sum_xx += x*x
            sum_yy += y*y
            sum_xy += x*y
        
        denominator = math.sqrt(sum_xx) * math.sqrt(sum_yy)
        return sum_xy / denominator if denominator != 0 else 0

    def get_recommendations(self, movie_name):
        """API Endpoint Simulation: Returns top 2 similar movies."""
        if movie_name not in self.movies:
            return f"❌ Error: Movie '{movie_name}' not in database."

        target_vector = self.movies[movie_name]
        scores = []

        for name, vector in self.movies.items():
            if name != movie_name:
                similarity = self.cosine_similarity(target_vector, vector)
                scores.append((name, similarity))

        # Sort by similarity score (highest first)
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:2]

# --- MAIN EXECUTION (API SIMULATION) ---
if __name__ == "__main__":
    engine = RecommendationEngine()

    # User Input / API Call
    user_choice = "Inception"
    print(f"\n📡 API REQUEST: Fetching recommendations for '{user_choice}'...")
    
    recommendations = engine.get_recommendations(user_choice)

    print("\n"
