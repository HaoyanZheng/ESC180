import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)  # find the length of the vector


def cosine_similarity(vec1, vec2):
    vec1set =set()
    vec2set =set()

    for key1 in vec1:
        vec1set.add(key1)
    for key2 in vec2:
        vec2set.add(key2)

    same = vec1set.intersection(vec2set)


    product = 0
    for words in same:
        product += vec1[words] * vec2[words]


    return product/(norm(vec1)*norm(vec2))

def build_semantic_descriptors(sentences):

    worddict = {}

    for sentence in sentences:
        stored = list(set(sentence))
        for words in stored:
            if words in worddict:
                for the_words in stored:
                    if the_words != words:
                        if the_words not in worddict[words]:
                            worddict[words][the_words] = 1
                        else:
                            worddict[words][the_words] += 1

            else:
                worddict[words] = {}
                #many_words = {}
                for the_words in stored:
                    if the_words != words:
                        if the_words not in worddict[words]:
                            worddict[words][the_words] = 1
                        else:
                            worddict[words][the_words] += 1

                    # worddict[words] = many_words


    return worddict


def build_semantic_descriptors_from_files(filenames):

    file_content = ""
    place = []

    for file in filenames:

        f = open(file, "r", encoding="latin1")
        file_content += f.read()

    file_content = file_content.lower()


    file_content = file_content.replace(",", " ")
    file_content = file_content.replace("-", " ")
    file_content = file_content.replace("--", " ")
    file_content = file_content.replace('"', " ")
    file_content = file_content.replace("'", " ")
    file_content = file_content.replace(":", " ")
    file_content = file_content.replace(";", " ")
    file_content = file_content.replace("!", ".")
    file_content = file_content.replace("?", ".")

    file_content = file_content.split(".")

    for item in file_content:
        place.append(item.split())







    return build_semantic_descriptors(place)



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    similarity_list = []
    max_similarity = -1

    if word not in semantic_descriptors:
        return choices[0]


    for choice in range(len(choices)):


        if choices[choice] not in semantic_descriptors:
            similarity = -1
            similarity_list.append(similarity)


        else:
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[choice]])
            similarity_list.append(similarity)

        max_similarity_index = similarity_list.index(max(similarity_list))
        most_word = choices[max_similarity_index]

    return most_word






def run_similarity_test(filename, semantic_descriptors, similarity_fn):


    correctness = 0.0
    question_list = []
    file_content = open(filename, "r", encoding="latin1")
    file_content = file_content.read()
    file_content = file_content.lower()
    file_content = file_content.strip("\ufeff")
    file_content = file_content.split("\n")



    for the_question_set in file_content:

        if the_question_set != "":
            question_list.append(the_question_set.split())

    for set_of_question in question_list:

        if most_similar_word(set_of_question[0], set_of_question[2:], semantic_descriptors, similarity_fn) == set_of_question[1]:
            correctness += 1

    percentage_correctness = (correctness/len(question_list))*100

    return percentage_correctness


# sem_descriptors = build_semantic_descriptors_from_files(["project1.txt", "project2.txt"])
# res = run_similarity_test ("test.txt", sem_descriptors, cosine_similarity)
# print(res, "of the guesses were correct")