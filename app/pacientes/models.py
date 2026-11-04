from app import db


class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    citas = db.relationship(
        "Cita",
        back_populates="paciente",
        cascade="all, delete-orphan",
        lazy=True,
    )

    def __repr__(self):
        return f"<Paciente {self.nombre} - {self.telefono}>"