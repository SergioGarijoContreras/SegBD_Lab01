# SegBD_Lab01 — Baseline inseguro
Estado vulnerable del laboratorio.
Mongo sin `--auth`, ES sin seguridad y puertos 27017/9200/8000 expuestos; app FastAPI sin validación.
Arranque: `docker compose up -d --build` y smoke test: `/pedidos`, `/login_mongo`, `/articulos`.
Ataques: NoSQLi `{"password":{"$ne":"x"}}`, `curl localhost:9200/_cat/indices?v`, `_search?q=*` y `DELETE /articulos`.
Resultado: todos funcionan (200) → sin auth, sin TLS, sin logs de seguridad.
