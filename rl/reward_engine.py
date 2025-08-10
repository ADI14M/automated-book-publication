from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def reward_function(original, rewritten):
    orig_vec = model.encode([original])
    rewrite_vec = model.encode([rewritten])
    score = cosine_similarity(orig_vec, rewrite_vec)[0][0]
    reward = 1 - score  # Encourage creative rewriting
    return reward
