class Contract:
    def __init__(self, projetista, data, contrato, contratante, endereco, email, cpfcnpj):
        self.projetista = projetista
        self.data = data
        self.contrato = contrato
        self.contratante = contratante
        self.endereco = endereco
        self.email = email
        self.cpfcnpj = cpfcnpj
    
    def __str__(self):
        return f"\nprojetista={self.projetista}\ndata={self.data}\ncontrato={self.contrato}\ncontratante={self.contratante}\nendereco={self.endereco}\nemail={self.email}\ncpfcnpj={self.cpfcnpj}"

    def to_dict(self):
        return {
            "projetista": self.projetista,
            "data": self.data,
            "contrato": self.contrato,
            "contratante": self.contratante,
            "endereco": self.endereco,
            "email": self.email,
            "cpfcnpj": self.cpfcnpj,
        }