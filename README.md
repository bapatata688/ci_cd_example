# Proyecto Integrador: API de Ventas con Docker y CI/CD

Proyecto integrador que combina Docker, contenerización de aplicaciones,
principios de CI/CD y automatización con GitHub Actions en un único flujo
de trabajo de extremo a extremo, replicando un proceso real de la
industria.

## Objetivo

Construir una solución capaz de:

1. Ejecutar pruebas automáticamente.
2. Construir una imagen Docker.
3. Versionar la aplicación.
4. Publicar la imagen en un registro.
5. Preparar el despliegue automático.

## Escenario

Una empresa cuenta con una API en Python para consultar información de
ventas. Cada vez que un desarrollador actualiza el código, se ejecutan
pruebas, se valida la sintaxis, se construye una imagen Docker, se
publica y se prepara para despliegue — todo de forma automática.

## Arquitectura general

```
GitHub
  │
  ▼
GitHub Actions
  │
  ▼
Pruebas
  │
  ▼
Docker Build
  │
  ▼
Docker Registry
  │
  ▼
Deploy
```

## Estructura del proyecto

El trabajo está dividido en dos partes iguales, entregadas como dos
archivos `.zip` independientes:

```
ventas_api/
│
├── app.py                          ← Parte 1
├── requirements.txt                ← Parte 1
├── tests/
│   └── test_app.py                 ← Parte 1
├── Dockerfile                      ← Parte 1
├── PARTE_1.md                      ← Parte 1
│
├── .github/
│   └── workflows/
│       └── pipeline.yml            ← Parte 2
├── docs/
│   ├── pipeline_explicado.md       ← Parte 2
│   └── buenas_practicas.md         ← Parte 2
└── PARTE_2.md                      ← Parte 2
```

### Parte 1 — Aplicación y Contenerización (`parte1_aplicacion_docker.zip`)

La API Flask, su prueba automatizada y el Dockerfile que la empaqueta.
Cubre todo lo que se verifica **manualmente** antes de automatizar nada.

### Parte 2 — Pipeline CI/CD (`parte2_pipeline_cicd.zip`)

El workflow de GitHub Actions que automatiza lo anterior: pruebas,
validación de sintaxis, construcción de la imagen y publicación en
Docker Hub.

Para que el pipeline funcione, ambas partes deben unirse en un mismo
repositorio (los archivos de la Parte 1 en la raíz, más `.github/` de la
Parte 2).

## Uso rápido

```bash
# 1. Verificación local (Parte 1)
pip install -r requirements.txt
pytest
docker build -t ventas-api .
docker run -p 5000:5000 ventas-api
```

Acceder a `http://localhost:5000`:

```json
{
  "mensaje": "API de ventas operativa"
}
```

```bash
# 2. Automatización (Parte 2)
# Configurar en GitHub → Settings → Secrets and variables → Actions:
#   DOCKER_USERNAME
#   DOCKER_PASSWORD
#
# Cualquier "git push" dispara el pipeline definido en
# .github/workflows/pipeline.yml
```

## Flujo de ejecución del pipeline

```
Git Push → Checkout → Python Setup → Dependencias → Pruebas
         → Validación → Docker Build → Docker Hub
```

## Buenas prácticas aplicadas

- Toda versión se valida (pruebas + sintaxis) antes de publicarse.
- El Dockerfile se mantiene simple para builds rápidos.
- Las credenciales viven en secretos de GitHub, nunca en el código.
- El pipeline es modular: jobs separados y encadenados con `needs`.

## Mejoras posibles

| Mejora | Herramienta |
|---|---|
| Cobertura de pruebas | `pytest --cov` |
| Escaneo de seguridad | Bandit |
| Análisis de calidad | SonarQube |
| Versionamiento | Tags semánticos (`v1.0.0`, `v1.1.0`) |
| Despliegue automático | Etapa adicional Registry → Producción |

## Más allá de esta API

La misma arquitectura (Checkout → Pruebas → Docker Build → Registro →
Deploy) aplica directamente a escenarios de ingeniería de datos: procesos
ETL, APIs analíticas con FastAPI, procesamiento con Pandas o
automatización de reportes — todos siguen los mismos principios.

## Documentación adicional

Un notebook (`proyecto_integrador.ipynb`) acompaña este README con una
explicación paso a paso de todo el flujo, incluyendo la app y la prueba
ejecutadas en vivo.
