from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import product_dao
from sql_connection import get_sql_connection

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 allow all origins (for dev only)
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

connection = get_sql_connection()

@app.get("/")
def get_product():
    products = product_dao.get_all_products(connection)
    return {"products": products}
