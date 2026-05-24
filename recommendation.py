movies = {
    "Action": ["Avengers", "John Wick", "Batman"],
    "Comedy": ["3 Idiots", "Golmaal", "Hera Pheri"],
    "Horror": ["Conjuring", "Annabelle", "IT"],
    "Romance": ["Titanic", "Aashiqui 2", "The Notebook"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Categories:")
for category in movies:
    print("-", category)

while True:
    user_choice = input("\nEnter preferred category: ").title()

    if user_choice in movies:
        print("\nRecommended Movies:\n")

        recommendations = movies[user_choice]

        for i, movie in enumerate(recommendations, start=1):
            print(f"{i}. {movie}")

        break

    else:
        print("Invalid category! Please try again.")