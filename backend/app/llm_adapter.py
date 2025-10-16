def generate_explanation(user, product):
    # In production, this would call your LLM/ChatGPT API
    return f"Recommended {product.name} to {user.name} because of interest in {product.category} items."
