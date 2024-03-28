if __name__ == "__main__":
    watched_movies = {
        "matrix": 9.0,
        "Thor love and thunder": 8.3,
        "green book": 8.3,
        "her": 8.1,
        "the evil dead": 7.8,
        "forrest gump": 9.2,
        "life aquatic": 9.5,
        "life of bryan": 7.9,
        "first blood": 8.9,
    }
    movies_to_watch = {}
    user_name = input("Please enter your name: ")
    users = [user_name]
    while True:
        user_input = input(
            "Enter a name of a movie you've recently watched,“cu” to change user or “q” to quit: "
        )
        match user_input.lower():
            case "q":
                len_users = len(users)
                len_movies_to_watch = len(movies_to_watch)
                if len_users == 1:
                    if len_movies_to_watch > 1:
                        print(
                            f"Well we had one user today going by the name {users[0]} and these were added tomovies_to_watch {movies_to_watch}"
                        )
                    else:
                        print(
                            f"Well we had one user today going by the name {users[0]} and nothing was added to movies_to_watch"
                        )
                elif len_users > 1:
                    if len_movies_to_watch > 1:
                        print(
                            f"Well we had {len_users} users today going by the names: {users} and these were added to movies_to_watch {movies_to_watch}"
                        )
                    else:
                        print(
                            f"Well we had {len_users} users today going by the names: {users} andnothing was added to movies_to_watch"
                        )
                exit()
            case "cu":
                user_name = input("Please enter your name: ")
                users.append(user_name)
            case default:
                user_rating = 0.0
                if user_input in watched_movies:
                    print(
                        f"I've watched that movie as well i rate it {watched_movies[user_input]}"
                    )
                    user_rating = float(input("what's your rating between 1 and 10? "))
                    if abs(user_rating - watched_movies[user_input]) <= 2:
                        print("wow we have similar taste:")
                    else:
                        print("Well i guess we will agree to disagree :)")
                else:
                    user_rating = float(
                        input(
                            "I haven't watched that one yet, how would you rate it on a scale from 1 to 10? "
                        )
                    )

                if user_rating >= 7:
                    movies_to_watch.setdefault(user_name, []).append(
                        {user_input: user_rating}
                    )
                    print(f"The movie {user_input} was added to movies_to_watch list")
                else:
                    print(
                        "Well my minimum is 7 so guess we wont be watching this one soon"
                    )
