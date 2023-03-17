import ldap3
import mysql.connector

server = 'ldap://192.168.182.3:389'

# Créer une connection avec le LDAP
ldap = ldap3.Server(server)
conn_LDAP = ldap3.Connection(ldap)

# Se connecter à l'annuaire anonymement 
conn_LDAP.bind()

# Sinon se connecter avec un utilisateur
# conn_LDAP.bind('cn=admin,dc=mondomaine,dc=lan', 'password')

# Rechercher les objets posixAccount et récupérer les uids
conn_LDAP.search('dc=mondomaine,dc=lan', '(objectClass=posixAccount)', attributes=['uid'])
uids = []

for entry in conn_LDAP.entries:
    uids.append(entry.uid.value)

# Fermer la connection avec le LDAP
conn_LDAP.unbind()

# Récupérer le mot de passe de connexion à la DB
rootPassword = ""
with open('/root/ALCASAR-passwords.txt') as f:
    for line in f.readlines():
        if line.startswith('#'):
            continue
        key, value = line.strip().split('=')
        if key == 'db_root':
            rootPassword = value

# Se connecter à la base de données
conn_mariadb = mysql.connector.connect(
        unix_socket='/var/lib/mysql/mysql.sock',
        user="root",
        password=rootPassword,
        database="radius"
)

# Créer un curseur pour exécuter des requètes SQL
cursor = conn_mariadb.cursor()

# Exécuter les réquêtes SQL pour l'ajout des utilisateurs au groupe LDAP
for uid in uids:
    cursor.execute("SELECT COUNT(*) FROM `radusergroup` WHERE `username` = %s", (uid,))
    result = cursor.fetchone()

    if result[0] == 0:
        cursor.execute("INSERT INTO `radusergroup` (`username`,`groupname`,`priority`) VALUES (%s,'ldap',1)", (uid,))

# Comfirmer
conn_mariadb.commit()

# Fermer le curseur et la connection
cursor.close()
conn_mariadb.close()
