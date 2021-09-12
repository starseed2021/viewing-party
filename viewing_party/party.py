#WAVE 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    updated_data = user_data["watched"]
    updated_data.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    movies_watched = user_data["watched"]
    movies_to_watch = user_data["watchlist"]
    remove_list = []

    for movie in movies_to_watch:
        if title == movie["title"]:
            movies_watched.append(movie)
            remove_list.append(movie)
      

    for movie in remove_list:
        movies_to_watch.remove(movie)
    
    return user_data

#WAVE 2
def get_watched_avg_rating(user_data):
#   pass
# #STEP 1 CALCULATE THE AVERAGE RATING OF ALL MOVIES IN THE WATCHED LIST
    watched_list = user_data["watched"]["rating"]
    print(f"{watched_list=}")
    score = 0
    for movie in watched_list:
        score += movie
    average_rating = score/len(watched_list)
    return average_rating



# #STEP 2 RETURN THE AVERAGE RATING
    # return average_rating
# def get_most_watched_genre(user_data):
#     pass
#STEP 1 WHICH GENRE IS MOST FREQUENTLY OCCURING IN THE WATCHED LIST
#STEP 2 RETURN THE GENRE 
    # return genre