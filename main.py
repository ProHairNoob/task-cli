import click
from tasks import add_cmd, list_all_tasks, update_cmd, delete_cmd, mark_cmd
from storage import make_db

# Initializing database
make_db()


# Initializing Click
@click.group()
def cli():
    pass


cli.add_command(add_cmd)
cli.add_command(list_all_tasks)
cli.add_command(update_cmd)
cli.add_command(delete_cmd)
cli.add_command(mark_cmd)
if __name__ == "__main__":
    cli()
