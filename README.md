# Challenge for N5

## How to Run Using Docker

### Pre-requisites:
```
Docker
Docker Compose (Newly Added)
```

### Steps:
1. Create a file named `.env` with the necessary environment variables.
2. Build the application with `docker compose build`.
3. Run the application with `docker compose up`.
4. In another terminal, execute tests with `docker compose exec backend pytest -vv`.

### Usage Instructions:
1. In Your Web Browser: 
   - Navigate to `http://localhost:8000/docs/` to access the Swagger Documentation.
   - Register a new user by using the `/register` endpoint under the `register` tag. A new user account also becomes a traffic officer.
   - Sign in with your newly created username and password using the `/sign-in` endpoint under the `sign-in` tag.
   - Copy the `access_token`.
   - Click the `Authorize` button and add the `Bearer + access_token` to authorize access.
   - You can now test all available endpoints, including CRUD operations and generating violation reports.

2. Using Your Web Browser:
   - Visit `http://localhost:8000/admin/` to access the Django Admin interface.
   - Before adding a violation, ensure you've added a vehicle.
   - By default, there are predefined people and vehicle brands.
   - Enter the vehicle license plate in the format 'AZ 123 BZ'.

3. With Your Preferred REST Client:
   - You can test all API endpoints.

### Environment Variables:
```
SECRET_KEY = 'django-insecure-g^o=!kqyy74mgsold)5epo$_=o6mvlfg)l9^ul5bli3=ew79mz'
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_DB=challenge
POSTGRES_HOST=db
```

### Algunos servicios que se pueden considerar en AWS:

1. **Amazon S3**: Se puede utilizar almacenar las imágenes, videos, informes, y cualquier otro archivo necesario para el sistema. Considerando una nueva version de la API!.
2. **Amazon RDS**: Utiliza Amazon RDS para almacenar datos estructurados. En esté momento la app usa PostgreSQL.
3. **Amazon SES**: Si necesitas enviar notificaciones por correo electrónico a los infractores.
4. **Amazon SQS**: Si necesitas procesar tareas en segundo plano de manera asíncrona.

### Repositorios:
```
docker pull chitohugo/challenge-n5:1.0
https://github.com/chitohugo/challenge-n5.git
```