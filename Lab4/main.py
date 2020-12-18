'''
Program ma sugerować podanemu użytkownikowi 7 filmów które powinien obejrzeć i 7
których nie powinien.

Autorzy:
Karol Niemykin
Kacper Kaczor

Instrukcja:
- Pobierz projekt
- Uruchom go w Pycharm
- Zaimportuj biblioteki jeśli występuje błąd
- Uruchom program
- Podaj nazwe użykownika
'''

import numpy as np
import json

#Funkcja wylicza który użytkownik w baziejest dobrym źródłem rekomendacji dla podanego użykownika
def euclidean_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('Cannot find ' + user1 + ' in the dataset')

    if user2 not in dataset:
        raise TypeError('Cannot find ' + user2 + ' in the dataset')

    # Movies rated by both user1 and user2
    common_movies = {}

    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    # If there are no common movies between the users,
    # then the score is 0
    if len(common_movies) == 0:
        return 0

    squared_diff = []

    for item in dataset[user1]:
        if item in dataset[user2]:
            squared_diff.append(np.square(dataset[user1][item] - dataset[user2][item]))

    return 1 / (1 + np.sqrt(np.sum(squared_diff)))



# Funkcja wyświetla polecane / nie polecane filmy ,dla podanego użytkownika
def getRecommendation(bestScore, userDict):
    print('Użytkownik ' + bestScore['user'])

    new_dict = {}
    for key, value in userDict.items():
        if key not in data[user].keys():
            new_dict[key] = value
    sort_dict = dict(sorted(new_dict.items(), key=lambda element: element[1]))
    recommendedMovies = dict(list(sort_dict.items())[-7:])
    notRecommededMovies = dict(list(sort_dict.items())[:7])

    i = 0
    movieList = []

    print('\nPoleca filmy:')
    for item in recommendedMovies:
        print(item + ' | ' + 'ocena: ' + str(recommendedMovies[item]))
        i += 1
        movieList.append(item)

    print('\nNie poleca filmów:')
    for item in notRecommededMovies:
        print(item + ' | ' + 'ocena: ' + str(notRecommededMovies[item]))
        i += 1
        movieList.append(item)
    return movieList

if __name__ == '__main__':

    print("Podaj nazwę użytkownika: ")
    user = input()

    score_type = 'Euclidean'

    ratings_file = 'database.json'
    with open(ratings_file, 'r',encoding="utf-8") as f:
        data = json.loads(f.read())

    scoreList = []
    for item in data:
        if item != user:
            if score_type == 'Euclidean':
                scoreList.append({'score': euclidean_score(data, user, item), 'user': item})

    bestScore = max(scoreList, key=lambda x: x['score'])
    userDict = data[bestScore['user']]
    movieList = getRecommendation(bestScore, userDict)