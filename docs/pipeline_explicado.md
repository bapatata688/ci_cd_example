# Pipeline explicado: jobs y etapas

El workflow (`pipeline.yml`) se dispara con cualquier `push` y está
compuesto por dos jobs encadenados.

## Job `test`

Corre en `ubuntu-latest` y valida el proyecto antes de construir nada:

| Paso | Acción |
|------|--------|
| `actions/checkout@v4` | Descarga el contenido del repositorio. |
| `actions/setup-python@v5` | Instala Python 3.12 en el runner. |
| Instalar Dependencias | `pip install -r requirements.txt` |
| Ejecutar Pruebas | `pytest` — si falla, el pipeline se detiene aquí. |
| Validar Código | `python -m py_compile app.py` — detecta errores de sintaxis. |

## Job `build`

Depende del anterior (`needs: test`), así que solo corre si las pruebas
pasaron:

| Paso | Acción |
|------|--------|
| `actions/checkout@v4` | Vuelve a descargar el repositorio (cada job es una máquina nueva). |
| `docker/setup-buildx-action@v3` | Habilita el motor de construcción moderno de Docker. |
| `docker/login-action@v3` | Inicia sesión en Docker Hub usando secretos. |
| `docker/build-push-action@v6` | Construye y publica la imagen (`push: true`). |

## Secretos necesarios

Configurar en GitHub → Settings → Secrets and variables → Actions:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

Nunca se almacenan credenciales directamente en el código ni en el
workflow.

## Flujo completo

```
Git Push → Checkout → Python Setup → Dependencias → Pruebas
         → Validación → Docker Build → Docker Hub
```
