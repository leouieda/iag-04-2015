from fatiando.gravmag import prism
from fatiando.mesher import Prism
from fatiando import gridder
from fatiando.vis import mpl, myv

# Criar um modelo
modelo = [Prism(-100, 100, -200, 200, 0, 500, {'density': 500})]
# Ver o modelo
myv.figure()
myv.prisms(modelo)
myv.show()

# Criar os pontos de observacao
x, y, z = gridder.regular((-500, 500, -500, 500), (100, 100), z=-10)
# Calcular a anomalia gerada pelo modelo nesses pontos
gz = prism.gz(x, y, z, modelo)
# Mapear a anomalia
mpl.contourf(y, x, gz, (100, 100), 30, cmap="Reds")
mpl.colorbar().set_label('mGal')
mpl.show()
