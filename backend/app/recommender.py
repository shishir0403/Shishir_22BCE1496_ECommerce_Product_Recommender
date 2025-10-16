from app.db import get_all_products
from difflib import SequenceMatcher
import math

# Optional: use OpenAI embeddings if you want super smart AI matching
# Uncomment if you have an OpenAI API key
# from openai import OpenAI
# client = OpenAI(api_key="your-openai-key-here")


def recommend_products(product_id: int):
    """
    Recommend products similar to the selected one based on:
    1. Category similarity
    2. Text description similarity
    """

    products = get_all_products()
    selected = next((p for p in products if p["id"] == product_id), None)

    if not selected:
        return []

    # Step 1: Get category-matching products
    same_category = [
        p for p in products
        if p["category"] == selected["category"] and p["id"] != selected["id"]
    ]

    # Step 2: If enough matches in category → return top 5
    if len(same_category) >= 5:
        return same_category[:5]

    # Step 3: Otherwise, use description similarity
    def similarity(a, b):
        return SequenceMatcher(None, a, b).ratio()

    scored = [
        (p, similarity(selected["description"], p["description"]))
        for p in products if p["id"] != selected["id"]
    ]

    # Sort by similarity score (descending)
    scored.sort(key=lambda x: x[1], reverse=True)

    # Step 4: Return top 5 similar items
    recommendations = [p for p, score in scored[:5]]
    return recommendations


# 🔵 OPTIONAL: Use real embeddings (OpenAI)
"""
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def cosine_similarity(vec1, vec2):
    dot = sum(a*b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a*a for a in vec1))
    norm2 = math.sqrt(sum(a*a for a in vec2))
    return dot / (norm1 * norm2)


def recommend_products(product_id: int):
    products = get_all_products()
    selected = next((p for p in products if p["id"] == product_id), None)
    if not selected:
        return []

    selected_emb = get_embedding(selected["title"] + " " + selected["description"])

    scored = []
    for p in products:
        if p["id"] == selected["id"]:
            continue
        emb = get_embedding(p["title"] + " " + p["description"])
        score = cosine_similarity(selected_emb, emb)
        scored.append((p, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return [p for p, score in scored[:5]]
"""
