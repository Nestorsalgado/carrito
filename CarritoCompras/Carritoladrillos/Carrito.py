from Carritoladrillos.models import Propiedad

#inicializa carrito
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito= self.session.get ("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito= self.session["carrito"]
        else:
            self.carrito = carrito


    #agrega a carrito
    def agregar(self,Propiedad):
        id = str(Propiedad.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "propiedad_id":Propiedad.id,
                "nombre": Propiedad.nombre,
                "acumulado": Propiedad.precio,
                "ladrillos": 1,
                "bandera": 0,
            }
        
        else:
            if self.carrito[id]["ladrillos"] == Propiedad.ladrillos:
                return {"bandera": 1}

                
            else:

                self.carrito[id]["ladrillos"]+=1
                self.carrito[id]["acumulado"]+= Propiedad.precio
        self.guarda_carrito()


#guarda propedades en carrito
    def guarda_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, Propiedad):
        id= str(Propiedad.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guarda_carrito()


    def restar (self, Propiedad):
        id= str(Propiedad.id)
        if id in self.carrito.keys():
            self.carrito[id]["ladrillos"]-=1
            self.carrito[id]["acumulado"]-= Propiedad.precio
            if self.carrito[id]["ladrillos"]<=0: self.eliminar(Propiedad)
            self.guarda_carrito()

    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True