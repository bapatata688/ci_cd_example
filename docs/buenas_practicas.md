# Buenas prácticas y mejoras posibles

## Buenas prácticas aplicadas 

- **Automatizar validaciones**: ninguna versión se publica sin pasar
  pruebas y validación de sintaxis primero.
- **Mantener el Dockerfile simple**: una sola etapa, sin pasos
  innecesarios, para builds rápidos.
- **Usar secretos**: las credenciales de Docker Hub nunca están en el
  código, solo en `secrets.*`.
- **Pipelines modulares**: dos jobs separados (`test`, `build`)
  encadenados con `needs`, no un solo job monolítico.

## Mejoras posibles para un pipeline más robusto

| Mejora | Herramienta / Comando |
|--------|------------------------|
| Cobertura de pruebas | `pytest --cov` |
| Escaneo de seguridad | Bandit |
| Análisis de calidad de código | SonarQube |
| Versionamiento automático | Tags semánticos (`v1.0.0`, `v1.1.0`) en vez de depender solo de `latest` |
| Despliegue automático | Etapa adicional que promueva la imagen del Docker Registry a producción |

## Esta misma arquitectura aplica a ingeniería de datos

El patrón Checkout → Pruebas → Docker Build → Registro → Deploy no es
exclusivo de APIs; sirve igual para:

- **Procesos ETL**: script Python → imagen Docker → pipeline CI/CD.
- **APIs analíticas**: FastAPI → Docker → GitHub Actions.
- **Procesamiento de datos**: Python + Pandas → Docker → CI/CD.
- **Automatización de reportes**: scripts → Docker → pipeline.
