
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import Product
from backend.schemas import ProductCreate
from backend.auth import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).filter(
        Product.is_active == True
    ).all()

    return products


@router.post("/")
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admins can add products"
        )

    product = Product(
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock,
        low_stock_threshold=data.low_stock_threshold,
        category=data.category
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return {
        "message": "Product created successfully",
        "product": {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "category": product.category
        }
    }