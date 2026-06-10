```md
# Changelog

Todos los cambios importantes de este proyecto serán documentados en este archivo.

## [1.1.0] - 2026-06-02

### Added
- Integración de **MinIO** para el almacenamiento de archivos.
- Implementación de **pip-audit** para la auditoría de vulnerabilidades (CVE).
- Documentación y comentarios descriptivos en el código.
- Archivo `uv.lock` para garantizar versiones reproducibles.
- Configuración funcional de Docker.

### Changed
- Migración del gestor de paquetes **pip** a **uv**.
- Reemplazo de `requirements.txt` por `pyproject.toml`.
- Estandarización del entorno de desarrollo utilizando uv.

### Security
- Fijación de versiones de dependencias mediante `uv.lock`.
- Auditoría automática de vulnerabilidades con **pip-audit**.

### Infrastructure
- Incorporación de un contenedor dedicado para **MinIO**.
- Mejoras en la configuración Docker.
```
