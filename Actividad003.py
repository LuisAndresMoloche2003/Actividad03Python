class Cliente():
    codigo = []
    nombre = []
    apellido = []
    pais = []

    def IngresarDatos(self,nom,ape,pa):

        self.nombre.append(nom)
        self.apellido.append(ape)
        self.pais.append(pa)
        codigo = len(self.nombre)
        for item in range(codigo):
            item += 1
        self.codigo.append(f'Cl-{codigo}')

    def Verificacion(self,cod):
        if cod in self.codigo:
            print('Codigo existente')
            True
        else:
            print('el codigo no existe')
            False



class Usuario(Cliente):
    usuario=[]
    password=[]
    estado=[]
    codcliente=[]

    def NuevoUsuario(self,cod,usu,pas,est):
        if cod in self.codigo:
            self.codcliente.append(cod)
            self.usuario.append(usu)
            self.password.append(pas)
            self.estado.append(est)
        else:
            print('Codigo de usuario no registrado')

    def VerifUsuario(self,usu):
        if usu in self.usuario:
            print('Usuario registrado')
        else:
            print('Usuario no registrado')

    def RecuperarCredenciales(self,cod):
        if cod in self.codigo:
            indice = self.codigo.index(cod)
            us= self.usuario[indice]
            pa= self.password[indice]
            print(f'Su usuario es : {us} y su contraseña: {pa}')

        elif cod in self.usuario:
            indice = self.usuario.index(cod)
            pa = self.password[indice]
            print(f'Su contraseña es: {pa}')

        else:
            print('Codigo de cliente o usuario mal ingresado')

    def ValidarCredenciales(self,us,pa):
        if (us in self.usuario) and (pa in self.password):
            print('credenciales validas')
        else:
            print('Credenciales mal ingresados')



cliente = Cliente()
usuario = Usuario()
cliente.IngresarDatos('German','Salcedo','Peru')
cliente.IngresarDatos('Angel','Castilla','Peru')
cliente.IngresarDatos('Luis','Moloche','Peru')
cliente.IngresarDatos('Cielo','Neciosup','Peru')
for item in cliente.codigo:
    print(item)
cliente.Verificacion('Cl-8')
usuario.NuevoUsuario('Cl-1','Germanlml','german123',1)
usuario.NuevoUsuario('Cl-2','Angelco','angel123',0)
usuario.NuevoUsuario('Cl-3','Luismg','luis123',0)
for item in usuario.usuario:
    print(item)
usuario.VerifUsuario('Germanlml')
usuario.RecuperarCredenciales('Cl-1')
usuario.ValidarCredenciales('Germanlml','german123')








