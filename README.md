# 📚 Plan de Estudio: 12 Semanas → Junior Full-Stack Python (Mentor Mode)

> **Dedicación:** 10–15 horas semanales (2–3 horas diarias × 5 días)  
> **Nivel:** Cero conocimiento → Primer trabajo como Developer  
> **Stack:** Python + FastAPI + React (Front-End básico) + Cloud  
> **Objetivo:** Ser contratables en 2026 en el mercado chileno

---

## ⚡ Cómo Usar Este Plan

Cada semana es **independiente y progresiva**. Trabajarás:
- **2-3 horas diarias** en conceptos + recursos
- **Preguntas frecuentes** que puedes hacerme en cualquier momento
- **Checklist semanal** para validar comprensión
- **3 proyectos** (básico, intermedio, avanzado) que suben en complejidad

**Nota:** No haremos autocompletes de código. Me explicas qué no entiendes y te lo enseño paso a paso.

---

# 🎯 FASE 1: FUNDAMENTOS TRANSVERSALES (Semanas 1–3)

## SEMANA 1: Git, GitHub y Setup del Entorno

### 📖 ¿Por Qué Empezamos Aquí?
Git es el **lenguaje universal** del desarrollo. Todo trabajo usa Git. GitHub es tu **portafolio visible** para reclutadores. Esta semana configuras tu entorno correctamente desde el inicio.

### 🎓 Conceptos a Aprender

1. **Git Básico**
   - Qué es un **repositorio** (carpeta especial que guarda el historial de cambios)
   - Qué significa **commit** (una "fotografía" de tu código en un momento)
   - **Diferencia entre Git (local) y GitHub (en la nube)**
   - Flujo básico: `git add` → `git commit` → `git push`

2. **GitHub**
   - Crear cuenta profesional
   - Entender **repositorio remoto** (tu código en GitHub)
   - Qué es un **README** (presentación de tu proyecto)

3. **Setup Local**
   - Terminal/CMD (ejecutar comandos)
   - Python 3.9+ instalado
   - Editor: VS Code configurado
   - Git instalado y vinculado a GitHub

### 📚 Recursos Recomendados

- **Video (15 min):** "Git para principiantes" - Traversy Media (YouTube)
- **Interactivo:** https://learngitbranching.js.org/ (juego para entender Git)
- **Documentación oficial:** https://git-scm.com/book/es/v2 (Capítulos 1-2)
- **GitHub Setup:** Guía oficial en https://docs.github.com/es

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Qué diferencia hay entre Git y GitHub?
Git es un repositorio local que tiene por objetivo llevar un control de versiones del un proyecto y GitHub es un repositorio remoto que permite sincronizar un proyecto local.

- ¿Qué es un commit y cuándo lo debo hacer?
Commit es un comando para guardar los cambios actuales del proyecto en Git.
- ¿Cómo recupero un archivo que eliminé?

- ¿Qué es un `.gitignore`?
Es un archivo que contiene todas los archivos, dependencias y librerias que no se sincronizaran con GitHub, en otras palabras que seran ignorados.

- ¿Cómo clono un repositorio?
Se realiza con el comando git clone <'link del proyecto'>

### ✅ Checklist Semanal

- [x] Git instalado y configurado (`git config --global user.name "Tu Nombre"`)
- [x] Cuenta GitHub creada y configurada con foto profesional
- [x] Clave SSH generada y vinculada a GitHub
- [x] VS Code instalado con extensión de Git
- [x] Python 3.9+ confirmado (`python --version`)
- [x] Entiendo qué es un commit y cuándo hacerlo
- [x] He creado mi primer repositorio en GitHub
- [x] He hecho al menos 5 commits en ese repositorio

### 🚀 Proyectos Semana 1

#### Proyecto 1.1: Mi Primer Repositorio (Básico)
**Qué harás:** Crear un repositorio llamado `mi-primer-proyecto` con un archivo README que te presente.

**Lo que aprenderás:**
- Crear repositorio en GitHub
- Clonar repositorio localmente
- Hacer cambios, hacer commits y hacer push
- Escribir un README básico

**Checklist del proyecto:**
- [x] Repositorio creado en GitHub
- [x] README con tu nombre, qué esperas aprender, y por qué
- [x] Al menos 3 commits con mensajes claros
- [x] Cambios visibles en GitHub

---

#### Proyecto 1.2: Estructura de Carpetas de Trabajo (Intermedio)
**Qué harás:** Crear la estructura de carpetas que usarás todo el curso, con un git ignore.

**Lo que aprenderás:**
- Organizar proyectos profesionalmente
- Qué es un `.gitignore` y por qué es importante
- Documentar estructura en README

**Carpetas a crear:**
```
repaso-dev/
├── semana-1/
├── semana-2/
├── ...
├── proyectos/
├── .gitignore
└── README.md
```

**Checklist del proyecto:**
- [ ] Carpetas creadas localmente
- [ ] Archivo `.gitignore` con patrones básicos
- [ ] README explicando la estructura
- [ ] Todo en GitHub con commits descriptivos

---

#### Proyecto 1.3: Contribución a Repositorio Existente (Avanzado)
**Qué harás:** Encontrar un repositorio open-source pequeño en GitHub y hacer tu primer **pull request**.

**Lo que aprenderás:**
- Fork de repositorios
- Crear branch para cambios
- Hacer pull request
- Entender flujo colaborativo

**Checklist del proyecto:**
- [ ] Repositorio fork seleccionado
- [ ] Branch creado con nombre descriptivo
- [ ] Cambio pequeño hecho (ej: corregir typo, agregar ejemplo)
- [ ] Pull request abierto con descripción clara

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **4-5 horas**
- Proyectos: **6-8 horas**
- **Total semana:** 10-13 horas

---

## SEMANA 2: HTML, CSS y JavaScript Básico (Fundamentos Web)

### 📖 ¿Por Qué Esta Semana?
Aunque trabajarás principalmente en **backend (Python)**, necesitas entender **cómo funciona el frontend** para construir APIs que lo alimenten. HTML + CSS + JavaScript son la **base de cualquier página web**.

### 🎓 Conceptos a Aprender

1. **HTML Básico**
   - Qué es una **etiqueta** (ej: `<div>`, `<p>`, `<h1>`)
   - Estructura básica de un HTML (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
   - Atributos (ej: `class`, `id`, `href`)
   - Diferencia entre **semántica** (etiquetas con significado) y divs genéricos

2. **CSS Básico**
   - Selectores (por elemento, por clase, por id)
   - Propiedades comunes: `color`, `background`, `margin`, `padding`, `display`
   - Box Model (el modelo de cajas: content → padding → border → margin)
   - Flexbox básico (para alinear cosas sin quebarse)

3. **JavaScript Básico (ES6+)**
   - Variables: `let`, `const`, `var` (cuándo usar cada una)
   - Tipos: `string`, `number`, `boolean`, `array`, `object`
   - Funciones: qué son, cómo crearlas, parámetros y retorno
   - Manipulación del DOM: seleccionar elementos y cambiarlos
   - Event listeners: responder a clics, inputs, etc.

### 📚 Recursos Recomendados

- **Video (2 horas):** "HTML & CSS Crash Course" - Traversy Media (YouTube)
- **Video (3 horas):** "JavaScript Basics" - The Net Ninja (YouTube)
- **Interactivo:** https://www.freecodecamp.org/learn/responsive-web-design/ (FreeCodeCamp)
- **Referencia:** https://developer.mozilla.org/es/docs/Web/HTML (MDN Docs)
- **Práctica:** https://www.codecademy.com/learn/learn-html (opcional, de pago)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuál es la diferencia entre `let` y `const`?
- ¿Por qué a veces veo atributos `data-*` en HTML?
- ¿Cómo cambio un elemento HTML desde JavaScript?
- ¿Qué es un event listener y cuándo lo uso?
- ¿Cuál es la diferencia entre una clase en CSS y un id?
- ¿Qué es el DOM?

### ✅ Checklist Semanal

- [ ] Entiendo la estructura básica de un HTML
- [ ] Puedo escribir CSS para cambiar colores, tamaños y posiciones
- [ ] Entiendo la diferencia entre `let`, `const` y `var`
- [ ] Puedo seleccionar elementos del DOM con JavaScript
- [ ] Sé cómo agregar event listeners para responder a clics
- [ ] Puedo crear funciones simples en JavaScript
- [ ] Entiendo qué es el Box Model en CSS
- [ ] Puedo usar Flexbox para alinear elementos básicamente

### 🚀 Proyectos Semana 2

#### Proyecto 2.1: Mi Primera Página Web (Básico)
**Qué harás:** Crear una página personal simple con HTML y CSS.

**Requisitos mínimos:**
- Header con tu nombre
- Sección "Sobre Mí" con párrafos
- Sección "Proyectos" (vacía por ahora)
- Footer con links a redes
- Debe verse bien en celular (responsive basic)

**Lo que aprenderás:**
- Estructura HTML semántica
- CSS para estilos y responsive
- Trabajo con git desde VS Code

**Checklist del proyecto:**
- [ ] Archivo HTML con estructura correcta
- [ ] Estilos CSS en archivo separado
- [ ] Al menos 3 commits en GitHub
- [ ] Funciona en navegador

---

#### Proyecto 2.2: Galería Interactiva (Intermedio)
**Qué harás:** Crear una galería de imágenes con JavaScript.

**Requisitos:**
- Mostrar 6 imágenes en una cuadrícula
- Click en imagen → muestra versión grande (modal o lightbox)
- Botón "Anterior" y "Siguiente" para navegar
- Contador de imágenes vistas

**Lo que aprenderás:**
- Manipulación del DOM con JavaScript
- Event listeners (click, navegación)
- Mostrar/ocultar elementos dinámicamente

**Checklist del proyecto:**
- [ ] 6 imágenes cargadas correctamente
- [ ] Modal funcional (abre y cierra)
- [ ] Navegación anterior/siguiente funciona
- [ ] Contador actualiza correctamente
- [ ] Responsive en celular

---

#### Proyecto 2.3: Aplicación Mini Tareas (Avanzado)
**Qué harás:** Crear una app de tareas con JavaScript puro (sin backend aún).

**Requisitos:**
- Input para crear tarea
- Botón "Agregar tarea"
- Lista de tareas con botón "Eliminar"
- Botón "Completar" que marca con estilo diferente
- Contador: "X de Y tareas completadas"
- Los datos se guardan en localStorage (persisten al recargar)

**Lo que aprenderás:**
- Manipulación del DOM compleja
- Arrays y objetos en JavaScript
- localStorage para persistencia
- Manejo de eventos múltiples

**Checklist del proyecto:**
- [ ] Puedo crear tareas
- [ ] Puedo marcar tareas como completadas
- [ ] Puedo eliminar tareas
- [ ] Las tareas persisten al recargar la página
- [ ] Contador funciona correctamente
- [ ] Código limpio con funciones bien separadas

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **5-6 horas**
- Proyectos: **7-9 horas**
- **Total semana:** 12-15 horas

---

## SEMANA 3: SQL, Bases de Datos y Conceptos de Backend

### 📖 ¿Por Qué Esta Semana?
Tu **backend (Python/FastAPI)** necesitará guardar datos en una **base de datos**. SQL es el lenguaje universal para comunicarse con bases de datos. Entender SQL es **crítico** para cualquier developer.

### 🎓 Conceptos a Aprender

1. **Conceptos de Bases de Datos**
   - Qué es una **base de datos** (conjunto organizado de datos)
   - Diferencia entre **SQL (relacional)** y NoSQL
   - Tablas, filas, columnas (estructura relacional)
   - Claves primarias e índices

2. **SQL Básico**
   - `SELECT`: Obtener datos (filtrar, ordenar)
   - `WHERE`: Condicionales
   - `JOIN`: Relacionar dos tablas
   - `INSERT`, `UPDATE`, `DELETE`: Crear, modificar, eliminar datos
   - `GROUP BY` y agregaciones (`COUNT`, `SUM`, `AVG`)

3. **PostgreSQL / MySQL Setup**
   - Instalar localmente (PostgreSQL recomendado)
   - Crear base de datos de prueba
   - Herramientas visuales (pgAdmin, DBeaver)

4. **Conceptos Backend**
   - Qué es una **API REST** (cómo el frontend pide datos al backend)
   - Métodos HTTP: GET (leer), POST (crear), PUT (actualizar), DELETE (eliminar)
   - Status codes: 200 (ok), 404 (no encontrado), 500 (error servidor)
   - JSON (formato de intercambio de datos)

### 📚 Recursos Recomendados

- **Video (2 horas):** "SQL for Beginners" - Alex The Analyst (YouTube)
- **Interactivo:** https://mode.com/sql-tutorial/ (Mode SQL Tutorial)
- **Práctica:** https://www.sqlzoo.net/ (ejercicios interactivos de SQL)
- **Instalación:** https://www.postgresql.org/download/ (PostgreSQL oficial)
- **Herramienta visual:** https://www.pgadmin.org/ (gestor PostgreSQL)
- **Video (1 hora):** "REST APIs Explained" - Web Dev Simplified (YouTube)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuál es la diferencia entre SQL y NoSQL?
- ¿Qué es una clave primaria?
- ¿Cuándo uso `JOIN` vs `WHERE`?
- ¿Cómo evito que alguien borre toda mi base de datos?
- ¿Qué es un índice y por qué es importante?
- ¿Cuál es la diferencia entre GET y POST?
- ¿Por qué usar JSON en las APIs?

### ✅ Checklist Semanal

- [ ] Entiendo qué es una tabla y cómo está estructurada
- [ ] PostgreSQL instalado y funcionando localmente
- [ ] Puedo crear una base de datos y una tabla
- [ ] Puedo escribir un SELECT básico con WHERE
- [ ] Entiendo cómo usar JOINs entre dos tablas
- [ ] Puedo usar GROUP BY para agregar datos
- [ ] Sé qué es una API REST y los métodos HTTP
- [ ] Entiendo qué es un status code
- [ ] Sé qué es JSON y cómo se estructura

### 🚀 Proyectos Semana 3

#### Proyecto 3.1: Base de Datos de Biblioteca (Básico)
**Qué harás:** Diseñar y crear una BD simple para una biblioteca.

**Tablas necesarias:**
- `libros` (id, título, autor, año)
- `usuarios` (id, nombre, email)
- `préstamos` (id, libro_id, usuario_id, fecha_préstamo)

**Queries a escribir:**
- Listar todos los libros
- Listar préstamos de un usuario específico
- Contar cuántos libros tiene cada autor
- Encontrar todos los préstamos sin devolución

**Lo que aprenderás:**
- Crear tablas y relaciones
- Escribir SELECT y WHERE
- Usar JOINs simples

**Checklist del proyecto:**
- [ ] Base de datos creada en PostgreSQL
- [ ] 3 tablas con campos apropiados
- [ ] Al menos 10 registros insertados (datos de prueba)
- [ ] 5 queries diferentes escritas y testadas

---

#### Proyecto 3.2: Dashboard SQL (Intermedio)
**Qué harás:** Crear un archivo con queries que respondan preguntas del negocio.

**Preguntas a responder con SQL:**
- ¿Cuál es el libro más prestado?
- ¿Qué usuario ha pedido más libros?
- ¿Cuál es el promedio de libros por usuario?
- ¿Qué libros no han sido prestados?
- Histórico de préstamos ordenado por fecha (más recientes primero)

**Lo que aprenderás:**
- Combinar WHERE, JOIN, ORDER BY, GROUP BY
- Agregaciones complejas
- Optimizar queries

**Checklist del proyecto:**
- [ ] 5+ queries que respondan a preguntas del negocio
- [ ] Queries están comentadas explicando qué hacen
- [ ] Resultados verificados manualmente
- [ ] Archivo guardado en GitHub

---

#### Proyecto 3.3: Sistema de Calificaciones de Cursos (Avanzado)
**Qué harás:** Diseñar una BD para un sistema de cursos y calificaciones.

**Tablas:**
- `cursos` (id, nombre, instructor)
- `estudiantes` (id, nombre, email)
- `inscripciones` (id, estudiante_id, curso_id)
- `calificaciones` (id, estudiante_id, curso_id, nota)

**Queries complejas:**
- Promedio de notas por curso
- Estudiante con mejor desempeño general
- Cursos donde un estudiante obtuvo A
- Instructor que tiene el mejor promedio en sus cursos
- Reporte: Por cada curso, mostrar: nombre, instructor, estudiantes inscritos, promedio general

**Lo que aprenderás:**
- Relaciones many-to-many
- Subconsultas
- Agregaciones múltiples

**Checklist del proyecto:**
- [ ] 4 tablas con relaciones correctas
- [ ] 30+ registros para pruebas
- [ ] 8+ queries complejas
- [ ] Todas las queries documentadas
- [ ] Resultados vistos en pgAdmin

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **5-6 horas**
- Proyectos: **7-8 horas**
- **Total semana:** 12-14 horas

---

# 🐍 FASE 2: PYTHON FULL-STACK (Semanas 4–7)

## SEMANA 4: Python Fundamentos y POO

### 📖 ¿Por Qué Esta Semana?
Esta es la **primera semana de programación real en Python**. Python será tu lenguaje principal. Necesitas entender **cómo funciona el lenguaje** antes de construir APIs.

### 🎓 Conceptos a Aprender

1. **Python Básico**
   - Variables, tipos de datos (int, float, string, bool, list, dict)
   - Operadores aritméticos y lógicos
   - Estructuras de control: `if/elif/else`, `for`, `while`
   - Funciones: qué son, parámetros, retorno, scope
   - Manejo de excepciones: `try/except/finally`

2. **Estructuras de Datos**
   - Listas: crear, acceder, modificar, métodos (append, remove, sort)
   - Diccionarios: clave-valor, acceso, iteración
   - Tuplas: inmutables, cuándo usarlas
   - Sets: colecciones sin duplicados

3. **Programación Orientada a Objetos (POO)**
   - **Clases**: plantilla para crear objetos
   - **Objetos/Instancias**: manifestación de una clase
   - **Atributos**: propiedades del objeto
   - **Métodos**: funciones dentro de una clase
   - **Constructor (`__init__`)**: inicializa el objeto
   - **Herencia**: una clase "hereda" de otra
   - **Polimorfismo**: mismo método, diferentes comportamientos

4. **Python Módulos**
   - Qué es un módulo (archivo .py reutilizable)
   - `import`: traer código de otros archivos
   - Librerías estándar: `math`, `datetime`, `random`, `json`

### 📚 Recursos Recomendados

- **Video (4 horas):** "Python Tutorial for Beginners" - Corey Schafer (YouTube)
- **Video (2 horas):** "Python OOP Tutorial" - Corey Schafer (YouTube)
- **Interactivo:** https://www.codecademy.com/learn/learn-python-3 (Codecademy)
- **Documentación:** https://docs.python.org/es/3/ (Official Python Docs)
- **Libro (free):** "Automate the Boring Stuff with Python" (caps 1-12)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuándo usar listas vs tuplas?
- ¿Cuál es la diferencia entre `==` y `is`?
- ¿Por qué necesito clases si tengo funciones?
- ¿Qué es `self` en las clases?
- ¿Cómo hereda una clase de otra?
- ¿Cuál es la diferencia entre atributo y método?
- ¿Para qué sirve `__init__`?
- ¿Cómo manejo errores en Python?

### ✅ Checklist Semanal

- [ ] Python 3.9+ instalado y funcionando
- [ ] Entiendo variables y tipos de datos básicos
- [ ] Puedo escribir funciones con parámetros y retorno
- [ ] Entiendo listas, diccionarios y tuplas
- [ ] Puedo crear una clase simple con atributos y métodos
- [ ] Entiendo qué es el constructor (`__init__`)
- [ ] Puedo heredar de una clase
- [ ] Entiendo try/except para manejo de errores
- [ ] Sé cómo importar módulos

### 🚀 Proyectos Semana 4

#### Proyecto 4.1: Sistema de Estudiantes (Básico)
**Qué harás:** Crear una clase `Estudiante` con atributos y métodos.

**Requisitos:**
- Clase `Estudiante` con: nombre, matricula, carrera, calificaciones (lista)
- Métodos:
  - `agregar_calificacion(nota)`: agrega nota a la lista
  - `promedio()`: calcula el promedio
  - `estado()`: retorna "Aprobado" si promedio >= 4.0, sino "Reprobado"
- Crear 3 instancias y mostrar sus promedios

**Lo que aprenderás:**
- Crear clases con atributos
- Métodos que manipulan atributos
- Listas y cálculos

**Checklist del proyecto:**
- [ ] Clase `Estudiante` creada con todos los atributos
- [ ] Métodos funcionan correctamente
- [ ] Puedo crear múltiples instancias
- [ ] Código guardado en GitHub con commits

---

#### Proyecto 4.2: Herencia de Vehículos (Intermedio)
**Qué harás:** Crear una jerarquía de clases con herencia.

**Requisitos:**
- Clase base `Vehículo` con:
  - Atributos: marca, modelo, año, velocidad_máxima
  - Método: `acelerar()`, `frenar()`, `velocidad_actual`
  
- Clases derivadas:
  - `Auto`: hereda de Vehículo + atributo "puertas"
  - `Moto`: hereda de Vehículo + atributo "tipo_manillar"
  - `Camión`: hereda de Vehículo + atributo "capacidad_carga"

- Cada clase derivada debe:
  - Tener su propio método `describir()` (polimorfismo)
  - Mostrar información específica de ese tipo

**Lo que aprenderás:**
- Herencia de clases
- Polimorfismo
- Métodos que se "sobrescriben"

**Checklist del proyecto:**
- [ ] Clase `Vehículo` base creada
- [ ] 3 clases derivadas heredan correctamente
- [ ] Método `describir()` es diferente en cada subclase
- [ ] Puedo crear instancias de cada tipo
- [ ] Métodos inherited funcionan en las subclases

---

#### Proyecto 4.3: Gestor de Inventario (Avanzado)
**Qué harás:** Sistema completo de gestión de inventario con POO.

**Requisitos:**
- Clase `Producto`:
  - Atributos: id, nombre, precio, cantidad_stock
  - Métodos: `info()`, `agregar_stock(cant)`, `restar_stock(cant)`, `valor_total()`

- Clase `Inventario`:
  - Gestiona lista de Productos
  - Métodos:
    - `agregar_producto(producto)`
    - `buscar_por_id(id)`: retorna el producto
    - `listar_todos()`
    - `valor_total_inventario()`: suma de todos los productos
    - `productos_bajos_stock(umbral)`: retorna productos con stock < umbral
    - `registrar_venta(id_producto, cantidad)`: vende y reduce stock

- Manejo de excepciones:
  - Si intento vender más de lo que hay en stock → error
  - Si intento buscar un ID que no existe → error

**Lo que aprenderás:**
- Clases que relacionan otras clases
- Gestión de colecciones
- Manejo de errores realista
- Lógica de negocio

**Checklist del proyecto:**
- [ ] Clases `Producto` e `Inventario` creadas
- [ ] Puedo agregar y buscar productos
- [ ] Sistema de ventas funciona
- [ ] Errores manejados correctamente
- [ ] Código bien comentado
- [ ] Mínimo 3 commits en GitHub

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **6-7 horas**
- Proyectos: **8-10 horas**
- **Total semana:** 14-17 horas

---

## SEMANA 5: FastAPI - Tu Primer Backend

### 📖 ¿Por Qué Esta Semana?
**FastAPI** es un framework moderno de Python para construir **APIs REST rápidamente**. Es lo que conecta tu base de datos con el frontend (React, más adelante). Esta semana construyes tu primer backend real.

### 🎓 Conceptos a Aprender

1. **Framework Web: Concepto General**
   - Qué es un framework (herramientas que facilitan construcción de apps)
   - Cliente-Servidor: frontend pide datos, backend responde
   - Rutas: cómo el backend sabe qué hacer con cada request

2. **FastAPI Básico**
   - Crear una app FastAPI
   - Definir rutas (endpoints) con `@app.get()`, `@app.post()`, etc.
   - Parámetros de ruta: `/usuarios/{id}`
   - Parámetros de query: `/usuarios?edad=25`
   - Body de request: datos que envía el cliente
   - Respuestas: qué retorna el backend

3. **Validación de Datos**
   - Pydantic: validar que los datos sean correctos
   - Tipos esperados: string, int, list, etc.
   - Requerido vs opcional
   - Errores automáticos si los datos no son válidos

4. **HTTP Métodos y Status Codes**
   - GET: leer datos (status 200)
   - POST: crear datos (status 201)
   - PUT: actualizar datos (status 200)
   - DELETE: eliminar datos (status 204)
   - Errores: 404 (no encontrado), 400 (datos inválidos), 500 (error servidor)

5. **Ejecución Local**
   - Correr la app en `localhost:8000`
   - Documentación automática en `/docs` (Swagger)
   - Testing con Postman o curl

### 📚 Recursos Recomendados

- **Documentación oficial:** https://fastapi.tiangolo.com/ (Tutorial oficial, muy bueno)
- **Video (2 horas):** "FastAPI Tutorial for Beginners" - Sanjeev Thiyagarajan (YouTube)
- **Video (1.5 horas):** "FastAPI + SQLAlchemy" - CodeWithVinson (YouTube)
- **Herramienta de testing:** https://www.postman.com/ (descargar Postman)
- **Alternativa curl:** https://curl.se/ (ya viene con macOS/Linux)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuál es la diferencia entre `@app.get()` y `@app.post()`?
- ¿Qué es Pydantic y por qué lo necesito?
- ¿Cómo valido que un campo sea un número positivo?
- ¿Cuándo uso path parameter vs query parameter?
- ¿Qué significa status code 201 vs 200?
- ¿Cómo testeo mi API sin frontend?
- ¿Por qué veo documentación automática en `/docs`?

### ✅ Checklist Semanal

- [ ] FastAPI instalado (`pip install fastapi uvicorn`)
- [ ] Puedo crear una ruta GET simple
- [ ] Entiendo path parameters y query parameters
- [ ] Puedo validar datos con Pydantic
- [ ] Sé qué status code usar en cada situación
- [ ] Puedo testear endpoints con Postman o curl
- [ ] Entiendo la diferencia entre GET, POST, PUT, DELETE
- [ ] Puedo ejecutar la app y ver documentación en `/docs`

### 🚀 Proyectos Semana 5

#### Proyecto 5.1: API de Lista de Tareas (Básico)
**Qué harás:** Una API REST simple para gestionar tareas (sin base de datos aún).

**Endpoints:**
- `GET /tareas`: devuelve lista de todas las tareas
- `GET /tareas/{id}`: devuelve una tarea específica
- `POST /tareas`: crea nueva tarea (body: nombre, descripción)
- `DELETE /tareas/{id}`: elimina una tarea

**Datos en memoria:** Usar una lista Python simple (no BD aún)

**Lo que aprenderás:**
- Crear rutas básicas
- Métodos GET y POST
- Validación con Pydantic
- Status codes apropiados

**Checklist del proyecto:**
- [ ] Todos los endpoints creados
- [ ] Pydantic valida datos de entrada
- [ ] GET devuelve datos correctamente
- [ ] POST crea tareas nuevas
- [ ] DELETE elimina correctamente
- [ ] Documentación en `/docs` funciona
- [ ] Testeo con Postman o curl

---

#### Proyecto 5.2: API de Biblioteca (Intermedio)
**Qué harás:** API para gestionar libros (similar a Semana 3, pero ahora con backend).

**Endpoints:**
- `GET /libros`: lista todos los libros (con filtro opcional por autor)
- `GET /libros/{id}`: obtiene un libro
- `POST /libros`: crea nuevo libro (validar que no sea duplicado)
- `PUT /libros/{id}`: actualiza libro
- `DELETE /libros/{id}`: elimina libro
- `GET /autores/{autor}/libros`: todos los libros de un autor

**Validación:**
- Título no puede estar vacío
- Autor no puede estar vacío
- Año debe ser número válido

**Lo que aprenderás:**
- CRUD completo (Create, Read, Update, Delete)
- Filtros y búsquedas
- Validación más compleja

**Checklist del proyecto:**
- [ ] 5+ endpoints funcionando
- [ ] Validación de todos los campos
- [ ] GET con filtros funciona
- [ ] POST crea correctamente
- [ ] PUT actualiza correctamente
- [ ] DELETE elimina correctamente
- [ ] Status codes apropiados en cada caso

---

#### Proyecto 5.3: API de E-Commerce (Avanzado)
**Qué harás:** API completa simulando un carrito de compras.

**Modelos de datos (Pydantic):**
- `Producto`: id, nombre, precio, stock
- `Carrito`: id_usuario, lista de productos, total
- `Pedido`: id, usuario, productos, fecha, estado

**Endpoints:**
- `GET /productos`: lista (con filtro por rango de precio)
- `POST /carrito`: crea carrito para usuario
- `GET /carrito/{usuario_id}`: obtiene carrito actual
- `POST /carrito/{usuario_id}/agregar`: agrega producto al carrito
- `DELETE /carrito/{usuario_id}/producto/{producto_id}`: quita producto
- `POST /carrito/{usuario_id}/checkout`: convierte carrito en pedido
- `GET /pedidos/{usuario_id}`: historial de pedidos

**Lógica de negocio:**
- Al agregar al carrito, verificar que hay stock
- Al hacer checkout, reducir stock
- Calcular total del carrito automáticamente
- Si no hay stock, devolver error 400

**Lo que aprenderás:**
- APIs con lógica compleja
- Manejo de estado (carrito, pedidos)
- Validaciones de negocio
- Error handling avanzado

**Checklist del proyecto:**
- [ ] 7+ endpoints funcionando
- [ ] Validaciones de stock funcionan
- [ ] Carrito persiste datos
- [ ] Checkout funciona correctamente
- [ ] Error handling para casos edge (sin stock, usuario no existe, etc.)
- [ ] Código organizado en funciones/clases
- [ ] Documentación clara en `/docs`

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **5-6 horas**
- Proyectos: **8-10 horas**
- **Total semana:** 13-16 horas

---

## SEMANA 6: FastAPI + SQL (Backend Productivo)

### 📖 ¿Por Qué Esta Semana?
Semana 5 guardaba datos en memoria (se pierden al reiniciar). **Ahora conectarás tu API con PostgreSQL** para guardar datos reales. Este es el backend que usan en producción.

### 🎓 Conceptos a Aprender

1. **ORMs: SQLAlchemy**
   - Qué es un ORM (Object-Relational Mapping): mapea clases Python a tablas de BD
   - Modelos SQLAlchemy: cómo definir tablas como clases
   - Tipos de datos: String, Integer, Float, DateTime, Boolean
   - Relaciones: Foreign Keys, One-to-Many, Many-to-Many

2. **Conexión a Base de Datos**
   - Connection string (cómo conectarse a PostgreSQL)
   - Session: sesión de BD (abrir, usar, cerrar)
   - Dependency Injection en FastAPI para sesiones

3. **CRUD con ORM**
   - Create: insertar registros
   - Read: consultar registros
   - Update: modificar registros
   - Delete: eliminar registros

4. **Migrations (Alembic)**
   - Qué es una migración (historial de cambios en la BD)
   - Crear migraciones automáticamente
   - Versionar cambios en BD

5. **Debugging y Testing**
   - Ver queries SQL que genera SQLAlchemy
   - Testear endpoints que usan BD

### 📚 Recursos Recomendados

- **Documentación:** https://www.sqlalchemy.org/documentation/ (oficial)
- **Video (2 horas):** "SQLAlchemy ORM Tutorial" - Pretty Printed (YouTube)
- **Video (1.5 horas):** "FastAPI + SQLAlchemy + PostgreSQL" - Traversy Media (YouTube)
- **Alembic docs:** https://alembic.sqlalchemy.org/ (migrations)
- **Debugging:** https://docs.sqlalchemy.org/en/14/core/engines.html (enable SQL logging)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuál es la diferencia entre ORM y SQL puro?
- ¿Por qué necesito migraciones?
- ¿Qué es una Foreign Key?
- ¿Cómo relaciono dos tablas en SQLAlchemy?
- ¿Cómo evito inyección SQL?
- ¿Cuándo es mejor SQL puro vs ORM?
- ¿Cómo testeo si mi ORM está generando queries correctas?

### ✅ Checklist Semanal

- [ ] PostgreSQL con BD creada y funcionando
- [ ] SQLAlchemy instalado (`pip install sqlalchemy`)
- [ ] Puedo definir modelos SQLAlchemy simples
- [ ] Conexión a BD funciona desde Python
- [ ] Puedo hacer SELECT, INSERT, UPDATE, DELETE con ORM
- [ ] Entiendo qué es una Foreign Key
- [ ] He creado una migración con Alembic
- [ ] Puedo ver las queries SQL generadas por SQLAlchemy

### 🚀 Proyectos Semana 6

#### Proyecto 6.1: API de Biblioteca Productiva (Básico)
**Qué harás:** Reconvertir tu API de Semana 5 para usar BD real.

**Tablas:**
- `libros`: id, titulo, autor_id, año, isbn
- `autores`: id, nombre, país

**Endpoints (igual que antes, pero ahora con BD):**
- `GET /libros`
- `GET /libros/{id}`
- `POST /libros` (validar ISBN único)
- `PUT /libros/{id}`
- `DELETE /libros/{id}`

**Validaciones nuevas:**
- ISBN único
- Autor debe existir
- Año razonable (1000-2030)

**Lo que aprenderás:**
- Modelos SQLAlchemy
- Relaciones Foreign Key
- Migraciones básicas
- CRUD con BD real

**Checklist del proyecto:**
- [ ] Tablas creadas en PostgreSQL
- [ ] Modelos SQLAlchemy definidos correctamente
- [ ] CRUD funciona contra BD real
- [ ] Validaciones en Pydantic
- [ ] Foreign Key respetada
- [ ] Migración inicial creada con Alembic

---

#### Proyecto 6.2: API de Blog (Intermedio)
**Qué harás:** API para un sistema de blog con usuarios, posts y comentarios.

**Tablas:**
- `usuarios`: id, email, nombre, contraseña (hash), fecha_creación
- `posts`: id, usuario_id (FK), titulo, contenido, fecha_creación, fecha_actualización
- `comentarios`: id, post_id (FK), usuario_id (FK), contenido, fecha_creación

**Endpoints:**
- `POST /usuarios/registrar`: crea usuario (validar email único)
- `GET /posts`: lista todos los posts (con paginación: ?page=1&limit=10)
- `GET /posts/{id}`: obtiene post con sus comentarios
- `POST /posts`: crea post (requiere usuario_id)
- `PUT /posts/{id}`: actualiza post (solo autor puede)
- `DELETE /posts/{id}`: elimina post (solo autor puede)
- `POST /posts/{id}/comentarios`: agrega comentario
- `DELETE /comentarios/{id}`: elimina comentario

**Validaciones:**
- Email válido y único
- Contraseña con mínimo 8 caracteres (hash con bcrypt)
- Post debe tener título
- Usuario no puede actualizar post ajeno

**Lo que aprenderás:**
- Relaciones complejas (many-to-many concepto)
- Paginación
- Autorización básica (solo autor puede editar)
- Queries más complejas

**Checklist del proyecto:**
- [ ] 3 tablas con relaciones correctas
- [ ] CRUD completo funcionando
- [ ] Paginación implementada
- [ ] Validaciones de autorización (user can only edit own posts)
- [ ] Migraciones creadas
- [ ] Mínimo 5 endpoints

---

#### Proyecto 6.3: API de Tienda Productiva (Avanzado)
**Qué harás:** E-commerce real con BD (mejorar Semana 5).

**Tablas:**
- `usuarios`: id, email, nombre, direccion, teléfono
- `categorias`: id, nombre
- `productos`: id, nombre, descripción, precio, stock, categoria_id (FK)
- `carritos`: id, usuario_id (FK), fecha_creación
- `carrito_items`: id, carrito_id (FK), producto_id (FK), cantidad, subtotal
- `pedidos`: id, usuario_id (FK), fecha, estado, total
- `pedido_items`: id, pedido_id (FK), producto_id (FK), cantidad, precio_unitario

**Endpoints:**
- `GET /productos`: lista con filtro (categoría, rango precio, búsqueda por nombre)
- `GET /productos/{id}`: detalle
- `POST /usuarios`: registra usuario
- `GET /carrito/{usuario_id}`: obtiene carrito actual
- `POST /carrito/{usuario_id}/items`: agrega producto (verif stock)
- `PUT /carrito/{usuario_id}/items/{item_id}`: actualiza cantidad
- `DELETE /carrito/{usuario_id}/items/{item_id}`: quita del carrito
- `POST /pedidos`: crea pedido desde carrito (valida stock, reduce stock, vacía carrito)
- `GET /pedidos/{usuario_id}`: historial
- `GET /pedidos/{id}`: detalle de pedido
- `PUT /pedidos/{id}/estado`: actualiza estado (Pendiente → Enviado → Entregado)

**Lógica transaccional:**
- Checkout: debe ser atómico (todo o nada)
- Stock no puede ser negativo
- Precio del pedido no puede cambiar después de creado

**Lo que aprenderás:**
- Transacciones en BD
- Relaciones complejas (many-to-many real)
- Queries con múltiples filtros
- Lógica de negocio realista

**Checklist del proyecto:**
- [ ] 6+ tablas con relaciones correctas
- [ ] CRUD completo
- [ ] Filtros avanzados en listados
- [ ] Checkout funciona correctamente
- [ ] Stock se reduce al hacer pedido
- [ ] Transacciones atómicas
- [ ] Migraciones versionadas
- [ ] Código limpio y bien organizado

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **5-6 horas**
- Proyectos: **9-11 horas**
- **Total semana:** 14-17 horas

---

## SEMANA 7: Frontend Básico con React

### 📖 ¿Por Qué Esta Semana?
Ya tienes un **backend (Python/FastAPI/PostgreSQL) sólido**. Ahora necesitas un **frontend (React)** para que los usuarios interactúen con tu API. Esta semana es introducción a React; profundizarás en Fase 3.

### 🎓 Conceptos a Aprender

1. **React Conceptos Fundamentales**
   - Qué es React (librería para construir UIs dinámicas)
   - **Componentes**: bloques reutilizables (función que retorna JSX)
   - **JSX**: sintaxis que parece HTML pero es JavaScript
   - **Props**: pasar datos de padre a hijo
   - **Estado (State)**: datos que cambian, el componente se re-renderiza
   - **Hooks**: `useState`, `useEffect` (funciones que acceden a características de React)

2. **Setup React**
   - Crear proyecto con Create React App o Vite
   - Estructura de carpetas (components, pages, utils)
   - Archivo package.json (dependencias)

3. **Comunicación con Backend**
   - `fetch()` API para hacer requests HTTP
   - GET: traer datos
   - POST: enviar datos
   - Manejo de errores
   - Loading states

4. **Manejo de Errores y Estados**
   - States para: data, loading, error
   - Mostrar mensajes de error al usuario
   - Spinner/loader mientras carga

5. **Reactividad**
   - `useEffect`: ejecutar código cuando componente monta o props cambian
   - Limpieza de efectos

### 📚 Recursos Recomendados

- **Tutorial oficial:** https://react.dev/learn (excelente, actualizado)
- **Video (3 horas):** "React for Beginners" - The Net Ninja (YouTube)
- **Video (2 horas):** "React Hooks Tutorial" - The Net Ninja (YouTube)
- **Interactivo:** https://learneact.dev.com (ejercicios prácticos)
- **Documentación:** https://developer.mozilla.org/es/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_getting_started

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuál es la diferencia entre componente funcional y de clase?
- ¿Qué es JSX exactamente?
- ¿Cuándo uso `useState` vs variables normales?
- ¿Para qué sirve `useEffect`?
- ¿Cómo paso datos entre componentes?
- ¿Cómo hago fetch desde React?
- ¿Cuál es la diferencia entre prop, state, y variable local?
- ¿Cómo manejo errores en fetch?

### ✅ Checklist Semanal

- [ ] React instalado con npm o yarn
- [ ] Puedo crear componentes funcionales simples
- [ ] Entiendo JSX y puedo escribir código con JSX
- [ ] Puedo usar `useState` para gestionar estado
- [ ] Puedo usar `useEffect` para efectos secundarios
- [ ] Puedo pasar props entre componentes
- [ ] Puedo hacer fetch GET y mostrar datos
- [ ] Puedo hacer fetch POST para crear datos
- [ ] Entiendo cómo manejar loading y error states

### 🚀 Proyectos Semana 7

#### Proyecto 7.1: Aplicación de Clima (Básico)
**Qué harás:** App que consume una API pública de clima.

**Requisitos:**
- Input para ingresar ciudad
- Botón "Buscar"
- Muestra: temperatura actual, descripción, humedad, viento
- Usa API gratuita: https://openweathermap.org/api (API key gratis)
- Maneja casos: ciudad no encontrada, error de red

**Lo que aprenderás:**
- Componentizar (crear componentes reutilizables)
- Fetch con parámetros
- Manejo de errores
- Estados de carga

**Checklist del proyecto:**
- [ ] Input y botón funcionales
- [ ] Fetch a API pública funciona
- [ ] Datos mostrados correctamente
- [ ] Loading spinner mientras carga
- [ ] Error handling (ciudad no existe, sin internet)
- [ ] Componentes bien separados
- [ ] Código limpio

---

#### Proyecto 7.2: Galería de Posts (Intermedio)
**Qué harás:** Conectar tu API de Blog (Semana 6) con React.

**Requisitos:**
- Página que lista posts (GET /posts)
- Click en post → abre detalle con comentarios
- Página de crear post (POST /posts)
- Editar post (PUT /posts/{id})
- Eliminar post
- Paginación (página 1, 2, 3...)

**Frontend:**
- Componente `PostList`: lista de posts
- Componente `PostDetail`: detalle + comentarios
- Componente `PostForm`: crear/editar
- Estados: posts, currentPost, loading, error

**Lo que aprenderás:**
- Navegar entre pages (con rutas, si instalas react-router)
- Múltiples endpoints
- Formularios (inputs, buttons, validación básica)
- Refrescar después de crear/editar
- Comunicación real con tu backend

**Checklist del proyecto:**
- [ ] Lista de posts carga correctamente
- [ ] Puedo ver detalles de un post
- [ ] Formulario de crear post funciona
- [ ] Editar post funciona
- [ ] Eliminar post funciona
- [ ] Paginación funciona
- [ ] Error handling en todos lados
- [ ] Navegación intuitiva

---

#### Proyecto 7.3: Dashboard de Tienda (Avanzado)
**Qué harás:** Frontend completo para tu API de tienda.

**Páginas:**
1. **Home**: listado de productos (con filtros)
2. **Detalle Producto**: información, agregar al carrito
3. **Carrito**: ver items, cambiar cantidades, checkout
4. **Pedidos**: histórico de pedidos del usuario
5. **Admin** (si tiempo): listar productos, crear nuevo, editar

**Componentes:**
- `ProductCard`: muestra producto
- `ProductFilter`: filtro por categoría, precio
- `Cart`: muestra carrito
- `CartItem`: item individual
- `OrderHistory`: tabla de pedidos
- `Form`: crear/editar producto

**Funcionalidad:**
- Login básico (guarda usuario en localStorage)
- Carrito persiste en localStorage
- Checkout: POST a tu API
- Mostrar estado del pedido

**Lo que aprenderás:**
- App más grande y realista
- Múltiples páginas (introducción a routing)
- Persistencia en localStorage
- Flujo de compra completo
- Separación de componentes
- Estados compartidos (carrito global)

**Checklist del proyecto:**
- [ ] Todas las páginas funcionales
- [ ] Productos carga del backend
- [ ] Filtros funcionan
- [ ] Carrito persiste
- [ ] Checkout funciona
- [ ] Error handling completo
- [ ] Código organizado (carpeta de componentes)
- [ ] Responsive (ve bien en celular)

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **6-7 horas**
- Proyectos: **8-10 horas**
- **Total semana:** 14-17 horas

---

# 🚀 FASE 3: DIFERENCIADORES (Semanas 8–10)

## SEMANA 8: Docker y Containerización

### 📖 ¿Por Qué Esta Semana?
Hasta ahora, tu código funciona **en tu máquina**. ¿Pero si lo ejecutas en otra máquina o en un servidor? **Docker** empaqueta tu app con todo lo que necesita (Python, dependencias, BD, etc.) en un "contenedor" que funciona igual en cualquier lado.

### 🎓 Conceptos a Aprender

1. **Concepto de Contenedores**
   - Diferencia entre máquina virtual y contenedor
   - Imagen Docker: blueprint (receta)
   - Contenedor: instancia de la imagen (app corriendo)
   - Dockerhub: repositorio de imágenes públicas

2. **Dockerfile**
   - Cómo escribir un Dockerfile (instrucciones para buildear imagen)
   - `FROM`: imagen base
   - `WORKDIR`: carpeta de trabajo
   - `COPY`: copiar archivos
   - `RUN`: ejecutar comandos
   - `CMD`: comando por defecto al iniciar

3. **Docker Compose**
   - Cómo definir múltiples servicios (backend + BD)
   - Archivos YAML
   - Redes entre contenedores
   - Volúmenes para persistencia
   - Iniciar todo con `docker-compose up`

4. **Workflows**
   - Buildear imagen
   - Correr contenedor localmente
   - Pushear a Dockerhub
   - Tirar abajo contenedores

### 📚 Recursos Recomendados

- **Documentación oficial:** https://docs.docker.com/ (oficial, completa)
- **Video (1.5 horas):** "Docker Crash Course" - Traversy Media (YouTube)
- **Video (1 hora):** "Docker Compose Tutorial" - Techno Tim (YouTube)
- **Interactive:** https://www.katakoda.com/docker (sandbox interactivo)
- **Guía visual:** "A Visual Guide to Docker" (Medium)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuál es la diferencia entre imagen y contenedor?
- ¿Qué debo poner en un Dockerfile?
- ¿Cuándo uso Docker Compose?
- ¿Cómo paso variables de entorno a un contenedor?
- ¿Cómo persisten los datos en Docker?
- ¿Por qué usar Docker si funciona en mi máquina?
- ¿Cómo conecto dos contenedores (backend + BD)?

### ✅ Checklist Semanal

- [ ] Docker instalado (`docker --version`)
- [ ] Puedo buildear una imagen simple
- [ ] Puedo correr un contenedor
- [ ] Entiendo layers en Docker
- [ ] Puedo escribir un Dockerfile funcional
- [ ] Puedo usar docker-compose para múltiples servicios
- [ ] Entiendo volúmenes para persistencia
- [ ] Sé cómo pasar variables de entorno

### 🚀 Proyectos Semana 8

#### Proyecto 8.1: Dockerizar tu API (Básico)
**Qué harás:** Crear Dockerfile para tu API de FastAPI.

**Requisitos:**
- Dockerfile que:
  - Usa imagen Python 3.9
  - Copia código
  - Instala dependencias (requirements.txt)
  - Expone puerto 8000
  - Corre uvicorn
- Testear que funciona: `docker build` y `docker run`

**Lo que aprenderás:**
- Estructura básica de Dockerfile
- Build y run
- Puertos expuestos
- Entrypoint

**Checklist del proyecto:**
- [ ] Dockerfile creado
- [ ] Imagen buildea sin errores
- [ ] Contenedor corre correctamente
- [ ] API accesible en localhost:8000
- [ ] Cambios en código no requieren rebuild (si usas volúmenes)

---

#### Proyecto 8.2: Docker Compose para Full-Stack (Intermedio)
**Qué harás:** Levantar tu backend + PostgreSQL con un solo comando.

**docker-compose.yml:**
- Servicio `backend`: tu FastAPI
- Servicio `db`: PostgreSQL
- Red compartida entre servicios
- Volúmenes: para BD persista datos
- Variables de entorno: contraseña DB, etc.

**Requisitos:**
- `docker-compose up` levanta backend + BD
- Backend se conecta a BD automáticamente
- `docker-compose down` detiene todo
- Datos en BD persisten (volumen nombrado)

**Lo que aprenderás:**
- docker-compose YAML
- Networking entre contenedores
- Volúmenes nombrados
- Variables de entorno
- Ordening (esperar a que BD esté lista)

**Checklist del proyecto:**
- [ ] docker-compose.yml creado
- [ ] `docker-compose up` levanta todo
- [ ] Backend conecta a BD
- [ ] Crear datos en API persisten
- [ ] `docker-compose down` y `up` nuevamente: datos están
- [ ] Logs son legibles (sin errores)

---

#### Proyecto 8.3: Full Stack en Docker (Avanzado)
**Qué harás:** Backend + BD + Frontend en Docker Compose.

**docker-compose.yml:**
- Servicio `backend`: FastAPI (puerto 8000)
- Servicio `db`: PostgreSQL (puerto 5432, no exposición pública)
- Servicio `frontend`: React (puerto 3000)
- Volúmenes para desarrollo (hot reload)
- Network compartida

**Requisitos:**
- Frontend en contenedor (Dockerfile para React)
- Frontend hace requests a `http://backend:8000` (no localhost, nombre del servicio)
- Todo funciona con un único `docker-compose up`
- Cambios en código del frontend reflejan sin rebuild (volumen)

**Lo que aprenderás:**
- Orquestación completa
- Service discovery (cómo se comunican contenedores)
- Dockerizar React
- Debugging multi-contenedor

**Checklist del proyecto:**
- [ ] `docker-compose up` levanta todo
- [ ] Frontend accesible en localhost:3000
- [ ] Backend accesible desde frontend
- [ ] BD funciona
- [ ] Cambios en código reflejan (hot reload)
- [ ] `docker-compose logs` muestra todo ordenado
- [ ] Pruebas: crear producto, ver en frontend

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **4-5 horas**
- Proyectos: **7-9 horas**
- **Total semana:** 11-14 horas

---

## SEMANA 9: Cloud Basics (AWS) + CI/CD

### 📖 ¿Por Qué Esta Semana?
Tu app está en Docker. Ahora necesitas **hospedarla en la nube** para que sea accesible 24/7. **AWS** es el cloud más demandado en Chile. También aprenderás **CI/CD** para que cada vez que hagas push, tu código se testee y depliegue automáticamente.

### 🎓 Conceptos a Aprender

1. **AWS Basics**
   - Qué es AWS (proveedor cloud: servidores bajo demanda)
   - EC2: máquinas virtuales
   - S3: almacenamiento de archivos
   - RDS: bases de datos managed
   - Elastic Beanstalk: deploy fácil (recomendado para principiantes)
   - Regiones y Availability Zones

2. **Elastic Beanstalk (para Deploy)**
   - Deploy de aplicaciones sin gestionar servidores
   - Sube tu código, AWS gestiona escalabilidad
   - Environment: desarrollo, staging, producción

3. **GitHub Actions (CI/CD)**
   - Qué es CI/CD (Continuous Integration/Deployment)
   - Workflows: automatizar tests, linting, deploy
   - Triggers: cuando pusheo código
   - Actions: scripts que corre automáticamente
   - Badge: mostrar estado en GitHub

4. **Basics de DevOps**
   - Environment: dev vs prod
   - Secrets: guardar credenciales seguramente
   - Logs: ver qué pasó en producción

### 📚 Recursos Recomendados

- **AWS Tutorial:** https://aws.amazon.com/es/getting-started/ (oficial)
- **Video (1.5 horas):** "AWS for Beginners" - A Cloud Guru (YouTube)
- **Video (1 hora):** "GitHub Actions Tutorial" - Traversy Media (YouTube)
- **Capa gratuita AWS:** https://aws.amazon.com/es/free/ (acceso gratis por 1 año)
- **GitHub Actions docs:** https://docs.github.com/en/actions

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Qué es un ambiente y por qué tener dev, staging, prod?
- ¿Cómo guardo secrets (contraseñas) de forma segura?
- ¿Qué es CI y CD exactamente?
- ¿Cuándo correr tests automáticamente?
- ¿Cómo monitoreo mi app en la nube?
- ¿Cuánto cuesta AWS?
- ¿Cuál es la diferencia entre Elastic Beanstalk y EC2?

### ✅ Checklist Semanal

- [ ] Cuenta AWS creada (Capa Gratuita)
- [ ] Entiendo qué es EC2, S3, RDS
- [ ] Entiendo Elastic Beanstalk
- [ ] He creado un repositorio GitHub Actions
- [ ] Entiendo qué es un workflow YAML
- [ ] Sé cómo pasar secrets a workflows
- [ ] He deployado una app simple a Elastic Beanstalk
- [ ] He visto logs en CloudWatch

### 🚀 Proyectos Semana 9

#### Proyecto 9.1: Deploy Simple en Elastic Beanstalk (Básico)
**Qué harás:** Deployar tu API de FastAPI a AWS.

**Requisitos:**
- Crear Elastic Beanstalk environment
- Conforme archivo `.ebextensions/` si es necesario
- Deployar código con `eb deploy`
- API accesible públicamente en URL de AWS
- Base de datos RDS (managed PostgreSQL)

**Lo que aprenderás:**
- Crear recurso en AWS
- Deploy básico
- Conectar a BD managed
- Ver logs en CloudWatch

**Checklist del proyecto:**
- [ ] Elastic Beanstalk environment creado
- [ ] RDS PostgreSQL creado
- [ ] `eb deploy` funciona
- [ ] API accesible públicamente
- [ ] Puedo crear datos y persistir
- [ ] Logs visibles en CloudWatch

---

#### Proyecto 9.2: CI/CD con GitHub Actions (Intermedio)
**Qué harás:** Automatizar tests y deploy con GitHub Actions.

**Workflow:**
1. Cuando pusheo código → GitHub Actions corre
2. Instala dependencias
3. Corre tests (si los tienes)
4. Corre linter (check de código)
5. Si todo pasa → deploya a Elastic Beanstalk

**Lo que aprenderás:**
- Workflows YAML
- Runners (máquinas que ejecutan)
- Secrets (pasar AWS credentials)
- Artifacts (almacenar outputs)
- Status checks en PRs

**Checklist del proyecto:**
- [ ] `.github/workflows/main.yml` creado
- [ ] Workflow se dispara al pushear
- [ ] Tests corren automáticamente
- [ ] Deploy solo si tests pasan
- [ ] Badge de status en README
- [ ] Secrets configurados (sin exponer credenciales)

---

#### Proyecto 9.3: Full Stack Deploy (Avanzado)
**Qué harás:** Deployar backend + frontend + BD a AWS + CI/CD.

**Arquitectura:**
- **Backend:** Elastic Beanstalk + RDS PostgreSQL
- **Frontend:** S3 + CloudFront (CDN)
- **CI/CD:** GitHub Actions deploya ambos

**Requisitos:**
- Build del frontend: `npm build` genera carpeta `build/`
- S3 bucket + CloudFront distribution
- Backend URL en variables de entorno del frontend
- Workflow deploya backend a EB y frontend a S3
- Dominio personalizado (opcional, pero nice-to-have)

**Lo que aprenderás:**
- Desacoplamiento frontend/backend en cloud
- CDN para servir frontend
- Deploy de múltiples servicios
- Coordinar deploys

**Checklist del proyecto:**
- [ ] Frontend hosteado en S3 + CloudFront
- [ ] Backend en Elastic Beanstalk
- [ ] Frontend se conecta al backend en la nube
- [ ] Workflow deploya ambos automáticamente
- [ ] Dominio personalizado (si quieres)
- [ ] Monitoreo en CloudWatch
- [ ] Logs accesibles

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **4-5 horas**
- Proyectos: **6-8 horas**
- **Total semana:** 10-13 horas

---

## SEMANA 10: IA Aplicada + Automatización

### 📖 ¿Por Qué Esta Semana?
**IA aplicada es un diferenciador** en 2026. No necesitas PhD en ML, pero sí saber integrar APIs de IA (OpenAI, Claude, etc.) en tus aplicaciones. Automatización low-code te permite crear workflows sin escribir código.

### 🎓 Conceptos a Aprender

1. **APIs de IA (OpenAI/Anthropic)**
   - Qué es una API de LLM (modelo de lenguaje)
   - Cómo llamar OpenAI API desde Python
   - Conceptos: prompt, tokens, temperatura
   - Use cases: chatbots, resúmenes, clasificación

2. **RAG (Retrieval Augmented Generation)**
   - Qué es RAG (combinar tu data con IA)
   - Embeddings: convertir texto a números (para búsqueda semántica)
   - Vector databases: guardar embeddings
   - Flujo: pregunta → búsqueda → IA → respuesta

3. **LangChain Básico**
   - Librería para orquestar LLMs
   - Chains: secuencias de prompts
   - Memory: recordar conversación previa
   - Tools: conectar con APIs externas

4. **Automatización Low-Code (n8n, Make)**
   - Crear workflows sin código
   - Triggers, actions, conditions
   - Integraciones: Google Sheets, Slack, OpenAI, etc.

### 📚 Recursos Recomendados

- **OpenAI API docs:** https://platform.openai.com/docs/ (official)
- **Video (1.5 horas):** "ChatGPT API Tutorial" - Traversy Media (YouTube)
- **LangChain docs:** https://python.langchain.com/en/latest/ (oficial)
- **n8n docs:** https://docs.n8n.io/ (low-code automation)
- **Video (1 hora):** "n8n for Beginners" - n8n (YouTube)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuánto cuesta usar OpenAI API?
- ¿Qué es un token en IA?
- ¿Cuándo usar RAG?
- ¿Qué diferencia hay entre prompt engineering y fine-tuning?
- ¿Cómo hago un chatbot con memoria?
- ¿Cuándo usar n8n vs código?
- ¿Cómo evito que la IA sea lenta?

### ✅ Checklist Semanal

- [ ] Cuenta OpenAI creada y API key generada
- [ ] Puedo llamar OpenAI API desde Python
- [ ] Entiendo qué es un prompt
- [ ] Sé qué es un embedding y embeddings
- [ ] Entiendo concepto de RAG
- [ ] He instalado LangChain
- [ ] He creado una cadena simple con LangChain
- [ ] Entiendo cómo funciona n8n
- [ ] He creado un workflow básico en n8n

### 🚀 Proyectos Semana 10

#### Proyecto 10.1: Chatbot con OpenAI (Básico)
**Qué harás:** Crear un chatbot conversacional que usa OpenAI API.

**Requisitos:**
- Backend (FastAPI) con endpoint `/chat`
- Frontend: chat box donde escribo mensajes
- Mensajes guardados en sesión
- Contexto: el chatbot recuerda mensajes previos

**Flujo:**
1. Usuario escribe pregunta
2. Frontend POST a backend con mensaje
3. Backend llama OpenAI API
4. Respuesta se muestra en el chat

**Lo que aprenderás:**
- Integración de APIs de IA
- Prompts basics
- Historial de conversación
- Error handling (si OpenAI está lento)

**Checklist del proyecto:**
- [ ] OpenAI API key configurada (en .env)
- [ ] Endpoint POST /chat creado
- [ ] Frontend muestra chat conversacional
- [ ] Historial se mantiene
- [ ] Manejo de errores (rate limit, error de API)
- [ ] Respuestas se muestran progresivamente (si stream)

---

#### Proyecto 10.2: Resumidor de PDFs con RAG (Intermedio)
**Qué harás:** Sube un PDF y haz preguntas sobre él.

**Requisitos:**
- Endpoint para subir PDF
- Extraer texto del PDF (librería `pypdf` o `pdfplumber`)
- Crear embeddings del texto (OpenAI)
- Almacenar embeddings en memoria (o vector DB como Pinecone)
- Endpoint para preguntar: busca contexto relevante + llama IA

**Flujo:**
1. Usuario sube PDF
2. Backend extrae texto, crea embeddings, guarda
3. Usuario pregunta algo
4. Backend: busca párrafos relevantes → crea prompt → llama OpenAI
5. Respuesta se muestra

**Lo que aprenderás:**
- Procesamiento de PDFs
- Embeddings y búsqueda semántica
- RAG workflow
- Vector similarity search

**Checklist del proyecto:**
- [ ] Endpoint POST /upload-pdf funciona
- [ ] PDF se procesa correctamente
- [ ] Embeddings se crean y guardan
- [ ] Búsqueda semántica funciona
- [ ] Respuestas son relevantes
- [ ] Manejo de PDFs grandes (chunking)

---

#### Proyecto 10.3: Workflow Automatizado (Avanzado)
**Qué harás:** Crear un workflow n8n que automatiza algo útil.

**Ideas:**
1. **Email Workflow:** Emails nuevos en Gmail → extrae links → guarda en Spreadsheet
2. **Social Media:** Nuevas menciones en Twitter → analiza con OpenAI → envía Slack
3. **Content Generation:** Schedule → genera post con IA → publica en blog
4. **Data Pipeline:** Scrapes web → procesa con IA → guarda en BD

**Requisitos:**
- Workflow tiene trigger (evento), actions (qué hacer)
- Usa al menos 1 integración de IA
- Usa al menos 1 integración de datos (Google Sheets, DB, etc.)
- Probado y funcionando

**Lo que aprenderás:**
- Orquestación no-code
- Integraciones
- Workflows multipasos

**Checklist del proyecto:**
- [ ] Workflow creado en n8n
- [ ] Trigger funciona
- [ ] Acciones ejecutan correctamente
- [ ] IA integrada
- [ ] Datos persisten
- [ ] Documentación del workflow
- [ ] Workflow testado end-to-end

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **4-5 horas**
- Proyectos: **7-9 horas**
- **Total semana:** 11-14 horas

---

# 💼 FASE 4: EMPAQUETADO Y POSTULACIÓN (Semanas 11–12)

## SEMANA 11: Portfolio Profesional y GitHub Optimization

### 📖 ¿Por Qué Esta Semana?
Hiciste 12 proyectos en 10 semanas. **Ahora necesitas empaquetarlos profesionalmente** para que reclutadores los vean. Tu GitHub es tu portafolio; tu README es tu vendedor.

### 🎓 Conceptos a Aprender

1. **README Excellence**
   - Estructura: qué es, cómo instalar, cómo usar, screenshots, stack
   - Badges: build status, version, license
   - Demo link: URL donde pueden verlo live
   - Instrucciones claras (asumir que el lector no sabe nada)

2. **Deployment y Demo Live**
   - Vercel: para frontend React (gratis)
   - Render/Railway: para backend (gratis tier)
   - GitHub Pages: para sitios estáticos

3. **README de GitHub Profile**
   - Presentación personal
   - Pinear 3-4 repos importantes
   - Mostrar skills gráficamente

4. **Documentación Técnica**
   - Decisiones de arquitectura (por qué FastAPI y no Django)
   - Setup local (cómo correr el proyecto en otra máquina)
   - API Documentation (endpoints, parámetros, respuestas)
   - Contributing guidelines (si quieres colaboradores)

5. **Blog Technical (Opcional pero +plus)**
   - Escribir 1-2 posts sobre qué aprendiste
   - Plataforma: Medium, Dev.to, Hashnode
   - Linkear desde GitHub

### 📚 Recursos Recomendados

- **README Template:** https://github.com/othneildrew/Best-README-Template (template profesional)
- **Badges:** https://shields.io/ (crear badges para README)
- **Vercel Deploy:** https://vercel.com/docs (documentación)
- **Render Deploy:** https://render.com/docs (documentación)
- **Writing Good READMEs:** https://www.youtube.com/watch?v=eUqNgsr0-Og (video)

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Qué debe incluir un README profesional?
- ¿Cómo hago que mi repo sea "destacable"?
- ¿Debo pinear todos mis proyectos?
- ¿Cómo pongo demo live gratis?
- ¿Qué es GitHub Pages?
- ¿Cómo escribo documentación de API?
- ¿Vale la pena escribir un blog?

### ✅ Checklist Semanal

- [ ] GitHub profile configurado con foto profesional y bio
- [ ] 3-4 repos están pinneados (los mejores)
- [ ] Cada repo tiene README excelente
- [ ] README incluye: descripción, instalación, uso, stack, demo link
- [ ] Frontend deployado en Vercel
- [ ] Backend deployado en Render/Railway
- [ ] Repo principal tiene badge de status/build
- [ ] GitHub profile README creado (opcional, pero plus)

### 🚀 Proyectos Semana 11

#### Proyecto 11.1: README Profesional (Básico)
**Qué harás:** Mejorar el README de tu mejor proyecto.

**Checklist de inclusión:**
- [ ] Título claro y atractivo
- [ ] Descripción de qué es (1 párrafo)
- [ ] Screenshot o GIF del proyecto funcionando
- [ ] Stack (tecnologías usadas)
- [ ] Instalación paso a paso (clonar, instalar dependencias, configurar BD, correr)
- [ ] Uso básico (cómo correr localmente)
- [ ] Live demo link
- [ ] Features principales listados
- [ ] Roadmap (qué falta)
- [ ] Contributing (opcional)
- [ ] License

**Lo que aprenderás:**
- Comunicación técnica
- Presentación de proyectos

---

#### Proyecto 11.2: Deploy Full-Stack con Demo Live (Intermedio)
**Qué harás:** Deployar tu mejor full-stack (backend + frontend).

**Requisitos:**
- Frontend en Vercel (vercel.com/new, selecciona repo, done)
- Backend en Render/Railway
- Frontend conecta al backend en producción
- Links en README funcionan
- Dominio personalizado (opcional)

**Lo que aprenderás:**
- Deployment práctico
- Conectar frontend a backend en producción
- Variables de entorno en plataformas cloud

---

#### Proyecto 11.3: GitHub Profile Profesional (Avanzado)
**Qué harás:** Crear un perfil GitHub impresionante.

**Componentes:**
- README en `username/username` (GitHub Lee automáticamente)
- Bio clara en el perfil
- Link a portfolio personal (si tienes)
- 4 repos pinneados (tus mejores proyectos)
- Readme de cada repo está perfecto
- Siguiendo a referentes de la industria
- Contribuciones activas (verde en el grafo)

**Lo que aprenderás:**
- Personal branding técnico
- Cómo se ve tu perfil desde ojos de recruiter

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **3-4 horas**
- Proyectos: **6-8 horas**
- **Total semana:** 9-12 horas

---

## SEMANA 12: CV, LinkedIn, Entrevistas y Postulación

### 📖 ¿Por Qué Esta Semana?
Ya tienes **portafolio, skills, proyectos**. Ahora necesitas **CV, LinkedIn optimizado** y estar listo para hablar de ti. Esta es la semana final: preparación para entrevistas y postulación real.

### 🎓 Conceptos a Aprender

1. **CV Profesional**
   - Formato: 1 página, PDF
   - Secciones: contacto, resumen, experiencia, proyectos, skills, educación
   - Lenguaje: verbos de acción, resultados cuantificables
   - No mentir: falsificación resulta en despido inmediato

2. **LinkedIn Optimization**
   - Headline: "Junior Full-Stack Developer | Python | FastAPI | React"
   - Foto profesional (rompe el hielo)
   - About: historia personal, qué buscas, logros
   - Experience: tus proyectos como si fueran trabajos
   - Skills: endorsements
   - Recomendaciones (pide a mentores)

3. **Inglés Técnico**
   - Vocabulario de job postings
   - Entender ofertas
   - Email profesional en inglés
   - Conversación básica

4. **Práctica de Entrevistas**
   - Preguntas técnicas (LeetCode easy level)
   - Preguntas conductuales (STAR method)
   - Explicar tus proyectos en voz alta
   - Preguntas para hacer TÚ (demuestra interés)

5. **Estrategia de Postulación**
   - Dónde buscar: LinkedIn, GetOnBoard, Computrabajo
   - Cómo seleccionar: skills match > salary
   - Tasa de éxito: espera 100 postulaciones = 5 entrevistas = 1 oferta
   - Perseverancia: esto es un números game

### 📚 Recursos Recomendados

- **CV Template:** https://www.canva.com/es_cl/plantillas/curriculums/ (plantillas gratis)
- **LinkedIn Guide:** https://www.linkedin.com/help/linkedin/answer/90-where-can-i-find-information-on-setting-up-my-profile (oficial)
- **LeetCode:** https://leetcode.com/problemset/ (problemas fáciles)
- **Interview Prep:** https://www.interviewkakao.com/ (preguntas comunes)
- **STAR Method:** https://www.themuse.com/advice/tell-me-about-a-time-you-failed (guía)
- **Portales de empleo:** LinkedIn, GetOnBoard, Computrabajo, StackOverflow Jobs

### ❓ Preguntas que Puedo Responder Esta Semana

- ¿Cuántas líneas debe tener mi CV?
- ¿Qué hago si nunca trabajé como developer?
- ¿Cuántas palabras clave debo poner en LinkedIn?
- ¿Cómo explico mis proyectos sin sonar como junior?
- ¿Cuánto debo esperar como primer sueldo?
- ¿Cómo negocio un offer?
- ¿Qué hacer si me rechazan?

### ✅ Checklist Semanal

- [ ] CV en 1 página, PDF, español e inglés
- [ ] LinkedIn perfil optimizado
- [ ] 3 primeros párrafos del About sean impactantes
- [ ] Bio de LinkedIn clara y profesional
- [ ] Foto profesional en ambos
- [ ] LeetCode: resuelto 10 easy problems
- [ ] STAR method: preparadas 3 historias
- [ ] Explicación en voz alta: cada proyecto en 2 minutos
- [ ] Lista de empresas objetivo creada
- [ ] Primer set de postulaciones lista

### 🚀 Proyectos Semana 12

#### Proyecto 12.1: CV Profesional (Básico)
**Qué harás:** Crear CV en 1 página.

**Secciones:**
- Contacto: nombre, email, LinkedIn, GitHub, teléfono
- Resumen: 3-4 líneas de quién eres y qué buscas
- Experiencia: tus 3 mejores proyectos (formato: impacto cuantificable)
- Skills: Python, FastAPI, PostgreSQL, React, Docker, AWS, Git
- Educación: carrera, fecha

**Tono:** Profesional, conciso, orientado a resultados

---

#### Proyecto 12.2: LinkedIn Optimization (Intermedio)
**Qué harás:** Perfil LinkedIn para conseguir oportunidades.

**Checklist:**
- [ ] Foto profesional
- [ ] Headline atractivo
- [ ] About (150+ palabras): quién soy, qué busco, logros
- [ ] Experience: 3-5 proyectos como "trabajos"
- [ ] Skills: 10+ endorsadas
- [ ] Recomendaciones: al menos 1 (pide a profesor/mentor)
- [ ] Background: conectado a GitHub
- [ ] Activo: post 1-2 veces por mes sobre aprendizajes

---

#### Proyecto 12.3: Preparación para Entrevistas (Avanzado)
**Qué harás:** Ensayar entrevista completa.

**Componentes:**
1. **Técnico:** Resuelve 10 problemas easy de LeetCode
2. **Conductual:** Grabar video respondiendo:
   - "Háblame de ti"
   - "¿Por qué quieres este trabajo?"
   - "Cuéntame de un proyecto que te enorgullece"
   - "¿Cuál fue tu mayor desafío?"
3. **Proyectos:** Explicar cada uno en 2 minutos
4. **Preguntas para hacer:** 5 preguntas inteligentes para el entrevistador

**Lo que aprenderás:**
- Comunicación bajo presión
- Estructuración clara

---

### ⏱️ Tiempo Estimado
- Conceptos + recursos: **3-4 horas**
- Proyectos + práctica: **6-8 horas**
- **Total semana:** 9-12 horas

---

# 🎯 Resumen Ejecutivo: 12 Semanas

| Semana | Tema | Stack | Salida |
|--------|------|-------|--------|
| 1 | Git + GitHub | - | Portfolio on GH |
| 2 | HTML/CSS/JS | Frontend | Proyectos interactivos |
| 3 | SQL + APIs | Backend | BD + REST concepts |
| 4 | Python POO | Python | Sistema con clases |
| 5 | FastAPI Basics | Backend | API REST en memoria |
| 6 | FastAPI + SQL | Backend | API + BD real |
| 7 | React Basics | Frontend | Frontend conectado a backend |
| 8 | Docker | DevOps | Full-stack containerizado |
| 9 | Cloud + CI/CD | AWS + GitHub | Deploy automático en nube |
| 10 | IA + Automatización | OpenAI + n8n | Diferenciador de mercado |
| 11 | Portfolio Profesional | GitHub | Portafolio visible |
| 12 | CV + LinkedIn + Entrevistas | Soft Skills | Listo para postular |

---

# 📋 Cómo Empezar Hoy

1. **Semana 1:** Abre terminal → `git config --global user.name "Tu Nombre"`
2. **Cada semana:** Lee "Conceptos a Aprender" → Ve recursos → Haz proyectos
3. **Cada proyecto:** Push a GitHub con commits descriptivos
4. **Si te atasques:** Pregúntame sobre cualquier concepto (aquí estoy)
5. **Si algo no tiene sentido:** Es normal. Te lo explico de otra forma.

---

# ⚠️ Notas Finales

- **Velocidad vs Profundidad:** Es mejor entender 80% profundamente que 100% superficialmente. Si necesitas 2 semanas en una fase, está bien.
- **Proyectos > Teoría:** Los proyectos son donde aprenderás. No te saltes.
- **Comunidad:** Busca grupo de estudio, Discord de developers chilenos, etc.
- **Mentalidad:** Esto es maratón, no sprint. Consistencia > intensidad.
- **Mercado Chileno 2026:** Hay demanda. Sé paciente y persistente.

---

**¿Listo para empezar? Comencemos la Semana 1. ¿Alguna pregunta antes de comenzar?**
