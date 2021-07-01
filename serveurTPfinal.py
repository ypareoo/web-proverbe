# Créé par Paul Bosseboeuf, le 07/04/2021 en Python 3.7

from bottle import route, run, static_file, get, request,error #importe la magie du code
from etape import* #importe l'etape de lecture de fichier des proverbes et les mets dans le tableau 'proverbes' en ajoutant le n° de la citation


listenombre=[] #création d'un tableau permettant de dire si les valeurs envoyées en GET correspondent bien au numéro d'une citation
for i in range(1,403):
    listenombre.append(str(i))
print("la liste des chiffres des différentes citations est créé")

@route('/<filepath:path>')#quand on demande un fichier statique situé dans le fichier "statique"(vous suivez tjrs ?), le programme/serveur le renvoie
def server_static(filepath):
    return static_file(filepath, root='./statique/')

@route('/proverbes') #renvoie d'un proverbe aléatoire quand est demandé la route 'proverbes'
def hello():
    #print(request.url)
    return proverbes[random.randint(0,compteur-2)]

@route('/sagesse.html')#travail du serveur statique + prélevement de la requête en GET
def login():
    global solution #variable qui sert lors de la requête 'proverbeperso'
    solution = request.url.split("=")[-1] #solution = requête en GET (dernière valeur du tableau dont les élements sont issues de l'url et séparés avec le '=')
    #print(solution)
    return static_file("sagesse.html", root='./statique/')

@route("/proverbeperso")
def hello():
    global solution #reprend la variable ayant la requête en GET
    if solution in listenombre: #si la requête correspond à une sitation --> envoie du proverbe demandé
        #print("OK")
        return proverbes[int(solution)-1] #'-1' --> les citations commence à 1 et l'emplacement du tableau à 0
    else:
        return "REPONSE DU SERVEUR : La valeur entrée est invalide (value must be 'int') OU Le proverbe demandé n'existe pas" #SINON --> renvoie une réponse qui se mettra à la place du proverbe




@error(404) #renvoie une page web personnalisé à l'erreur 404 (page web aurait pu être séparé du programme dans un fichier html externe)
def error404(error):
    return '''
<!DOCTYPE html>
<html lang="fr">
    <head>
		<meta charset="utf-8">
		<title>réponse du serveur : Error 404</title>
		<link rel="icon" href="404.png" />
    </head>
    <body>
        <h1>Ah désolé le serveur est encore un peu trop jeune, il connait pas tout du web</h1>
        <h2>Vous êtes bien connecté au serveur de P.bosseboeuf</h2>
        Serveur amateur code : J.U.LZ
        <h3>essaiez de bien orthographier la destination</h3>
        <h1>ERREUR 404</h1>
    </body>'''





run(host='0.0.0.0', port=8080, debug=True) #lance le serveur sur le port 8080 à l'adresse 127.0.0.1:8080 OU depuis le WAN si configuration admin sur la box (NAT)
