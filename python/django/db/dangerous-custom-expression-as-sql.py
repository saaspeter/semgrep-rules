from django.db.models.expressions import Func

class ConcatPair(Func):
    function = 'CONCAT'

    # ruleid: dangerous-custom-expression-as-sql
    def as_mysql(self, compiler, connection, **extra_context):
        return super().as_sql(
            compiler, connection,
            function='CONCAT_WS',
            template="%(function)s('', %(expressions)s)",
            **extra_context
        )