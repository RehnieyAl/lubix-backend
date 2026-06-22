from sqlalchemy.orm import Session
from app.models.ModelUser import Users
from app.models.ModelProduct import Product, Catalog
from fastapi import HTTPException
import json

def create_product_service(
        user_id,
        nameProduct,
        nameCatalog,
        priceProduct,
        stockProduct,
        descripcionProduct,
        technicalSpecProduct,
        imagesProduct,
        nas,
        database: Session
    ):

    try:

        search_user = database.query(Users).filter(Users.id == user_id).first()
        
        if not search_user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        
        company = search_user.company
        
        if not company:
            raise HTTPException(status_code=401, detail="Empresa no encontrado")
    
        if nameCatalog:
            search_catalog = database.query(Catalog).filter(Catalog.name == nameCatalog).first()
            
            if not nameCatalog:
                raise HTTPException(status_code=401, detail="Este catalogo no existe")
        
        print("Esto es solo una prueba")
        print("Name user", search_user.fullName)
        print("id compañia: ", company.id)
        print("Nombre compañia: ", company.nameCompany)
        print("Id de catalogo: ", search_catalog.id)
        print("Nombre catalogo: ", search_catalog.name)

        image_urls = []
        technical_spec = {}

        if technicalSpecProduct:
            if isinstance(technicalSpecProduct, str):
                technical_spec = json.loads(technicalSpecProduct)
            else:
                technical_spec = technicalSpecProduct


        if imagesProduct:
            for file in imagesProduct:
                url = nas.upload_file(file, f"companies/{company.CompanyNIT}/imagesProduct/")
                image_urls.append(url["path"])
        
        new_product = Product(
            name=nameProduct,
            price=priceProduct,
            images= image_urls,
            stock=stockProduct,
            descripcion=descripcionProduct,
            technical_spec=technical_spec,
            company_id = company.id,
            catalog_id = search_catalog.id
        )

        database.add(new_product)
        database.commit()
        database.refresh(new_product)

        return {
            "messaje": "producto guardado exitosamente",
            "id": new_product.id,
            "nameProduct": new_product.name,
            "price": new_product.price,
            "stock": new_product.stock,
            "categorie": new_product.catalog_id,
            "descripcion": new_product.descripcion,
            "technicalSpec": new_product.technical_spec,
            "imagesProduct": new_product.images
        }
    
    except Exception as e:
        database.rollback()
        return {"error": str(e)}
    
    
def update_product_service():
    pass

def delete_product_service():
    pass

