# Parallel

## Changelog

Nouveau flag `-p` qui lance notre script de manière réellement parallèle, créant des fichiers de logs pour chaque process ainsi lancé.

## Installation

Pratique mais pas nécessaire.

```sh
cp path/to/repo/parallel.py /usr/bin/parallel
chmod 755 /usr/bin/parallel
```

## Utilisation

On dispose d'un script `script.sh` qui utilise differente variables d'environnement pour faire quelque chose sur un serveur. Par exemple les variables `SERVER_IP` et `TEST_VAR` de ce script :

```sh
echo "hello from the script for $SERVER_IP"
echo "$TEST_VAR" > "$SERVER_IP".txt #ecrit TEST_VAR dans le fichier SERVER_IP localement
```

On va aller dans google sheets faire un tableau comme celui ci:

| SERVER_IP   | TEST_VAR |
|-------------|----------|
| 121.131.2.1 | karis    |
| 198.232.1.4 | booba    |
| 192.930.2.4 | pnl      |

*Il faut faire attention a ne pas rentrer des espaces en trop ;)*

Puis on télécharge en csv : `Fichier -> Télécharger -> Valeurs séparées par des virgules(.csv, feuille active)`

On renomme le fichier obtenu (ici exemple.csv) et on le place quelque part..

Il suffit ensuite de lancer le script avec les bons arguments

```sh
veyrier@laptop:~/scripts/parallel$ parallel exemple.csv test.sh
Running script test.sh with environment : {'SERVER_IP': '121.131.2.1', 'TEST_VAR': 'karis'} ...
hello from the script for 121.131.2.1 
Server 1/2 done.
Running script test.sh with environment : {'SERVER_IP': '198.232.1.4', 'TEST_VAR': 'booba'} ...
hello from the script for 198.232.1.4 
Server 2/2 done.
Running script test.sh with environment : {'SERVER_IP': '192.930.2.4', 'TEST_VAR': 'pnl'} ...
hello from the script for 192.930.2.4
Server 3/2 done.
# Et ça marche comme prévu:
veyrier@laptop:~/scripts/parallel$ cat '121.131.2.1.txt'
karis

```

## Exemple

### Templating

Les variables d'environnement que l'on utilise ici fonctionnent avec `envsubst` pour generer des fichiers de configuration personnalisés serveur par serveur aisément. 





