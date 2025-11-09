# Manual de Usuario - Sistema de Boletas de Calificaciones

## 1. Descripción y Objetivo

El Sistema de Boletas de Calificaciones es una aplicación web diseñada para gestionar y visualizar calificaciones escolares. Permite:

- Registro de calificaciones por alumno
- Cálculo automático de promedios
- Visualización mediante semáforo de desempeño
- Exportación de datos a CSV
- Gestión de registros (agregar/eliminar)

## 2. Requisitos del Sistema

### Software Necesario
- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Edge)
- Node.js (para despliegue)

### Dependencias
````text
flet>=0.21.0
````

## 3. Guía de Uso

### Paso 1: Registro de Calificaciones
1. Selecciona un alumno del menú desplegable
2. Ingresa calificaciones (0-100) para cada materia:
   - Español
   - Matemáticas
   - Inglés
   - Humanidades
   - Emplea
   - Ecosistema
   - Aplica
   - Educación Física
3. Presiona "Calcular Promedio"

### Paso 2: Gestión de Datos
- **Borrar Registro**: Usa el botón rojo en cada fila
- **Borrar Tabla**: Limpia todos los registros
- **Exportar**: Guarda datos en formato CSV

## 4. Semáforo de Desempeño

| Color | Rango | Significado |
|-------|-------|------------|
| 🟢 Verde | ≥ 85 | Excelente |
| 🟡 Amarillo | 70-84 | Regular |
| 🔴 Rojo | < 70 | Necesita mejorar |

## 5. Capturas de Pantalla

[Aquí deberías incluir capturas de:
- Pantalla principal
- Proceso de registro
- Tabla con datos
- Exportación CSV]

## 6. Enlace del Proyecto

Accede a la aplicación en vivo:
[Boletas de Calificaciones](https://boletas-vercel.app)

## 7. Créditos

**Desarrollado por:** Dulce María Valadez Molina  
**Versión:** 1.0  
**Fecha:** Noviembre 2025

### Contacto
- GitHub: [@valadezmolinadulcemaria-del]
- Email: [valadezmolinadulcemaria@cetis50cdmx.com]

---

**Nota**: Para reportar problemas o sugerir mejoras, por favor crear un issue en el repositorio del proyecto.
