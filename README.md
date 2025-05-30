# TestCICD - Backend Flask & Frontend HTML

Ce projet contient :
- Un **backend Python Flask** (`backend/`)
- Un **frontend HTML/CSS** (`frontend/`)

Le projet peut être exécuté dans **trois environnements** :
1. **Production** : Lancer les dernières images Docker publiées sur Docker Hub
2. **CI/CD Pipeline** : Builder et pousser de nouvelles images via Jenkins
3. **Local sans Docker** : Démarrer le projet en local, sans Docker ni Jenkins

---

## 1. Exécution en Production (avec Docker)

### Pré-requis
- Docker et Docker Compose installés sur la machine cible
- Accès aux images sur Docker Hub (`massire1/testcicd-backend` et `massire1/testcicd-frontend`)

### Commandes
Clonez le dépôt ou téléchargez le fichier `docker-compose.prod.yml`, puis exécutez :

```bash
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

---

## 2. Builder et Pusher avec le Pipeline CI/CD

### Pré-requis
- Dépot Github disponible et accessible
- Webhook Github configuré
- Serveur Jenkins configuré et disponible sur internet
- Pipeline CI/CD configuré sur Jenkins

### Commandes
- Faire le push vers le dépot github distant avec `git push`

---

## 3. Exécution en Local (sans Docker ni Jenkins)

### Pré-requis
- Avoir le dépot github déjà cloné en Local
- Pointer sur le répertoire racine avec le terminal
- Avoir python installé sur la machine

### Commandes Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Commandes Frontend
```bash
python -m http.server 8000
```

