# Permissions and Group Configuration

## Custom Permissions

Defined in `Book` model:

- `can_view`: Allows viewing book list
- `can_create`: Allows adding new books
- `can_edit`: Allows editing existing books
- `can_delete`: Allows deleting books

## User Groups

- **Admins**: All permissions
- **Editors**: View, Create, Edit
- **Viewers**: View only

## View Enforcement

Views use the `@permission_required` decorator to restrict access. Users receive a 403 error if they lack permission.

## How to Assign Permissions

1. Go to Admin > Groups.
2. Create groups and assign permissions.
3. Assign users to groups in the admin interface.

