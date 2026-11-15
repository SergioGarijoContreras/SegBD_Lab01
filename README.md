# Garijo_Contreras_Sergio_SegBD_Lab01 — Seguridad en NoSQL (MongoDB y Elasticsearch) con FastAPI

**Autor:** Sergio Garijo Contreras

**Asignatura:** Seguridad en Bases de Datos, Blockchain y Big Data

Laboratorio reproducible mediante Docker Compose, realizar ataques controlados y aplicar contramedidas de defensa con tal de implementar seguridad NoSQL en MongoDB y Elasticsearch con FastAPI. 

---

## Branch explicadas

- `hardened` (**default branch**): versión bastionada, aplicando contramedidas solicitadas.
- `baseline-insecure`: estado vulnerable de la configuración (Mongo sin auth, ES abierto, NoSQLi en `/login_mongo`).

## Software utilizado

Se ha realizado esta actividad en un sistema Arch Linux, enteramente mediante comandos CLI.

Los comandos y herramientas usadas han sido:
- `Docker compose`
- `Docker`
- `Python 3.11`
- `curl`
- `git`
- `nmap`

## Setup

```bash
git checkout hardened
docker compose down
docker compose up -d --build
docker compose ps
