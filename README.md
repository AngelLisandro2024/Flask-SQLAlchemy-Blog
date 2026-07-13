# 📝 Flask & SQLAlchemy Blog Engine

Un sistema de blog minimalista diseñado para la gestión y persistencia de publicaciones. Este proyecto representa la evolución hacia el desarrollo backend con bases de datos relacionales, utilizando un mapeador de objeto-relacional (ORM) para interactuar con un motor de base de datos local de manera eficiente y segura.

---

## 🚀 Características Técnicas

* **🗄️ Persistencia con SQLite & SQLAlchemy:** Configuración de un motor de base de datos relacional ligero (`blog.db`) mediante **Flask-SQLAlchemy**. Define un modelo de datos estructurado (`Post`) para almacenar títulos, fechas automáticas de creación (`datetime.now`) y cuerpos de texto.
* **🔨 Inicialización Controlada del Esquema:** Uso de un script de contexto de aplicación (`create_db.py`) para generar las tablas correspondientes de forma segura en la base de datos antes de arrancar el servidor.
* **🧩 Maquetación Dinámica (Jinja2):** Implementación de layouts heredables (`layout.html` -> `inicio.html`). El contenido de cada publicación se consulta desde la base de datos en orden cronológico descendente y se inyecta directamente en las plantillas.
* **🎨 Interfaz Limpia y Responsiva:** Estilos CSS personalizados estructurados desde cero (sin depender de frameworks de terceros) empleando unidades relativas (`rem`, `vh`), sistemas de alineación modernos (`Flexbox`) y un esquema de colores sobrio orientado a la lectura de artículos.

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3 / Flask Microframework
* **ORM / Base de Datos:** Flask-SQLAlchemy / SQLite 3
* **Frontend:** HTML5 / CSS3 Personalizado (Layout Flexbox)
* **Control de Plantillas:** Jinja2 Template Engine

---

## 📂 Estructura del Proyecto

* `app.py`: Controlador principal de la aplicación. Configura la base de datos, define el modelo `Post` y expone las rutas principales de lectura y creación de contenido.
* `create_db.py`: Script de utilidad para la creación y setup del archivo de base de datos local dentro del contexto de la aplicación.
* `templates/`: Carpeta que almacena las vistas HTML estruturadas bajo herencia de plantillas (`layout.html` como plantilla maestra).
* `static/`: Contiene el archivo de diseño `style.css` que centraliza los estilos visuales de todo el portal.
* `blog.db`: Archivo SQLite generado automáticamente para almacenar las publicaciones del blog.

---

## 👨‍💻 Sobre el Desarrollador
**Ángel Fernández** | **T.S.U en Informática** Desarrollador enfocado en la arquitectura de software, con experiencia práctica conectando lógica de servidor, bases de datos relacionales y renderizado dinámico en la web.
