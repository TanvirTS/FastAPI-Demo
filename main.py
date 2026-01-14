from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get('/')
def greet():
    return "Hello My name is Tanvir"

products = [
    Product(id=1,name="Phone",description="Budget Phone",price=99,quantity=10)
] 

@app.get("/products")
def get_all_products():
    return products

@app.get("/product")
def get_product_by_id():
    return products[0]
