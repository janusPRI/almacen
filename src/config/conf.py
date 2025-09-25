AUTHOR= 'JanusDEV'
SITENAME= 'Almacén JANUS'
if 'BRANDNAME' not in locals():
  BRANDNAME= 'Almacén JANUS'
SITEURL= '.' #'https://januspri.github.io/almacen'

if 'SITESUBTITLE' not in locals():
  SITESUBTITLE= "Agricultura Biodinámica" #"Proyecto Rural Integrador" # #Catálogo de productos"

COPYRIGHT_NOTICE= '© 2025 JanusDEV' #+ AUTHOR

if 'WHATSAPPNUM' not in locals():
  WHATSAPPNUM= '542995463130' #711049' #6333410'
if 'EMAIL' not in locals(): 
  EMAIL='info@janus.bio'
if 'COSTODEENVIO' not in locals(): 
  COSTODEENVIO=600


print(EMAIL.split('@'))
def showEMAIL(email):
  return email.replace('@',' @ ')

IMG_DIR='https://www.janus.bio/almacen/imgs/'
# IMG_DIR='../data/imgs/'
IMG_DIR_PRODUCTS=IMG_DIR+"products/w200/"
ImagenMostrador= IMG_DIR+'mostrador-980x515.jpeg'
ImagenSemillas= IMG_DIR+'constelacion-thin.png'
IframeMostrador=''

undesired_articles=[]#"Huevos de GALLINA","Miel Millakó","Sidra de Pera PEER", "Sidra de Manzana Gran SUREÑA","Nueces enteras"]

#from jorge_conf import *
# from encuentro_chacra_conf import *

SHORTCEL=WHATSAPPNUM[2:5]+' '+WHATSAPPNUM[5:]

if 'LINKS' not in locals():
  LINKS = (
    ('Janus Proyecto Rural Integrador', 'http://janus.bio/'),
    # ('Almacén Janus', 'https://almacenjanus.bio/'),
    ('Parador Janus', 'https://janus.bio/parador'),
    ('Semillas Agroecológicas','https://constelacionsemillas.com'),
    ('Mapa: RN 151 ~ km 24,5 ~ Clte Cordero ~ Río Negro ~ ARG','https://g.page/JanusBio?share'),
    ('WhatsApp: '+SHORTCEL,'https://wa.me/'+WHATSAPPNUM),
    ('e-mail: '+showEMAIL(EMAIL),'mailto: '+EMAIL)
    )

input_files=['../data/productos.csv'] #,'../data/semillas.csv']
if 'output_file' not in locals():
  print('entro en output')
  output_file='../public/index.html'

#template_subdir:
subdir='productos'
#Categorias
if 'parents' not in locals():
  parents={}
if 'only' not in parents:
  parents['only']=[]

parents['name']='Categorias'
parents['col_title']='categories'

parents['undesired']=['parador','entrega semanal','cuerpo y salud']#,'Productos Elaborados','Esenciales']

parents['first']=['entrega semanal','frescos','elaborados']
parents['last']=['esenciales']
parents['long_names']={'frescos':'productos frescos','elaborados':'productos elaborados'}
parents['mensajes']={'elaborados':""}
#ARTICULOS

if 'articles' not in locals():
  articles={}

if 'only' not in articles:
  articles['only']=[]
  
articles['prefix']='un'
articles['word']='producto'
articles['limited']={'entrega semanal':1,'bolsón':1,'caña con ruda':1}
articles['undesired']=['semillas agroecológicas']


# articles['outofstock']=['entrega semanal completa','bolsón de productos envasados']
#PEDIDOS
pedido=True

#MENSAJES
mensaje={}

mensaje['pedido']='' #'Compra mínima: $3000'

