class session():
    def __init__(self, db, evo_id, pac_id, numero_sessao, datetime_inicio, datetime_termino, prodecimentos, sintese, observacao, plan_prox_sessao):
        self.db = db
        self.evo_id = evo_id
        self.pac_id = pac_id
        self.numero_sessao = numero_sessao
        self.datetime_inicio = datetime_inicio
        self.datetime_termino = datetime_termino
        self.prodecimentos = prodecimentos
        self.sintese = sintese
        self.observacao = observacao
        self.plan_prox_sessao = plan_prox_sessao
        
    def post(self):
        return self.db.cursor.execute(f"""INSERT INTO `evolucao`(
        `evo_id`,
        `pac_id`,
        `numero_sessao`,
        `datetime_inicio`,
        `datetime_termino`,
        `prodecimentos`,
        `sintese`,
        `observacao`,
        `plan_prox_sessao`) VALUES(
        {self.evo_id},
        {self.pac_id},
        {self.numero_sessao},
        {self.datetime_inicio},
        {self.datetime_termino},
        {self.prodecimentos},
        {self.sintese},
        {self.observacao},
        {self.plan_prox_sessao});""")

    def get(self):
        return self.db.cursor.execute(f"""SELECT * from session;""")