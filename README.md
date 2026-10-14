# 📦 Sistema de Gestión de Inventario y Ventas - Backend Evaluación 2

Aplicación web desarrollada con **Django 5**, **Python 3.12**, y **PostgreSQL (Supabase)**, desplegada en producción sobre **Vercel** utilizando arquitectura Serverless y diseño moderno con **Tailwind CSS**.

---

## 🚀 Enlace en Producción

* **Sitio Web (Catálogo y CRUD):** [https://backendeva-2-steel.vercel.app/](https://backendeva-2-steel.vercel.app/)
* **Panel de Administración:** [https://backendeva-2-steel.vercel.app/admin/](https://backendeva-2-steel.vercel.app/admin/)

---

## 🛠️ Tecnologías y Arquitectura

* **Backend:** Django 5 (Python 3.12)
* **Base de Datos:** PostgreSQL en la nube (Supabase)
* **Frontend:** HTML5 semántico, plantillas Django y Tailwind CSS (Tema Dark)
* **Archivos Estáticos:** WhiteNoise con almacenamiento comprimido (`CompressedManifestStaticFilesStorage`)
* **Despliegue:** Vercel (WSGI Serverless Function)
* **Seguridad:** Variables de entorno protegidas con `python-dotenv` y configuración de orígenes confiables (`CSRF_TRUSTED_ORIGINS`).

---

## 📋 Funcionalidades Implementadas

1. **Gestión de Productos (CRUD Completo):**
   * Listado con **paginación dinámica del lado del servidor** (5 productos por página con `ListView`).
   * Creación (`CreateView`), Actualización (`UpdateView`) y Eliminación protegida (`DeleteView`).
   * Feedback visual mediante mensajes flotantes del framework `django.contrib.messages` y `SuccessMessageMixin`.
2. **Lógica de Ventas y Descuento de Stock:**
   * Modelos relacionados: `Producto`, `Venta` y `DetalleVenta`.
   * Validación de disponibilidad en el método `clean()` para evitar stock negativo.
   * Reducción automática de existencias y cálculo del total acumulado al registrar cada detalle.
   * Integridad referencial protegida (`on_delete=models.PROTECT`).
3. **Panel Administrativo Personalizado:**
   * Branding corporativo adaptado (`site_header`, `site_title`, `index_title`).
   * Gestión integrada mediante `TabularInline` para añadir detalles de venta en un solo formulario.

---

## 💻 Instalación y Ejecución Local

Si se desea ejecutar el proyecto en un entorno de desarrollo local, seguir estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/jairo-maldonado/BACKENDEVA2.git](https://github.com/jairo-maldonado/BACKENDEVA2.git)
   cd BACKENDEVA2