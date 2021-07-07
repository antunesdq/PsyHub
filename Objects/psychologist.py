class psychologist():
    def __init__(self, db, psi_nome, psi_email, psi_celular, psi_senha, psi_CPF, psi_CRP, psi_nascimento, psi_endereco):
        self.db = db
        self.psi_nome = psi_nome
        self.psi_email = psi_email
        self.psi_celular = psi_celular
        self.psi_senha = psi_senha
        self.psi_CPF = psi_CPF
        self.psi_CRP = psi_CRP
        self.psi_nascimento = psi_nascimento
        self.psi_endereco = psi_endereco
        
    def post(self):
        return self.db.cursor.execute(f"""INSERT INTO `psicologo`(
        `psi_nome`,
        `psi_email`,
        `psi_celular`,
        `psi_senha`,
        `psi_CPF`,
        `psi_CRP`,
        `psi_nascimento`,
        `psi_endereco`) VALUES(
        {self.psi_nome},
        {self.psi_email},
        {self.psi_celular},
        {self.psi_senha},
        {self.psi_CPF},
        {self.psi_CRP},
        {self.psi_nascimento},
        {self.psi_endereco});""")

    def get(self):
        return self.db.cursor.execute(f"""SELECT * from psicologo;""")