from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_all_products
from app.recommender import recommend_products

app = FastAPI()

# Allow frontend (Vite) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can replace "*" with "http://localhost:5173" for safety
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "E-commerce recommender API is running"}

@app.get("/products")
def get_products():
    products = get_all_products()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products

@app.post("/recommend")
def recommend(data: dict):
    product_id = data.get("product_id")
    if not product_id:
        raise HTTPException(status_code=400, detail="Missing product_id")
    return recommend_products(product_id)
