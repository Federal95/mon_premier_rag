# Mini Projet RAG avec ChromaDB et Groq

## Présentation

Ce projet implémente un système de Retrieval-Augmented Generation (RAG) en Python. Il permet d'indexer un document CSV dans une base vectorielle ChromaDB, de retrouver les passages les plus pertinents et de générer une réponse à l'aide de l'API Groq.

## Objectifs

- Construire une base vectorielle avec ChromaDB.
- Générer des embeddings avec SentenceTransformers.
- Effectuer une recherche sémantique.
- Générer des réponses grâce à Groq.
- Protéger le système contre les attaques de Prompt Injection.

## Technologies utilisées

- Python 3.11
- ChromaDB
- SentenceTransformers
- Groq API
- Git
- GitHub

## Structure du projet

```
MON_PREMIER_RAG/

├── chroma_db/
├── data/
├── prompts/
├── config.py
├── main.py
├── moderator.py
├── rag.py
├── vectordb.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
```

L'activer :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Configuration

Créer un fichier `.env` contenant :

```env
GROQ_API_KEY=votre_cle_api
```

## Exécution

```bash
python main.py
```

Le programme lance un assistant RAG qui répond aux questions sur le document indexé.

## Workflow Git

Le développement a été réalisé selon le workflow suivant :

```
feature/vector-db
        │
        ▼
       dev
        │
        ▼
      main
```

## Difficultés rencontrées

- Installation des dépendances Python.
- Incompatibilité avec Python 3.13.
- Création et activation de l'environnement virtuel.
- Configuration de la clé API Groq.
- Gestion des branches Git et des fusions.

## Solutions apportées

- Utilisation de Python 3.11.
- Création d'un environnement virtuel dédié.
- Installation des dépendances avec `requirements.txt`.
- Utilisation d'un fichier `.env` pour stocker la clé API.
- Fusion progressive des branches `feature`, `dev` et `main`.

## Améliorations possibles

- Interface graphique avec Streamlit.
- Support des fichiers PDF.
- Historique des conversations.
- Déploiement dans un conteneur Docker.

## Auteur

DAPA Paulin