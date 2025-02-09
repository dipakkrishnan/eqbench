import numpy as np

def euclidean_distance(vec1: list[float]: , vec2: list[float]):
    return np.linalg.norm(np.array(vec1) - np.array(vec2))

def cosine_similarity(vec1: list[float]: , vec2: list[float]):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
