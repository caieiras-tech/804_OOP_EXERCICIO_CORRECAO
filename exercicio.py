class Pessoa:

    def __init__(self, nome, genero, email, idade, cpf):
        self.nome = nome
        self.genero = genero
        self.email = email
        self.idade = idade
        self.cpf = cpf

    def imprimir_dados(self):
        print(f'Nome -> {self.nome} \n'
              f'Gênero -> {self.genero} \n'
              f'E-mail -> {self.email} \n'
              f'Idade -> {self.idade} \n'
              f'Cpf -> {self.cpf}')


class Paciente(Pessoa):

    def __init__(self, sintoma, nome, genero, email, idade, cpf):
        super().__init__(nome, genero, email, idade, cpf)
        self.sintoma = sintoma

    def imprimir_sintoma(self):
        return print('Sintomas: ' + self.sintoma)


class Medico(Pessoa):

    def __init__(self, crm, nome, genero, email, idade, cpf):
        super().__init__(nome, genero, email, idade, cpf)
        self.crm = crm

    def imprimir_crm(self):
        return print('CRM: ' + self.crm)


print('________________________PACIENTE______________________________')
paciente = Paciente('Pneumonia', 'Groger', 'm', 'groger@mastertech.tech', 52, '837824783748')
paciente.imprimir_dados()
paciente.imprimir_sintoma()

print('______________________MEDICO_________________________________')
medico =  Medico('272671', 'Raul', 'm', 'raul@mastertech.tech', 52, '837824783748')
medico.imprimir_crm()
medico.imprimir_dados()