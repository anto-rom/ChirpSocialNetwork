class Usuario:
    def __init__(self, nombre, alias):
        self.nombre = nombre

        if alias.startswith("@"):
            self.alias = alias
        else:
            self.alias = f"@{alias}"

        self.seguidos = []

    def seguir(self, otro_usuario):
        if otro_usuario == self:
            raise ValueError("Un usario no se puede seguir a si mismo.")

        if otro_usuario in self.seguidos:
            raise ValueError("El usuario ya está siendo seguido")
        self.seguidos.append(otro_usuario)

    def sigue_a(self, otro_usuario):
        return otro_usuario in self.seguidos

    @property
    def numero_seguidos(self):
        return len(self.seguidos)

    def a_dict(self):
        return {"nombre": self.nombre, "alias": self.alias}

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["nombre"], datos["alias"])

    def __str__(self):
        return f"{self.nombre} ({self.alias})"

    def __eq__(self, otro_usuario):
        if not isinstance(otro_usuario, Usuario):
            return False
        return self.alias == otro_usuario.alias
