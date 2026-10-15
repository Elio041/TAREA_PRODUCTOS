from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///productos.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price}, stock={self.stock})>"


def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada satisfactoriamente")


def insert_products():
    with app.app_context():
        product1 = Product(name="Teclado", price=120.50, stock=10)
        product2 = Product(name="Mouse", price=75.00, stock=15)
        product3 = Product(name="Monitor", price=950.00, stock=5)

        db.session.add_all([product1, product2, product3])
        db.session.commit()

        print("Productos insertados correctamente")


def query_products():
    with app.app_context():
        print("\nListado de productos")
        products = Product.query.all()

        for item in products:
            print(item)

        print("\nConsulta de un producto por ID")
        product = Product.query.filter_by(id=1).first()

        if product:
            print(product)
        else:
            print("Producto no encontrado")


def update_product():
    with app.app_context():
        print("\nActualización de un producto")
        product = Product.query.filter_by(id=1).first()

        if product:
            product.name = "Teclado Mecánico"
            product.price = 180.00
            product.stock = 20

            db.session.commit()
            print("Producto actualizado:", product)
        else:
            print("Producto no encontrado")


def delete_product():
    with app.app_context():
        print("\nEliminación de un producto")
        product = Product.query.filter_by(id=3).first()

        if product:
            db.session.delete(product)
            db.session.commit()
            print("Producto eliminado correctamente")
        else:
            print("Producto no encontrado")


if __name__ == "__main__":
    #init_db()
    #insert_products()
    #query_products()
    #update_product()
    delete_product()