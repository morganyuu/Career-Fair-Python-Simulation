# Morgan Yu 261294882
# All code limited to 79 characters per line using wordWrapColumn in VS Code
# Global variables and modules

import math

# Question 1 Utilities first: utils.py
# Part 1.1 get_list

def get_list(s):
    """
    Convert a dash-separated string into a list of cleaned, lowercase tokens.

    Args:
        s (str): Input string with tokens separated by dashes.

    Returns:
        list: List of lowercase, stripped tokens.
    """
    # Split the input string by dash to separate tokens
    token_parts = s.split('-')
    
    token_list = []
    for p in token_parts:
        # Strip whitespace and convert to lowercase
        token = p.strip().lower()
        # Only add non-empty tokens to the list
        if token:
            token_list.append(token)
    
    return token_list

# print(get_list("password management-IT maintenance- computer repair"))
# print(get_list(" python---SQL - etl "))

# Part 1.2 make_vocabulary

def make_vocabulary(items):
    """
    Create a vocabulary list of unique lowercase tokens from a list of token lists.

    Args:
        items (list of list of str): List containing multiple token lists.

    Returns:
        list: List of unique lowercase tokens.
    """
    vocab = []

    # Iterate over each list of tokens
    for item in items:
        # Iterate over each token in the current list
        for token in item:
            # Add token to vocab if its lowercase form is not already present
            if token.lower() not in vocab:
                vocab.append(token.lower())

    return vocab

# print(make_vocabulary([['Python','SQL'],['python','etl', 'sql']]))
# print(make_vocabulary([[], ['a', 'a'], ['b']]))
# print(make_vocabulary([]))

# Part 1.3 vectorize


def vectorize(tokens, vocab):
    """
    Convert a list of tokens into a count vector aligned with the vocabulary.

    Args:
        tokens (list of str): List of tokens to vectorize.
        vocab (list of str): Vocabulary list to align counts with.

    Returns:
        list of int: Count vector where each element corresponds to the count
                     of a vocab token in the input tokens.
    """
    # Normalize all tokens to lowercase for consistent counting
    tokens_lower = [t.lower() for t in tokens]
    
    counts = []
    # Count occurrences of each vocab token in the tokens list
    for v in vocab:
        count = tokens_lower.count(v)  # count occurrences of vocab token
        counts.append(count)
    
    return counts

# vocab = ['etl','python','sql']
# print(vectorize(['python','etl','python'], vocab))
# print(vectorize(['pyThon','ETl','pandas','sql','sql'], vocab))
# print(vectorize([], vocab))

# Part 1.4 cosine_similarity

def cosine_similarity(v1, v2):
    """
    Calculate the cosine similarity between two numeric vectors.

    Args:
        v1 (list of numbers): First vector.
        v2 (list of numbers): Second vector.

    Returns:
        float: Cosine similarity rounded to two decimals. Returns 0.0 if
               either vector is zero-vector. Raises ValueError if lengths differ.
    """
    # Check if vectors have the same length
    if len(v1) != len(v2):
        raise ValueError("v1 and v2 have different lengths")
    
    dot_product_sum = 0

    # Compute dot product of v1 and v2
    for i in range(len(v1)):
        dot_product_sum += v1[i] * v2[i]

    norm_v1 = 0
    norm_v2 = 0

    # Compute squared norms of v1 and v2
    for i in range(len(v1)):
        norm_v1 += v1[i] ** 2
        norm_v2 += v2[i] ** 2

    # Calculate Euclidean norms (magnitudes)
    euclidean_norm_v1 = math.sqrt(norm_v1)
    euclidean_norm_v2 = math.sqrt(norm_v2)

    # Return 0 if either vector has zero magnitude to avoid division by zero
    if euclidean_norm_v1 == 0 or euclidean_norm_v2 == 0:
        return 0.0
    
    # Calculate cosine similarity as dot product divided by product of norms
    cosine_sim = dot_product_sum / ((euclidean_norm_v1) * (euclidean_norm_v2))
    # Round similarity to two decimal places
    sim = round(cosine_sim, 2)
    
    return sim

# print(cosine_similarity([1, 2, 0], [0, 2, 1]))
# print(cosine_similarity([1, 2, 0, 4], [0, 2, 1]))
# print(cosine_similarity([0,0], [5,7]))
# print(cosine_similarity([3,4], [3,4]))



