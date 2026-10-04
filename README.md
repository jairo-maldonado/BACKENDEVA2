# Sistema de Control de Ventas - Django

Este proyecto es una aplicación web desarrollada en Django para la gestión de un inventario de productos y el registro de ventas. Está diseñado para cumplir con altos estándares de desarrollo backend, integrando una base de datos PostgreSQL en la nube y despliegue en producción mediante Vercel.

## 🚀 Funcionalidades Principales

- **CRUD de Productos:** Interfaz pública para Crear, Leer, Actualizar y Eliminar productos del inventario.
- **Gestión de Ventas (Admin):** Registro de ventas mediante el uso de *Inlines* (`DetalleVenta`), permitiendo agregar múltiples productos a una sola transacción.
- **Lógica de Negocio:** 
  - Cálculo automático del total de la venta en base a los subtotales de los productos agregados.
  - Validación de stock disponible antes de registrar un detalle de venta.
- **Interfaz de Usuario (Frontend):** 
  - Diseño responsivo utilizando Bootstrap 5.
  - Paginación implementada en el listado de productos.
  - Sistema de mensajes (Alertas) para notificar al usuario sobre acciones exitosas o errores.
- **Administración Personalizada:** Panel de Django Admin con *Branding* adaptado, filtros de búsqueda y jerarquía por fechas.

## 🛠️ Tecnologías y Herramientas

- **Backend:** Python 3.12, Django 6.1.1
- **Base de Datos:** PostgreSQL alojada en Supabase (Conexión vía Transaction Pooler).
- **Despliegue (Hosting):** Vercel (Serverless Functions).
- **Gestión de Estáticos:** WhiteNoise.
- **Frontend:** HTML5, CSS3, Bootstrap 5.

## ⚙️ Configuración e Instalación Local

Si deseas ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
cd tu-repositorio
```

### 2. Crear y activar el entorno virtual
**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Variables de Entorno
Crea un archivo llamado `.env` en la raíz del proyecto y agrega las siguientes variables (solicita las credenciales de la base de datos al administrador):

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_bd
```

### 5. Aplicar Migraciones
El proyecto utiliza una base de datos en la nube. Para sincronizar las tablas, ejecuta:
```bash
python manage.py migrate
```

### 6. Crear un Superusuario (Opcional)
Para acceder al panel de administración y gestionar las ventas:
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el Servidor Local
```bash
python manage.py runserver
```
El proyecto estará disponible en `http://127.0.0.1:8000/`. Para acceder al panel administrativo, ingresa a `http://127.0.0.1:8000/admin/`.

## 📦 Despliegue en Producción

Este proyecto está configurado para ser desplegado en **Vercel**.
- Las rutas estáticas son manejadas por `WhiteNoise`.
- El archivo `vercel.json` está configurado para utilizar el runtime de Python 3.12.
- El script `build.sh` se encarga de instalar dependencias, recolectar estáticos y aplicar migraciones automáticamente durante el proceso de *build*.

## 👨‍💻 Autor
**Jairo Maldonado** - Estudiante de Ingeniería en Informática.

