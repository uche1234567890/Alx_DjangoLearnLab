## Authentication Setup

- **Method**: Token Authentication (DRF built-in)
- **Endpoint to get token**: POST `/api/auth/token/`
- **Header format**: `Authorization: Token <your_token>`
- **Permissions**: All Book API endpoints require authentication (`IsAuthenticated`)

## Access Levels

- Users must be logged in to access any CRUD operation.
- You can replace `IsAuthenticated` with `IsAdminUser` or a custom permission class.