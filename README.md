# alembic example

## New database
### 1. Init alembic
```
$ alembic init migrate
```

### 2. Config in `alembic.init` file

```
sqlalchemy.url = postgresql://root:secret@localhost:5432/migration
```

> Make sure: You have import your models in `env.py`, like this:
```py
from project.models import Base, a_class, b_class
```
That make sure the `a_class` and `b_class` will register to alembic integration.

## Existing database

```
$ alembic stamp head
```

## Contributing

If you want to colaborate check the project's issues.

1. Fork the repository
2. Implement your solution
3. Commit
4. Open a Pull Request

Thanks!