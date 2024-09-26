class Conta:
    def __init__(self, id, nome, cpf, email, saldo):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._saldo = saldo
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    def __str__(self):
        return (f"\nID: {self.id}"
                f"\nCliente: {self._nome}"
                f"\nCPF: {self._cpf}"
                f"\nEmail: {self._email}"
                f"\nSaldo: {self._saldo}"
                f"\n")