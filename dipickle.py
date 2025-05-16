import pickle
def depickle_to_string(pickled_data):
    the_string = ""
    word_list = pickle.loads(pickled_data)
    for x in range(0, len(word_list)):
        print(word_list[x])
    return the_string