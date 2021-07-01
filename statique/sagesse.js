function loadXMLDoc() { /*demande un proverbe au serveur (qui en renvoie un de manière aléatoire)*/
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("provb").innerHTML =//met le proverbe obtenu dans la zone id="provb"
			this.responseText;
		}
	};
	xhttp.open("GET", "proverbes", true);
	xhttp.send();
}



//loadXMLDoc();

function getParam(param){//récuperation du paramètre dont le nom est passé en paramètre de la fonction
	return new URLSearchParams(window.location.search).get(param);
	}
	
function getproverbeperso(){//demande au serveur le proverbe correspondant au numéro du paramètre 'num'
	console.log(getParam("num"));
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("provb").innerHTML =//met le proverbe obtenu dans la zone id="provb OU affiche le message d'erreur du serveur"
			this.responseText;
		}
	};
	xhttp.open("GET", "proverbeperso", true);
	xhttp.send();
}
console.log(getParam("num"));

function quedemander(){//au chargement de la page, pour savoir s'il faut demander au serveur un proverbe spécifique ou aléatoire en fonction de l'url
	if (getParam("num") == ""){
		alert("Veuillez rentrer une valeur dans le champs avant de soumettre");//alerte l'utilisateur
		location.replace("/sagesse.html");
		return;
	}
	if (getParam("num") == null){
		loadXMLDoc();

	}else {
		getproverbeperso();
	}
}
			
			